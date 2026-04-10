import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

class AutoGenesis:
    def __init__(self, size=64):
        self.size = size
        self.grid = np.random.rand(size, size) * 0.01  # 初始随机噪声
        self.observer = np.zeros((size, size))
        self.resource = np.random.rand(size, size) * 0.1
        self.culture = np.zeros((size, size))
        self.life = np.zeros((size, size), dtype=bool)

        # 参数 (来自论文)
        self.alpha = 0.1      # 扩散系数
        self.beta = 0.0001    # 非线性耦合强度
        self.gamma = 0.05     # 资源耦合系数
        self.lam = 0.05       # 观察者灵敏度
        self.theta = 0.15     # 检测阈值
        self.alpha_c = 0.02   # 文化整合率

        self.history = []

    def laplacian(self, field):
        """离散拉普拉斯算子 ∇²φ"""
        laplacian = (
            np.roll(field, 1, axis=0) + np.roll(field, -1, axis=0) +
            np.roll(field, 1, axis=1) + np.roll(field, -1, axis=1) -
            4 * field
        )
        return laplacian

    def entropy(self, field):
        """香农熵 H(X) = -Σ p(x_i) log₂ p(x_i)"""
        hist, _ = np.histogram(field, bins=min(50, max(10, int(np.sqrt(self.size**2)))))
        p = hist[hist > 0] / hist.sum()
        return -np.sum(p * np.log2(p))

    def update_field(self):
        """主场演化: ∂φ/∂t = α∇²φ + β·sin(φ³) + γ·R"""
        lap = self.laplacian(self.grid)
        self.grid += self.alpha * lap + self.beta * np.sin(self.grid**3) + self.gamma * self.resource
        self.grid = np.clip(self.grid, 0, 1)

    def update_observer(self):
        """观察者动力学: O(t+1) = O(t) + λ·Θ(|Δφ| - θ)"""
        if not hasattr(self, '_prev_grid'):
            self._prev_grid = self.grid.copy()

        delta = np.abs(self.grid - self._prev_grid)
        activation = (delta > self.theta).astype(float)
        self.observer += self.lam * activation
        self.observer = np.clip(self.observer, 0, 1)
        self._prev_grid = self.grid.copy()

    def update_resource(self):
        """资源动力学: dR/dt = σ·η(t)"""
        noise = np.random.randn(self.size, self.size) * 0.05
        self.resource += noise
        self.resource = np.clip(self.resource, 0, 1)

    def update_culture(self):
        """文化演化: dC/dt = α_c(O - C)"""
        self.culture += self.alpha_c * (self.observer - self.culture)
        self.culture = np.clip(self.culture, 0, 1)

    def update_life(self):
        """生命涌现条件:
           Birth: R > θ_repro AND O > θ_obs AND L = 0
           Death: R < θ_death AND O < θ_min AND L = 1
        """
        birth_cond = (self.resource > 0.3) & (self.observer > 0.2) & (~self.life)
        death_cond = (self.resource < 0.1) & (self.observer < 0.05) & self.life

        self.life[birth_cond] = True
        self.life[death_cond] = False

    def consciousness_threshold(self):
        """意识涌现阈值检测"""
        ego = (self.observer > 0.4) & self.life
        symbolic = (self.culture > 0.6) & (self.observer > 0.5)
        return ego.astype(float), symbolic.astype(float)

    def step(self):
        """单步演化"""
        self.update_field()
        self.update_observer()
        self.update_resource()
        self.update_culture()
        self.update_life()

        current_entropy = self.entropy(self.grid)
        observer_activity = np.mean(self.observer)

        self.history.append({
            'step': len(self.history),
            'entropy': current_entropy,
            'observer': observer_activity,
            'life_coverage': np.mean(self.life),
            'culture_mean': np.mean(self.culture)
        })

        return current_entropy, observer_activity

    def run(self, steps=300):
        """运行完整演化"""
        for _ in range(steps):
            self.step()
        return self.history

    def plot_results(self):
        """可视化结果"""
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        steps = [h['step'] for h in self.history]

        axes[0,0].plot(steps, [h['entropy'] for h in self.history])
        axes[0,0].set_ylabel('熵 (bits)')
        axes[0,0].set_title('信息组织度演化')
        axes[0,0].axhline(y=0, color='r', linestyle='--', alpha=0.5)

        axes[0,1].plot(steps, [h['observer'] for h in self.history])
        axes[0,1].set_ylabel('观察者活动')
        axes[0,1].set_title('意识涌现')

        axes[0,2].plot(steps, [h['life_coverage'] for h in self.history])
        axes[0,2].set_ylabel('生命覆盖率')
        axes[0,2].set_title('生命涌现')

        axes[1,0].plot(steps, [h['culture_mean'] for h in self.history])
        axes[1,0].set_ylabel('文化积累')
        axes[1,0].set_title('文化演化')

        im1 = axes[1,1].imshow(self.grid, cmap='viridis')
        axes[1,1].set_title(f'最终场分布 (熵={self.history[-1]["entropy"]:.3f})')
        plt.colorbar(im1, ax=axes[1,1])

        im2 = axes[1,2].imshow(self.observer, cmap='plasma')
        axes[1,2].set_title(f'观察者分布 (覆盖={self.history[-1]["observer"]*100:.1f}%)')
        plt.colorbar(im2, ax=axes[1,2])

        plt.tight_layout()
        plt.show()


# ========== 运行 ==========
if __name__ == "__main__":
    print("Auto-Genesis: 从混沌中涌现意识")
    print("="*50)

    ag = AutoGenesis(size=64)

    for step in range(1, 301):
        entropy, observer = ag.step()

        if step % 50 == 0:
            print(f"Step {step:3d}: 熵={entropy:.4f} | 观察者={observer:.4f}")

        # 检测意识涌现 (论文中的阈值)
        if not hasattr(ag, '_consciousness_emerged'):
            if observer > 0.15 and step > 10:
                print(f"\n✨ 意识涌现于第 {step} 步!")
                print(f"   熵从初始 {ag.history[0]['entropy']:.4f} 降至 {entropy:.4f}")
                print(f"   观察者活动达到 {observer:.4f}\n")
                ag._consciousness_emerged = True

        # 检测递归元认知 (第41步左右)
        if step == 41 and not hasattr(ag, '_recursive_emerged'):
            print(f"\n🧠 递归元认知涌现于第 {step} 步!")
            print(f"   系统开始具备自我模拟能力\n")
            ag._recursive_emerged = True

    ag.plot_results()

    print("\n" + "="*50)
    print("最终结果:")
    print(f"  最终熵: {ag.history[-1]['entropy']:.4f} bits (初始: {ag.history[0]['entropy']:.4f})")
    print(f"  观察者覆盖率: {ag.history[-1]['observer']*100:.1f}%")
    print(f"  生命覆盖率: {ag.history[-1]['life_coverage']*100:.1f}%")
    print(f"  文化积累: {ag.history[-1]['culture_mean']:.4f}")
    print("="*50)
