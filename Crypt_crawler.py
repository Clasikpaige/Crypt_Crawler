import hashlib
import random
import concurrent.futures
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
import argparse
import requests
import json

class ECurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def modinv(self, a, p):
        if a == 0:
            raise ValueError('Inverse does not exist')
        lm, hm = 1, 0
        low, high = a % p, p
        while low > 1:
            ratio = high // low
            nm, new = hm - lm * ratio, high - low * ratio
            lm, low, hm, high = nm, new, lm, low
        return lm % p

    def add(self, P, Q):
        if P == (None, None):
            return Q
        if Q == (None, None):
            return P
        if P == Q:
            l = (3 * P[0] * P[0] + self.a) * self.modinv(2 * P[1], self.p) % self.p
        else:
            l = (Q[1] - P[1]) * self.modinv(Q[0] - P[0], self.p) % self.p
        x = (l * l - P[0] - Q[0]) % self.p
        y = (l * (P[0] - x) - P[1]) % self.p
        return (x, y)

    def multiply(self, k, P):
        R = (None, None)
        while k:
            if k & 1:
                R = self.add(R, P)
            P = self.add(P, P)
            k >>= 1
        return R

def pollards_rho(curve, base_point, target_point, max_iter=500000):
    def f(X, a, b):
        if X[0] % 3 == 0:
            return curve.add(X, base_point), (a + 1) % curve.p, b
        elif X[0] % 3 == 1:
            return curve.add(X, X), (a * 2) % curve.p, (b * 2) % curve.p
        else:
            return curve.add(X, target_point), a, (b + 1) % curve.p

    x, alpha, beta = base_point, 1, 0
    X, A, B = x, alpha, beta
    for _ in range(max_iter):
        x, alpha, beta = f(x, alpha, beta)
        X, A, B = f(*f(X, A, B))
        if x == X:
            r = (beta - B) % curve.p
            if r == 0:
                return None
            return (A - alpha) * curve.modinv(r, curve.p) % curve.p
    return None

def parallel_pollards_rho(curve, base_point, target_point, max_iter, num_workers):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for _ in range(num_workers):
            futures.append(executor.submit(pollards_rho, curve, base_point, target_point, max_iter))
        results = [future.result() for future in futures]
    return results

def get_address_info(wallet_address):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error fetching address info: {response.status_code}, {response.text}")

def convert_wallet_to_point(wallet_address):
    address_info = get_address_info(wallet_address)
    pubkey = address_info.get('public')
    if not pubkey:
        raise ValueError("Public key not found for the given wallet address.")
    x, y = pubkey_to_point_conversion(pubkey)
    return (x, y)

def pubkey_to_point_conversion(pubkey):
    if len(pubkey) == 66:  # Uncompressed key
        prefix = pubkey[:2]
        if prefix == '04':
            x = int(pubkey[2:66], 16)
            y = int(pubkey[66:], 16)
            return x, y
    raise ValueError("Invalid public key format")

def main():
    parser = argparse.ArgumentParser(description="Pollard's Rho algorithm for ECDLP on secp256k1 curve.")
    parser.add_argument('--wallet_address', type=str, required=True, help='Target Bitcoin wallet address')
    parser.add_argument('--max_iter', type=int, default=500000, help='Maximum iterations for Pollard\'s Rho algorithm')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of parallel workers')
    args = parser.parse_args()

    # secp256k1 curve parameters
    a = 0
    b = 7
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    base_point = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
                  0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)

    target_point = convert_wallet_to_point(args.wallet_address)

    curve = ECurve(a, b, p)
    results = parallel_pollards_rho(curve, base_point, target_point, args.max_iter, args.num_workers)

    for i, res in enumerate(results):
        print(f"Worker {i+1} result: {res}")

if __name__ == "__main__":
    main()