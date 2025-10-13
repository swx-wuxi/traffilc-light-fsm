import pytest
from module_adc import ADC, OutOfRange

def test_known_values():
    adc = ADC(bits=12, vref=3.3)
    assert adc.convert(0.0) == 0
    assert adc.convert(3.3) == 4095
    assert adc.convert(1.65) == pytest.approx(2048, abs=1)

def test_out_of_range_low():
    adc = ADC(bits=12, vref=3.3)
    with pytest.raises(OutOfRange):
        adc.convert(-0.3)

def test_out_of_range_high():
    adc = ADC(bits=12, vref=3.3)
    with pytest.raises(OutOfRange):
        adc.convert(3.5)
