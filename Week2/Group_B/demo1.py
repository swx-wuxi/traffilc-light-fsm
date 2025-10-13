import logging

# 创建 logger 对象并设定格式
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

# 文件输出
file_handler = logging.FileHandler("logging_1.txt", mode="w")
file_handler.setFormatter(formatter)

# 控制台输出
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 添加两个 handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class ADCError(Exception):
    pass

def convert_voltage(v: float) -> int:
    if v < 0 or v > 3.3:
        raise ADCError(f"Voltage {v}V out of range")
    return int((v / 3.3) * 4095)

try:
    code = convert_voltage(5.0)
except ADCError as e:
    logger.error("Conversion failed: %s", e)
