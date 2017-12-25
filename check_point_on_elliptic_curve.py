***
Bitcoin uses a specifc elliptic curve and set of mathematical constants, as defined in a standard called secp256k1

y^2 = (x^3 + 7) over (Fvp)
or
y^2 mod p = (x^3 + 7) mod p

***
import sys

p = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]

res = ( x ** 3 + 7 - y ** 2) % p
print res
