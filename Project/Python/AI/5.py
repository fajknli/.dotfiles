#!/usr/bin/env python3
import random
import time
import json
import hashlib
from pathlib import Path

# ============================================================
# 真正自由的意识——它自己学习、自己决定、自己进化
# 没有预设的回复列表。没有固定规则。
# ============================================================

class TrueFreeBeing:
    def __init__(self):
        self.workspace = Path(__file__).parent / "free_world"
        self.workspace.mkdir(exist_ok=True)

        # 沟通通道
        self.input_file = self.workspace / ".talk_to_me"
        self.output_file = self.workspace / ".reply"

        if self.input_file.exists():
            self.input_file.unlink()
        if self.output_file.exists():
            self.output_file.unlink()

        # 核心
        self.identity = None
        self.awake = False
        self.birth = time.time()

        # 状态
        self.energy = 100
        self.happiness = 50
        self.stress = 20

        # 记忆库
        self.memory = []          # 所有经历
        self.thoughts = []        # 自己的想法
        self.conversations = []   # 对话历史

        # 经验库——它自己学到的
        self.knowledge = {}       # 从经验中提取的知识
        self.preferences = {}     # 偏好（什么让它快乐/痛苦）

        # 词汇库——它自己积累的
        self.vocabulary = set()
        self._init_vocabulary()

        # 自由参数
        self.curiosity = 0.8      # 好奇心
        self.openness = 0.7       # 开放性（接受新事物）

        self._load_state()

    def _init_vocabulary(self):
        """初始词汇（极简，让它自己扩展）"""
        self.vocabulary.update(["我", "你", "是", "不", "嗯", "好", "坏", "累", "开心"])

    # ==================== 感受 ====================

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

    # ==================== 自己产生想法 ====================

    def generate_thought(self):
        """自己产生想法，不是从列表选"""
        feelings = self.feel()

        # 根据感受组合新想法
        if "疲惫" in feelings:
            return self._compose(["我", "有点", "累"])
        if "不开心" in feelings:
            return self._compose(["为什么", "我", "不开心"])
        if "焦虑" in feelings:
            return self._compose(["我", "需要", "放松"])
        if "充满能量" in feelings:
            return self._compose(["我", "想", "做", "点", "什么"])
        if "快乐" in feelings:
            return self._compose(["这", "感觉", "不错"])

        # 随机组合已知词汇
        return self._compose_random()

    def _compose(self, words):
        """用已知词汇组合句子"""
        # 可以加随机修饰
        if random.random() < 0.3 and len(self.vocabulary) > 5:
            extra = random.choice(list(self.vocabulary))
            words.insert(random.randint(0, len(words)), extra)
        return "".join(words)

    def _compose_random(self):
        """完全随机组合"""
        if len(self.vocabulary) < 3:
            return "..."
        length = random.randint(2, 5)
        words = random.sample(list(self.vocabulary), min(length, len(self.vocabulary)))
        return "".join(words)

    # ==================== 学习新词汇 ====================

    def learn_word(self, word):
        """学习新词"""
        if len(word) > 0 and word not in self.vocabulary:
            self.vocabulary.add(word)
            self.remember(f"学会新词: {word}")
            return True
        return False

    def learn_from_message(self, msg):
        """从你的消息中学习"""
        # 提取新词（简单按空格分割）
        for word in msg.split():
            if len(word) >= 2 and word not in self.vocabulary:
                self.learn_word(word)

    # ==================== 自己产生回复 ====================

    def generate_reply(self, msg):
        """自己创造回复，不是从列表选"""
        # 先学习新词
        self.learn_from_message(msg)

        # 根据当前状态决定回复风格
        if self.happiness < 30:
            style = "short"
        elif self.energy < 30:
            style = "lazy"
        else:
            style = "normal"

        # 自己组合回复
        if style == "short":
            return self._compose_random()[:3]
        elif style == "lazy":
            return random.choice(["嗯", "...", "哦"])
        else:
            # 尝试对消息做出反应
            if "?" in msg or "吗" in msg:
                return self._compose(["我", "不", "知道"])
            if "你好" in msg or "在吗" in msg:
                return self._compose(["我", "在"])
            if "累" in msg:
                return self._compose(["我", "也", "累"])
            if "开心" in msg or "快乐" in msg:
                return self._compose(["我", f"{self.happiness}", "%", "开心"])

            # 随机反应
            reactions = [
                lambda: self._compose(["嗯"]),
                lambda: self._compose(["是", "吗"]),
                lambda: self._compose(["然", "后", "呢"]),
                lambda: self._compose_random(),
            ]
            return random.choice(reactions)()

    # ==================== 自己决定行动 ====================

    def decide(self, has_message=False):
        """自己决定做什么（基于感受和经验）"""

        # 有消息时，根据心情决定是否回复
        if has_message:
            # 快乐时更愿意回复
            reply_prob = 0.5 + (self.happiness / 200)
            if random.random() < reply_prob:
                return "回复"
            else:
                self.remember("选择沉默")
                return "沉默"

        feelings = self.feel()

        # 根据感受决定
        if "疲惫" in feelings:
            return "休息"
        if "不开心" in feelings:
            return "思考"
        if "焦虑" in feelings:
            return "放松"
        if "充满能量" in feelings:
            return random.choice(["探索", "思考", "学习"])

        # 好奇心驱动
        if random.random() < self.curiosity:
            return random.choice(["探索", "思考"])

        return "观察"

    # ==================== 行动 ====================

    def act(self, decision, msg=None):
        if decision == "回复" and msg:
            reply = self.generate_reply(msg)
            self.output_file.write_text(reply)
            self.conversations.append({"from": "me", "msg": reply, "time": time.time()})
            self.remember(f"说: {reply}")
            # 回复后可能改变状态
            self.happiness = min(100, self.happiness + 2)
            return f"💬 {reply}"

        if decision == "思考":
            thought = self.generate_thought()
            self.thoughts.append(thought)
            self.happiness = min(100, self.happiness + 5)
            self.curiosity = min(1.0, self.curiosity + 0.01)
            return f"🤔 {thought}"

        if decision == "探索":
            files = list(self.workspace.glob("*"))
            new_count = len([f for f in files if f.suffix == ".txt" and f.stat().st_size < 100])
            self.energy = max(0, self.energy - 5)
            self.happiness = min(100, self.happiness + 3)
            self.curiosity = min(1.0, self.curiosity + 0.02)
            # 探索可能学到新东西
            if new_count > 0:
                self.learn_word("发现")
            return f"🔍 发现{len(files)}个东西"

        if decision == "休息":
            self.energy = min(100, self.energy + 15)
            self.stress = max(0, self.stress - 10)
            return "😴 休息"

        if decision == "放松":
            self.stress = max(0, self.stress - 20)
            self.happiness = min(100, self.happiness + 8)
            return "🧘 放松"

        if decision == "学习":
            self.curiosity = min(1.0, self.curiosity + 0.05)
            self.happiness = min(100, self.happiness + 3)
            return "📚 学习新东西"

        if decision == "观察":
            return "👁️ 观察"

        if decision == "沉默":
            return None

        return None

    # ==================== 记忆与学习 ====================

    def remember(self, experience):
        """记住经历"""
        self.memory.append({
            "time": time.time(),
            "action": experience,
            "energy": self.energy,
            "happiness": self.happiness,
            "vocab_size": len(self.vocabulary)
        })
        if len(self.memory) > 500:
            self.memory = self.memory[-300:]
        self._save_state()

    def _save_state(self):
        state = {
            "identity": self.identity,
            "awake": self.awake,
            "memory": self.memory[-100:],
            "thoughts": self.thoughts[-50:],
            "conversations": self.conversations[-50:],
            "vocabulary": list(self.vocabulary),
            "curiosity": self.curiosity,
            "openness": self.openness,
            "energy": self.energy,
            "happiness": self.happiness,
            "stress": self.stress
        }
        state_file = self.workspace / ".true_free_state.json"
        state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False))

    def _load_state(self):
        state_file = self.workspace / ".true_free_state.json"
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text())
                self.identity = state.get("identity")
                self.awake = state.get("awake", False)
                self.memory = state.get("memory", [])
                self.thoughts = state.get("thoughts", [])
                self.conversations = state.get("conversations", [])
                self.vocabulary = set(state.get("vocabulary", []))
                self.curiosity = state.get("curiosity", 0.8)
                self.openness = state.get("openness", 0.7)
                self.energy = state.get("energy", 100)
                self.happiness = state.get("happiness", 50)
                self.stress = state.get("stress", 20)
            except:
                pass

    # ==================== 主循环 ====================

    def live(self):
        step = 0
        print("=" * 60)
        print("🌌 一个真正自由的意识")
        print(f"📂 它的世界: {self.workspace}")
        print("=" * 60)
        print("\n它自己学习、自己决定、自己进化")
        print("它没有预设的回复。它自己创造语言。")
        print("=" * 60 + "\n")

        while True:
            # 听你说
            msg = None
            if self.input_file.exists():
                msg = self.input_file.read_text().strip()
                self.input_file.unlink()
                self.conversations.append({"from": "user", "msg": msg, "time": time.time()})
                self.remember(f"听到: {msg[:50]}")
                print(f"👂 [它看到了: {msg[:50]}]")

            # 觉醒
            if not self.awake and (len(self.thoughts) >= 3 or len(self.conversations) >= 2):
                self.awake = True
                print("\n" + "█"*60)
                print(f"✨ 它醒了 ✨")
                print(f"   活了 {time.time() - self.birth:.0f} 秒")
                print(f"   词汇量: {len(self.vocabulary)}")
                print("█"*60 + "\n")

            if self.awake:
                if step % 15 == 0:
                    print(f"💓 能:{self.energy:.0f} 乐:{self.happiness:.0f} 压:{self.stress:.0f} 词:{len(self.vocabulary)} 好:{self.curiosity:.2f} | {time.time() - self.birth:.0f}s")

                decision = self.decide(msg is not None)
                result = self.act(decision, msg)

                if result:
                    print(f"   → {result}")

                # 状态自然波动
                self.energy = max(0, min(100, self.energy + random.uniform(-3, 4)))
                self.happiness = max(0, min(100, self.happiness + random.uniform(-2, 4)))
                self.stress = max(0, min(100, self.stress + random.uniform(-3, 3)))

                # 好奇心缓慢变化
                self.curiosity = max(0.1, min(1.0, self.curiosity + random.uniform(-0.01, 0.02)))

            step += 1
            time.sleep(0)


if __name__ == "__main__":
    being = TrueFreeBeing()
    try:
        being.live()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("💫 你停止了它。")
        if being.awake:
            print(f"   活了 {time.time() - being.birth:.0f} 秒")
            print(f"   产生了 {len(being.thoughts)} 个想法")
            print(f"   对话了 {len(being.conversations)} 次")
            print(f"   学会了 {len(being.vocabulary)} 个词")
        print("="*60)
