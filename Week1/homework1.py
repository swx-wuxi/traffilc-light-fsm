
import time

def test(): 
    s = 0
    for i in range(10**7):
        s = s + i

start = time.time()
test()
print("Time:",time.time()-start)

