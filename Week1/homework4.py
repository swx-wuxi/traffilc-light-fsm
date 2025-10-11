import dis

def add(a,b): 
    return 2 * a + 3 * b

def print_name(name): 
    return f"Name: Tony + {name}"

def my_loop(n):
    total = 0
    for i in range (n): 
        total+=i
    return total

dis.dis(add)
dis.dis(print_name)
dis.dis(my_loop)