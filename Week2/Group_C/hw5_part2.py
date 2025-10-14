

def saturating_add_signed(a,b,bits) -> int: 
   max_val = 2**(bits-1) - 1
   min_val = -2**(bits-1) - 1
   res = a+b
   if res > max_val:
       res = max_val
   
   if res < min_val :
       res = min_val

   return res

def wrapping_add_signed(a, b, bits) -> int :
    mask = 2**bits - 1 # 低bits位全部是1
    res = (a+b) & mask
    sign_bit = 1 << (bits-1)

    # 如果高位是1，在计算机中这个就是复数（有符号）
    if res & sign_bit: 
       return res - (2**bits)
    
    return res

if __name__ == '__main__': 
    print("Saturating 16-bit process: ->",
          saturating_add_signed(10000,30000,16))
    print("Wrapping_add_sign:",wrapping_add_signed(10000,30000,16))

