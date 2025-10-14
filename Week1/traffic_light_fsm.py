from enum import Enum, auto
import time
import argparse

class State(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    BLINKING_YELLOW = auto()

class TrafficLightFSM:
    """一个简单的交通灯有限状态机：RED → GREEN → YELLOW → RED"""

    def __init__(self, initial: State = State.RED):
        self.state = initial

    def next_state(self) -> State:
        """状态推进一次，不打印；返回推进后的状态。"""
        if self.state == State.RED:
            self.state = State.GREEN
        elif self.state == State.GREEN:
            self.state = State.YELLOW
        elif self.state == State.YELLOW:
            self.state = State.RED
        else:
            raise ValueError(f"Invalid state: {self.state}")
        return self.state
    
    def enter_blinking_mode(self):
        """强制进入闪烁黄灯模式"""
        self.state = State.BLINKING_YELLOW
        print("Entering BLINKING_YELLOW mode...")

    def cycle(self, steps: int = 1, delay: float | None = None, include_start: bool = True) -> None:
        """
        循环推进并打印当前状态。
        - steps: 推进次数
        - delay: 每次推进后的停顿秒数；None 或 0 表示不等待
        - include_start: 是否先打印初始状态
        """
        if include_start:
            print(self.state.name)
        for _ in range(steps):
            if self.state == State.BLINKING_YELLOW:
                print("BLINKING_YELLOW")
                time.sleep(1)
                continue
            self.next_state()
            print(self.state.name)
            if delay and delay > 0:
                time.sleep(delay)


def main():
    parser = argparse.ArgumentParser(description="Traffic Light FSM: RED → GREEN → YELLOW → RED")
    parser.add_argument("-n", "--steps", type=int, default=6, help="推进（切换）次数")
    parser.add_argument("--delay", type=float, default=0.0, help="每步之间的等待秒数")
    parser.add_argument("--no-start", action="store_true", help="不要打印初始状态")
    args = parser.parse_args()

    fsm = TrafficLightFSM()
    fsm.enter_blinking_mode()
    fsm.cycle(steps=args.steps, delay=args.delay, include_start=(not args.no_start))


if __name__ == "__main__":
    main()
