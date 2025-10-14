
"""
fault_harness.py
Simulate several fault scenarios and show how they propagate through a tiny 'processing' function.
This is a host-side test harness — it logs injected values and how the processing handles them.
"""

import random
import logging
from typing import Any, Callable, List

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("FaultHarness")

def process_sensor_reading(x: Any) -> float:
    """
    Example processing pipeline that expects an integer ADC reading 0..1023.
    Returns normalized float 0.0 .. 1.0 or raises ValueError on bad input.
    """
    if x is None:
        raise ValueError("Missing reading")
    if not isinstance(x, int):
        raise TypeError(f"Unexpected type: {type(x)}")
    if x < 0 or x > 4096:  # accept a wider raw range to show spike handling
        raise ValueError("Out-of-range sensor reading")
    
    return float(x) / 1023.0

# Fault scenario generators （假的，只是模拟罢了，故意让x出错）
def overflow_scenario(x: int) -> int:
    return x + (1 << 16)

def missing_data_scenario(x: int) -> int:
    return None

def sign_flip_scenario(x: int) -> int:
    return x * -1

def adc_spike_scenario(x: int) -> int:
    # occasional huge spike
    if random.random() < 0.05:
        return x + random.randint(1000, 5000)
    return x


SCENARIOS = [
    ("normal", lambda x: x),
    ("overflow", overflow_scenario),
    ("missing", missing_data_scenario),
    ("sign_flip", sign_flip_scenario),
    ("adc_spike", adc_spike_scenario),
]

def run_harness(trials):
    results = []
    for i in range(trials):
        base = random.randint(0, 1023)   # 随机选择一个数字
        scenario_name, scenario_fn = random.choice(SCENARIOS) # 随机选择场景
        injected = scenario_fn(base)   # injected是一个数字 
        # 如果抛出异常，就执行下一个分支
        try:
            out = process_sensor_reading(injected)
            logger.info("Trial %d: scenario=%s injected=%s -> normalized=%.3f",
                        i, scenario_name, injected, out)
            results.append((scenario_name, injected, "OK", out))
        except Exception as e:
            logger.warning("Trial %d: scenario=%s injected=%s -> ERROR: %s",
                           i, scenario_name, injected, e)
            results.append((scenario_name, injected, "ERROR", str(e)))
    return results


if __name__ == "__main__":
    import json
    import pathlib
    res = run_harness(10)
    Path = pathlib.Path
    Path("Week2/output_files/fault_results.json").write_text(json.dumps(res, indent=2))
    print("Wrote fault_results.json")

