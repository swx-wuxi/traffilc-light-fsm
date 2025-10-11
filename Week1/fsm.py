from enum import Enum
import time
class Digit(Enum):
    ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = range(10)

# 七段数码管跳转程序
SEGMENTS = {
    Digit.ZERO:  "abcdef",
    Digit.ONE:   "bc",
    Digit.TWO:   "abdeg",
    Digit.THREE: "abcdg",
    Digit.FOUR:  "bcfg",
    Digit.FIVE:  "acdfg",
    Digit.SIX:   "acdefg",
    Digit.SEVEN: "abc",
    Digit.EIGHT: "abcdefg",
    Digit.NINE:  "abcdfg",
}

def next_digit(state):
    
    return Digit((state.value + 1) % 10)

def reset():
    return Digit.ZERO

# Example run
state = reset()
for _ in range(12):
    print(f"State: {state}, Segments: {SEGMENTS[state]}")
    time.sleep(1)
    state = next_digit(state)
