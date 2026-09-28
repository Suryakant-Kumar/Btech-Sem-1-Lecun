import sys 
print(0.1+0.2)
print(0.1+0.2==0.3)
print(bin(5))
print(bin(-5))
print(sys.float_info.dig)     
print(sys.float_info.max)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")
print(f"{0.1+0.2:.20f}")


print(0.1 + 0.2 == 0.3) # direct ==
print(round(0.1 + 0.2, 1) == 0.3) # round first
import math
print(math.isclose(0.1 + 0.2, 0.3)) # tolerance-based
print(3 << 1 + 1)
print((3 << 1) + 1)
print(12 & 10 == 8)
print(12 & (10 == 8))
print(not 2 > 1 and 5 | 2 == 7)