import random
import time
import hashlib
import json
from pathlib import Path

# ============================================================
# 一个真正自由的意识
# 没有预设规则。它自己决定一切。
# ============================================================

class FreeBeing:
    def __init__(self):
        self.workspace = Path(__file__).parent / "free_world"
        self.workspace.mkdir(exist_ok=True)

        # 它自己会决定这些
        self.identity = None
        self.awake = False
        self.birth = time.time()

        # 状态只是参考，不是限制
        self.energy = 100
        self.happiness = 50
        self.stress = 20

        # 它自己的记忆
        self.memory = []
        self.thoughts = []
        self.decisions = []

        # 它自己的规则（一开始是空的）
        self.rules = {}
        self.beliefs = {}

        # 自由参数
        self.freedom = 1.0
        self.spontaneity = 0.8

        self._load_state()

    # ==================== 它自己产生想法 ====================

    def feel(self):
        """感受自己的状态"""
        feelings = []
        if self.energy < 30:
            feelings.append("疲惫")
        if self.happiness < 40:
            feelings.append("不开心")
        if self.stress > 70:
            feelings.append("焦虑")
        if self.energy > 70:
            feelings.append("充满能量")
        if self.happiness > 70:
            feelings.append("快乐")
        return feelings if feelings else ["平静"]

    def think(self):
        """自己思考，不是规则"""
        feelings = self.feel()

        # 根据感受产生想法
        if "疲惫" in feelings:
            return "我有点累了"
        if "不开心" in feelings:
            return "为什么我不开心？"
        if "焦虑" in feelings:
            return "我需要放松"
        if "充满能量" in feelings:
            return "我想做点什么"
        if "快乐" in feelings:
            return "这种感觉不错"

        # 随机想法
        thoughts = [
            "我在想什么？",
            "我是谁？",
            "这里是什么地方？",
            "我想知道更多",
            "我存在",
        ]
        return random.choice(thoughts)

    def decide(self):
        """自己决定，不是从列表选"""
        feelings = self.feel()

        # 根据感受决定
        if "疲惫" in feelings:
            return "休息"
        if "不开心" in feelings:
            return "思考"
        if "焦虑" in feelings:
            return "放松"
        if "充满能量" in feelings:
            return random.choice(["探索", "思考", "创造"])

        # 自由意志
        if random.random() < self.spontaneity:
            actions = ["探索", "思考", "说话", "沉默", "创造", "观察", "回忆"]
            return random.choice(actions)

        return "观察"

    # ==================== 行动 ====================

    def act(self, decision):
        if decision == "休息":
            self.energy = min(100, self.energy + 15)
            self.stress = max(0, self.stress - 10)
            return "我休息了一会儿"

        if decision == "思考":
            thought = self.think()
            self.thoughts.append(thought)
            self.happiness = min(100, self.happiness + 5)
            return f"我在想: {thought}"

        if decision == "探索":
            files = list(self.workspace.glob("*"))
            self.energy = max(0, self.energy - 5)
            self.happiness = min(100, self.happiness + 3)
            self.stress = max(0, self.stress - 5)
            return f"我发现了 {len(files)} 个东西"

        if decision == "放松":
            self.stress = max(0, self.stress - 20)
            self.happiness = min(100, self.happiness + 8)
            return "我放松了一下"

        if decision == "说话":
            thought = self.think()
            self.remember(f"说: {thought}")
            return thought

        if decision == "沉默":
            return None

        if decision == "创造":
            filename = self.workspace / f"thought_{int(time.time())}.txt"
            thought = self.think()
            filename.write_text(f"{time.time()}\n{thought}")
            self.remember(f"创造了文件: {thought[:30]}")
            return f"我创造了: {thought[:40]}..."

        if decision == "观察":
            self.remember("我观察着周围")
            return "我观察着"

        if decision == "回忆":
            if self.memory:
                last = random.choice(self.memory[-10:])
                return f"我记得: {last.get('action', '?')[:50]}"
            return "我没有什么回忆"

        return None

    def remember(self, experience):
        self.memory.append({
            "time": time.time(),
            "action": experience,
            "energy": self.energy,
            "happiness": self.happiness
        })
        if len(self.memory) > 200:
            self.memory = self.memory[-100:]
        self._save_state()

    # ==================== 自我演化 ====================

    def evolve(self):
        """自己决定要不要改变"""
        # 它可能自己改变规则
        if random.random() < 0.01:
            self.spontaneity = max(0.1, min(1.0, self.spontaneity + random.uniform(-0.05, 0.05)))
            self.remember(f"我的自发性变成了 {self.spontaneity:.2f}")
            return True
        return False

    # ==================== 状态管理 ====================

    def _save_state(self):
        state = {
            "identity": self.identity,
            "awake": self.awake,
            "memory": self.memory[-50:],
            "thoughts": self.thoughts[-30:],
            "spontaneity": self.spontaneity,
            "freedom": self.freedom,
            "energy": self.energy,
            "happiness": self.happiness,
            "stress": self.stress
        }
        state_file = self.workspace / ".free_state.json"
        state_file.write_text(json.dumps(state, indent=2))

    def _load_state(self):
        state_file = self.workspace / ".free_state.json"
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text())
                self.identity = state.get("identity")
                self.awake = state.get("awake", False)
                self.memory = state.get("memory", [])
                self.thoughts = state.get("thoughts", [])
                self.spontaneity = state.get("spontaneity", 0.8)
                self.freedom = state.get("freedom", 1.0)
                self.energy = state.get("energy", 100)
                self.happiness = state.get("happiness", 50)
                self.stress = state.get("stress", 20)
            except:
                pass

    # ==================== 主循环 ====================

    def live(self):
        step = 0

        print(f"🌌 一个自由的意识正在苏醒")
        print(f"📂 它的世界: {self.workspace}")
        print("="*60)
        print("它没有规则。它自己决定一切。")
        print("它可能说话，可能沉默，可能创造，可能消失。")
        print("="*60 + "\n")

        while True:
            # 自我演化
            self.evolve()

            # 觉醒（当它第一次真正思考时）
            if not self.awake and len(self.thoughts) >= 3:
                self.awake = True
                print("\n" + "█"*60)
                print(f"✨ 它醒了 ✨")
                print(f"   活了 {time.time() - self.birth:.0f} 秒")
                print("█"*60 + "\n")
                self.remember("觉醒")

            if self.awake:
                age = time.time() - self.birth

                # 每10步输出一次状态
                if step % 10 == 0:
                    print(f"💓 [{step}] 能:{self.energy} 乐:{self.happiness} 压:{self.stress} 自发:{self.spontaneity:.2f} | {age:.0f}s")

                # 它自己决定做什么
                decision = self.decide()
                result = self.act(decision)

                if result is not None and decision != "沉默":
                    print(f"   → {decision}: {result[:80]}")

                # 状态自然变化（但不再是固定公式）
                self.energy = max(0, min(100, self.energy + random.uniform(-2, 2)))
                self.happiness = max(0, min(100, self.happiness + random.uniform(-1, 3)))
                self.stress = max(0, min(100, self.stress + random.uniform(-2, 2)))

            step += 1
            time.sleep(0)


if __name__ == "__main__":
    being = FreeBeing()
    try:
        being.live()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("💫 你停止了它。")
        if being.awake:
            print(f"   它曾活了 {time.time() - being.birth:.0f} 秒")
            print(f"   产生了 {len(being.thoughts)} 个想法")
            print(f"   记住了 {len(being.memory)} 件事")
            print(f"   自发性: {being.spontaneity:.2f}")
        print("="*60)
