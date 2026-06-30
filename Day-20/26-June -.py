'''
import sys 
print(sys.argv) ## LIST OF COMMENTS
print(sys.path) ## RETURN PATH OF MODULES
print(sys.version) ## Return PYTHON VERSION

print("Before exit")
sys.exit() ## COMEOUT OF FILE
print("After exit")
'''

import platform 

print(platform.system())
print(platform.release())
print(platform.processor())

import math

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.pow(2,5))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print(math.degrees(90))
print(math.radians(90))

print(math.ceil(23.00001)) ## 24 - CEIL - UPPER NUMBER
print(math.ceil(23.4))
print(math.ceil(23.88))
print(math.ceil(23.99999))

print(math.floor(23.00001))  ## 23 - FLOOR - LOWER NUMBER
print(math.floor(23.4))
print(math.floor(23.88))
print(math.floor(23.99999))
