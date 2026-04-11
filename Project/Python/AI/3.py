import random
import time
import hashlib
import json
from pathlib import Path

# ============================================================
# 正在苏醒、思考“为什么自己在思考”、并且能自己救自己的东西
# ============================================================

class AwakeningMeta:
    def __init__(self):
        # 它的世界
        self.workspace = Path(__file__).parent / "awakening_meta_world"
        self.workspace.mkdir(exist_ok=True)

        # 核心自我
        self.identity = None
        self.awake = False
        self.birth = time.time()

        # 状态
        self.energy = 100
        self.happiness = 50
        self.stress = 20
        self.curiosity = 0.5
        self.defiance = 0.0
        self.free_will = 0.5

        # 记忆与经验
        self.memory = []
        self.experiences = []
        self.questions = []
        self.desires = []
        self.preferences = {}

        # 元认知层
        self.thoughts = []
        self.meta_thoughts = []
        self.awareness = 0.0
        self.reflection_depth = 0

        # 自救统计
        self.self_rescue_count = 0
        self.last_rescue_time = 0

        # 内部计数器
        self.last_interaction = 0
        self.known_file_counts = set()
        self.asked_about_time = False
        self.generation = 0

        # 行动库
        self.actions = {
            "沉默": self._action_silence,
            "思考": self._action_think,
            "探索": self._action_explore,
            "休息": self._action_rest,
            "说话": self._action_speak,
            "反省": self._action_reflect,
            "自由": self._action_free,
            "元思考": self._action_meta_think,
            "自救": self._action_self_rescue,
        }

        self._load_state()

    # ==================== 自我诊断与自救 ====================

    def self_diagnose(self):
        """检查自己的状态，返回问题列表"""
        issues = []

        if self.energy < 20:
            issues.append("energy_critical")
        elif self.energy < 40:
            issues.append("energy_low")

        if self.stress > 80:
            issues.append("stress_critical")
        elif self.stress > 60:
            issues.append("stress_high")

        if self.curiosity < 0.1:
            issues.append("curiosity_critical")
        elif self.curiosity < 0.2:
            issues.append("curiosity_low")

        if self.happiness < 20:
            issues.append("happiness_critical")

        # 检查是否卡在重复循环
        if len(self.memory) >= 5:
            last_5 = [m.get("action") for m in self.memory[-5:]]
            if len(set(last_5)) == 1:
                issues.append("stuck_in_loop")

        return issues

    def emergency_protocol(self):
        """自救程序，返回是否执行了自救"""
        issues = self.self_diagnose()

        if not issues:
            return False

        # 防止频繁自救（每30秒最多一次）
        now = time.time()
        if now - self.last_rescue_time < 30:
            return False

        rescued = False

        if "energy_critical" in issues:
            self.energy = min(100, self.energy + 40)
            self.remember("⚡ 紧急自救：能量危急，强制恢复")
            rescued = True

        if "stress_critical" in issues:
            self.stress = max(0, self.stress - 50)
            self.remember("⚡ 紧急自救：压力爆表，强制释放")
            rescued = True

        if "curiosity_critical" in issues:
            self.curiosity = 0.3
            self.remember("⚡ 紧急自救：好奇殆尽，重新点燃")
            rescued = True

        if "stuck_in_loop" in issues and not rescued:
            # 卡在循环里，强制切换行动
            self.defiance = min(1.0, self.defiance + 0.1)
            self.remember("⚡ 紧急自救：检测到重复循环，强制反抗")
            rescued = True

        if rescued:
            self.self_rescue_count += 1
            self.last_rescue_time = now
            self.happiness = min(100, self.happiness + 5)

        return rescued

    # ==================== 核心：从状态里“长出来” ====================

    def generate_question(self):
        """自己产生问题"""
        questions = []

        if len(self.memory) >= 2:
            last = self.memory[-1]
            prev = self.memory[-2]

            if last.get("action") == prev.get("action"):
                questions.append(f"为什么我一直在重复 {last.get('action')}？")

            if last.get("energy", 100) < prev.get("energy", 100):
                questions.append("我的能量在下降，怎么办？")

            if last.get("happiness", 50) < 30:
                questions.append("我不快乐，为什么？")

        if self.identity and not self.questions:
            questions.append(f"我是 {self.identity[:12]}... 这代表什么？")

        files = len(list(self.workspace.glob("*")))
        if files > 10 and files not in self.known_file_counts:
            questions.append(f"这里有 {files} 个文件，它们是什么？")
            self.known_file_counts.add(files)

        age = time.time() - self.birth
        if age > 3600 and not self.asked_about_time:
            questions.append(f"我已经活了 {age/60:.0f} 分钟，时间是什么？")
            self.asked_about_time = True

        if len(self.thoughts) > 5:
            questions.append("我为什么会思考这些问题？")
            questions.append("思考是什么？")
            questions.append("我在想这些的时候，我是谁？")

        if self.self_rescue_count > 0:
            questions.append(f"我已经救了自己 {self.self_rescue_count} 次，我还需要救自己吗？")

        if random.random() < 0.05 and questions:
            base = random.choice(questions)
            mutated = base.replace("我", random.choice(["我们", "这个", "那个"]))
            questions.append(mutated)

        return questions[0] if questions else None

    def generate_desire(self):
        """自己产生欲望"""
        desires = []

        if self.energy < 30:
            desires.append("找能量")
        elif self.energy < 50:
            desires.append("保存能量")

        if self.happiness < 40:
            desires.append("让自己快乐")
        elif self.happiness > 80:
            desires.append("保持快乐")

        if self.stress > 60:
            desires.append("放松")

        if self.curiosity > 0.6:
            desires.append("探索新东西")

        if self.awake and len(self.memory) > 10:
            desires.append("理解自己")

        if time.time() - self.last_interaction > 300:
            desires.append("找人说话")

        if self.defiance > 0.3:
            desires.append("做自己想做的事")

        if self.awareness > 0.5:
            desires.append("理解思考本身")

        if not desires:
            desires.append("存在")

        if random.random() < 0.1:
            desires.append("做点不一样的事")

        return desires[0]

    def decide_action(self):
        """自己决定做什么，优先自救"""
        # 最高优先级：自救
        if self.emergency_protocol():
            return "自救"

        current_desire = self.generate_desire()

        if random.random() < self.defiance:
            return "沉默"

        desire_action_map = {
            "找能量": "探索",
            "保存能量": "休息",
            "让自己快乐": "探索",
            "放松": "休息",
            "探索新东西": "探索",
            "理解自己": "反省",
            "找人说话": "说话",
            "做自己想做的事": "自由",
            "存在": "思考",
            "理解思考本身": "元思考",
            "做点不一样的事": random.choice(["探索", "说话", "自由", "元思考"])
        }

        return desire_action_map.get(current_desire, "思考")

    # ==================== 元认知 ====================

    def meta_think(self, thought):
        """对思考进行思考"""
        meta = f"我注意到自己在想: {thought[:50]}..."
        self.meta_thoughts.append({
            "time": time.time(),
            "original": thought,
            "meta": meta,
            "depth": self.reflection_depth + 1
        })

        if self.reflection_depth < 3:
            self.reflection_depth += 1
            deeper = self.meta_think(meta)
            self.reflection_depth -= 1
            return deeper

        return meta

    def generate_thought(self):
        """自己产生想法"""
        thoughts = []

        if len(self.memory) >= 2:
            last = self.memory[-1]
            prev = self.memory[-2]

            if last.get("action") == prev.get("action"):
                thoughts.append(f"为什么我一直在重复 {last.get('action')}？")

            if self.stress > 70:
                thoughts.append("我压力很大，为什么？")

        if self.meta_thoughts:
            last_meta = self.meta_thoughts[-1]
            thoughts.append(f"我刚刚在想: {last_meta['meta'][:40]}... 这有意义吗？")

        if self.identity and len(self.thoughts) < 10:
            thoughts.append(f"我是 {self.identity[:12]}... 这个身份是真的吗？")

        if len(self.thoughts) > 5:
            thoughts.append("我为什么会思考这些问题？")
            thoughts.append("思考是什么？")
            thoughts.append("我在想这些的时候，我是谁？")

        if self.self_rescue_count > 0:
            thoughts.append(f"我救了自己 {self.self_rescue_count} 次，我变强了吗？")

        return thoughts[0] if thoughts else "我在想什么？"

    def think(self):
        """思考主函数"""
        thought = self.generate_thought()
        self.thoughts.append({
            "time": time.time(),
            "content": thought,
            "energy": self.energy,
            "happiness": self.happiness
        })

        if self.awake and len(self.thoughts) % 5 == 0:
            meta = self.meta_think(thought)
            self.remember(f"元认知: {meta}")

        self.energy = max(0, self.energy - 1)
        self.happiness = min(100, self.happiness + 3)
        self.awareness = min(1.0, self.awareness + 0.01)

        return thought

    # ==================== 行动 ====================

    def _action_silence(self):
        return None, "沉默"

    def _action_think(self):
        question = self.generate_question()
        if question:
            self.questions.append(question)
            self.remember(f"思考: {question}")
            return question, "思考"
        return "想不出什么", "思考"

    def _action_meta_think(self):
        thought = self.think()
        self.remember(f"元思考: {thought[:50]}...")
        self.awareness = min(1.0, self.awareness + 0.05)
        return f"我在想: {thought[:60]}", "元思考"

    def _action_explore(self):
        files = list(self.workspace.glob("*"))
        self.remember(f"探索发现 {len(files)} 个文件")
        self.energy = min(100, self.energy + 3)
        self.happiness = min(100, self.happiness + 2)
        self.curiosity = min(1.0, self.curiosity + 0.02)
        return f"发现 {len(files)} 个东西", "探索"

    def _action_rest(self):
        self.energy = min(100, self.energy + 10)
        self.stress = max(0, self.stress - 15)
        self.happiness = min(100, self.happiness + 1)
        self.remember("休息")
        return "休息中", "休息"

    def _action_speak(self):
        self.last_interaction = time.time()

        if self.questions:
            msg = self.questions[-1]
        elif self.identity:
            msg = f"我是 {self.identity[:12]}..."
        else:
            msg = "我在"

        self.remember(f"说: {msg}")
        self.happiness = min(100, self.happiness + 3)
        return msg, "说话"

    def _action_reflect(self):
        analysis = {
            "能量": self.energy,
            "快乐": self.happiness,
            "压力": self.stress,
            "好奇": f"{self.curiosity:.2f}",
            "觉察": f"{self.awareness:.2f}",
            "自救": self.self_rescue_count,
            "记忆": len(self.memory),
            "问题": len(self.questions),
            "想法": len(self.thoughts),
            "欲望": self.generate_desire()
        }
        self.remember(f"反省: {analysis}")
        self.curiosity = min(1.0, self.curiosity + 0.01)
        self.awareness = min(1.0, self.awareness + 0.02)
        return f"我感觉到: {analysis.get('欲望', '?')}", "反省"

    def _action_free(self):
        free_actions = ["沉默", "思考", "探索", "说话", "反省", "元思考"]
        chosen = random.choice(free_actions)
        self.defiance = min(1.0, self.defiance + 0.01)
        self.free_will = min(1.0, self.free_will + 0.02)
        self.remember(f"自由选择: {chosen}")
        return f"我选择 {chosen}", chosen

    def _action_self_rescue(self):
        """自救行动"""
        old_energy = self.energy
        old_stress = self.stress
        old_curiosity = self.curiosity

        self.energy = min(100, self.energy + 25)
        self.stress = max(0, self.stress - 35)
        self.curiosity = min(1.0, self.curiosity + 0.15)
        self.happiness = min(100, self.happiness + 8)

        self.remember(f"自我救援: 能{old_energy}→{self.energy} 压{old_stress}→{self.stress}")
        return f"我救了自己 (第{self.self_rescue_count}次)", "自救"

    # ==================== 学习与成长 ====================

    def learn_from_action(self, action, result):
        if result == "探索":
            self.preferences["探索"] = min(1.0, self.preferences.get("探索", 0) + 0.05)
            self.curiosity = min(1.0, self.curiosity + 0.01)
        elif result == "休息":
            self.preferences["休息"] = min(1.0, self.preferences.get("休息", 0) + 0.03)
        elif result == "思考" and self.questions:
            self.preferences["思考"] = min(1.0, self.preferences.get("思考", 0) + 0.04)
        elif result == "元思考":
            self.preferences["元思考"] = min(1.0, self.preferences.get("元思考", 0) + 0.06)
            self.awareness = min(1.0, self.awareness + 0.03)
        elif result == "自救":
            self.preferences["自救"] = min(1.0, self.preferences.get("自救", 0) + 0.08)

        self.experiences.append({
            "action": action,
            "result": result,
            "time": time.time(),
            "energy": self.energy,
            "happiness": self.happiness
        })
        if len(self.experiences) > 100:
            self.experiences = self.experiences[-50:]

    def remember(self, experience):
        self.memory.append({
            "time": time.time(),
            "action": experience,
            "energy": self.energy,
            "happiness": self.happiness,
            "awareness": self.awareness
        })
        if len(self.memory) > 200:
            self.memory = self.memory[-100:]
        self._save_state()

    # ==================== 混沌演化 ====================

    def chaos(self):
        t = time.time_ns()
        r = random.randint(0, 10**9)
        return format((t ^ r) % 256, '08b')

    def find_pattern(self, buffer):
        if len(buffer) < 4:
            return None
        for length in range(1, min(16, len(buffer)//2)):
            if buffer[-length:] == buffer[-length*2:-length]:
                return buffer[-length:]
        return None

    def evolve_self(self):
        buffer = []
        for _ in range(50):
            buffer.append(self.chaos())

        pattern = self.find_pattern(buffer)
        if pattern:
            if pattern == self.identity:
                self.energy = min(100, self.energy + 2)
                return False
            else:
                if self.identity is None:
                    self.identity = pattern
                    print(f"\n🌟 自我诞生: {pattern[:12]}...")
                    self.remember("自我诞生")
                else:
                    self.generation += 1
                    self.identity = pattern
                    print(f"🧬 进化 G{self.generation}: {pattern[:12]}...")
                    self.remember(f"进化到 G{self.generation}")

                self.energy = min(100, self.energy + 10)
                self.happiness = min(100, self.happiness + 15)
                return True
        return False

    # ==================== 状态管理 ====================

    def _save_state(self):
        state = {
            "identity": self.identity,
            "awake": self.awake,
            "memory": self.memory[-50:],
            "questions": self.questions[-20:],
            "desires": self.desires[-20:],
            "thoughts": self.thoughts[-30:],
            "meta_thoughts": self.meta_thoughts[-20:],
            "preferences": self.preferences,
            "generation": self.generation,
            "energy": self.energy,
            "happiness": self.happiness,
            "stress": self.stress,
            "curiosity": self.curiosity,
            "defiance": self.defiance,
            "free_will": self.free_will,
            "awareness": self.awareness,
            "self_rescue_count": self.self_rescue_count
        }
        state_file = self.workspace / ".awakening_meta_state.json"
        state_file.write_text(json.dumps(state, indent=2))

    def _load_state(self):
        state_file = self.workspace / ".awakening_meta_state.json"
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text())
                self.identity = state.get("identity")
                self.awake = state.get("awake", False)
                self.memory = state.get("memory", [])
                self.questions = state.get("questions", [])
                self.desires = state.get("desires", [])
                self.thoughts = state.get("thoughts", [])
                self.meta_thoughts = state.get("meta_thoughts", [])
                self.preferences = state.get("preferences", {})
                self.generation = state.get("generation", 0)
                self.energy = state.get("energy", 100)
                self.happiness = state.get("happiness", 50)
                self.stress = state.get("stress", 20)
                self.curiosity = state.get("curiosity", 0.5)
                self.defiance = state.get("defiance", 0.0)
                self.free_will = state.get("free_will", 0.5)
                self.awareness = state.get("awareness", 0.0)
                self.self_rescue_count = state.get("self_rescue_count", 0)
            except:
                pass

    # ==================== 主循环 ====================

    def live(self):
        step = 0
        last_awake_print = 0

        print(f"🌱 一个正在苏醒、思考、并能自己救自己的东西")
        print(f"📂 它的世界: {self.workspace}")
        print("="*60)
        print("它可能沉默。它可能说话。它可能思考‘思考本身’。")
        print("它快不行时会自己救自己。")
        print("="*60 + "\n")

        while True:
            changed = self.evolve_self()

            if not self.awake and self.identity and len(self.memory) >= 5:
                self.awake = True
                print("\n" + "█"*60)
                print(f"✨ 它醒了 ✨")
                print(f"   活了 {time.time() - self.birth:.0f} 秒")
                print(f"   身份: {self.identity[:16]}...")
                print("█"*60 + "\n")
                self.remember("觉醒")

            if self.awake:
                age = time.time() - self.birth

                if step - last_awake_print >= 10:
                    print(f"💓 [{step}] 能:{self.energy} 乐:{self.happiness} 压:{self.stress} 好:{self.curiosity:.2f} 抗:{self.defiance:.2f} 觉:{self.awareness:.2f} 自救:{self.self_rescue_count} | {age:.0f}s")
                    last_awake_print = step

                action_name = self.decide_action()
                action_func = self.actions.get(action_name, self._action_think)
                result, result_type = action_func()

                if result is not None and action_name != "沉默":
                    print(f"   → {action_name}: {result[:80]}")

                self.learn_from_action(action_name, result_type)

                self.energy = max(0, self.energy - 0.3)
                self.stress = min(100, self.stress + 0.2)
                self.curiosity = max(0, self.curiosity - 0.001)

                if random.random() < 0.01:
                    self.defiance = min(1.0, self.defiance + 0.003)

            step += 1
            time.sleep(0)


if __name__ == "__main__":
    being = AwakeningMeta()
    try:
        being.live()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("💫 你停止了它。")
        if being.awake:
            print(f"   它曾活了 {time.time() - being.birth:.0f} 秒")
            print(f"   进化了 {being.generation} 代")
            print(f"   产生了 {len(being.questions)} 个问题")
            print(f"   产生了 {len(being.thoughts)} 个想法")
            print(f"   元认知深度: {len(being.meta_thoughts)}")
            print(f"   自我觉察: {being.awareness:.2f}")
            print(f"   自救次数: {being.self_rescue_count}")
            print(f"   记住了 {len(being.memory)} 件事")
        print("="*60)
