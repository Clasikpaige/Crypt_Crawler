import hashlib
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
import argparse
import random

# Define the elliptic curve parameters and the base point
a = -0x3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

P = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 
     0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)

Q = (0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe, 
     0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562)

# Elliptic Curve class for mathematical operations
class ECurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    
    def mod(self, x):
        return x % self.p

    def invmod(self, x):
        s0, s1 = 0, 1
        r0, r1 = self.p, x
        while r0 != 0:
            q = r1 // r0
            r1, r0 = r0, r1 - q * r0
            s1, s0 = s0, s1 - q * s0
        return s1 % self.p

    def add(self, p, q):
        if p == (0, 0): return q
        if q == (0, 0): return p
        
        if p == q:
            if p[1] != 0:
                l = self.mod(self.mod(3 * p[0] * p[0] + self.a) * self.invmod(2 * p[1]))
                x = self.mod(l * l - 2 * p[0])
                y = self.mod(l * (p[0] - x) - p[1])
                return (x, y)
        else:
            if q[0] != p[0]:
                l = self.mod(self.mod(q[1] - p[1]) * self.invmod(q[0] - p[0]))
                x = self.mod(l * l - p[0] - q[0])
                y = self.mod(l * (p[0] - x) - p[1])
                return (x, y)
        return (0, 0)

    def double(self, p):
        return self.add(p, p)

    def multiply(self, p, n):
        if n == 0:
            return (0, 0)
        elif n == 1:
            return p
        elif n % 2 == 1:
            return self.add(p, self.multiply(p, n - 1))
        else:
            return self.multiply(self.double(p), n // 2)

# Pollard's Rho Algorithm for ECDLP
def pollards_rho(curve, base_point, target_point, max_iter=100000):
    x1, x2, x3 = random.randint(1, p - 1), random.randint(1, p - 1), random.randint(1, p - 1)
    A1, A2, A3 = base_point, base_point, base_point
    for _ in range(max_iter):
        if A1 == target_point:
            return x1
        if A2 == target_point:
            return x2
        if A3 == target_point:
            return x3
        
        # Update A1, A2, A3 and their corresponding x values
        x1 = (x1 + 1) % p
        A1 = curve.add(A1, base_point)
        if x1 % 3 == 0:
            x1 = (x1 + 1) % p
            A1 = curve.add(A1, base_point)
        
        x2 = (x2 + 2) % p
        A2 = curve.double(A2)
        if x2 % 3 == 0:
            x2 = (x2 + 1) % p
            A2 = curve.add(A2, base_point)

        x3 = (x3 + 1) % p
        A3 = curve.add(A3, base_point)
        if x3 % 3 == 0:
            x3 = (x3 + 1) % p
            A3 = curve.add(A3, base_point)
        
        if A1 == A2:
            k = (x1 - x2) % p
            if k == 0:
                continue
            k = curve.invmod(k)
            d = (x2 - x1) % p
            if d == 0:
                continue
            return (d * k) % p

    return None

def main():
    # Define elliptic curve
    curve = ECurve(a, b, p)

    # Compute ECDLP
    result = pollards_rho(curve, P, Q)
    if result is not None:
        print(f"Found private key: {result}")
    else:
        print("Private key not found")

if __name__ == "__main__":
    main()
    