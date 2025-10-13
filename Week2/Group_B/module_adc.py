# import numpy as np
# import matplotlib.pyplot as plt

# # def adc_quantise(signal: np.ndarray, bits, vref) -> np.ndarray:
# #     if bits <=0 :
# #         raise 
# #     levels = 2**bits
# #     step = vref / (levels - 1)
# #     return np.round(signal / step) * step

# # Example usage
# # 量化到离散的电平 AD转换（现实中信号非连续，转换成连续的信号）
# t = np.linspace(0, 1, 1000)
# vin = 1.65 + 1.65 * np.sin(2 * np.pi * 5 * t)

# # 需要给三个参数：输入，量化个数，参考电压
# vout = adc_quantise(vin,2,3.3)

# plt.plot(t, vin, label="Analog")
# plt.step(t, vout, label="Quantised", where="mid")
# plt.legend()
# plt.show()

import logging, math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("adc")

# Define types of error! 
class ADCError(Exception): 
    pass

class OutOfRange(ADCError): 
    pass

class InvalidInput(ADCError): 
    pass


class ADC:
    def __init__(self, bits, vref):
        self.bits = bits
        self.vref = vref
        self.max_code = 2**bits - 1

    def convert(self, voltage: float) -> int:
        if not isinstance(voltage, (int, float)):
            raise InvalidInput(f"{voltage} Not a number")
        if math.isnan(voltage) or math.isinf(voltage):
            raise InvalidInput("Invalid float")
        if self.bits <= 0:   
            raise ValueError(f"bits {self.bits} is invalid!!")
        if voltage < 0 or voltage > self.vref:
            raise OutOfRange(f"Voltage {voltage}V out of range 0-{self.vref}")

        # clipping: 
        # if voltage < 0:
        #     logger.warning(f"Warning! Voltage will clip to 0 V")
        #     voltage = 0

        # if voltage > self.vref:
        #     logger.warning(f"Warning! Voltage will clip to {self.vref} V")
        #     voltage = self.vref

        code = int(round((voltage / self.vref) * self.max_code))
        logger.info("Converted %.3fV -> code %d", voltage, code)
        return code

# adc = ADC(bits=8,vref=5.0)
# print(adc.convert(2.5))
# print(adc.convert(3.453525))
# print(adc.convert(5.4))

