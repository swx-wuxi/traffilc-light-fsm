
# 不要定义在开始，节省运算效率
def get_random_even():
    import random
    ran = random.randint(1,100)
    if ran % 2 != 0:
        ran += 1
    
    return ran

print(f"The random even num is: {get_random_even()}")