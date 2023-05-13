import os
import subprocess
import string
import random
import argparse
import pandas as pd
import hashlib
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_wordlist(length, count, output_file):
    words = []
    for i in range(count):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        words.append(word)
    df = pd.DataFrame(words, columns=['word'])
    df.to_csv(output_file, index=False)
    return df['word']


def hash_wordlist(hash_type, wordlist_file):
    hash_command = f'john --wordlist={wordlist_file} --format={hash_type}'
    subprocess.run(hash_command, shell=True)


def generate_private_key(wordlist, target_hash):
    backend = default_backend()
    salt = os.urandom(16)
    password = None
    for i in range(len(wordlist)):
        if target_hash == hashlib.sha256(wordlist[i].encode()).hexdigest():
            password = wordlist[i].encode()
            break
    if password:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )
        key = kdf.derive(password)
        private_key = binascii.hexlify(key).decode()
        return private_key
    return None


def main():
    parser = argparse.ArgumentParser(description='Generate a wordlist and hash it with John the Ripper.')
    parser.add_argument('--length', type=int, default=8, help='the length of each word in the wordlist')
    parser.add_argument('--count', type=int, default=20000, help='the number of words to generate in the wordlist')
    parser.add_argument('--output', type=str, default='wordlist.csv', help='the name of the output file')
    parser.add_argument('--hash-type', type=str, default='md5crypt', help='the type of hash to use with John the Ripper')
    parser.add_argument('--target', type=str, default=None, help='the hostname or wallet to target')
    parser.add_argument('--target-hash', type=str, default=None, help='the hash of the target to generate the private key for')
    args = parser.parse_args()

    length = args.length
    count = args.count
    output_file = args.output
    hash_type = args.hash_type
    target = args.target
    target_hash = args.target_hash

    if not target:
        target = input("Enter the target hostname or wallet address: ")

    wordlist_file = os.path.join('wordlist', output_file)
    wordlist = generate_wordlist(length, count, wordlist_file)
    hash_wordlist(hash_type, wordlist_file)

    if target and target_hash:
        print(f"Generating private key for target {target}...")
        private_key = generate_private_key(wordlist, target_hash)
        if private_key:
            print(f"Private key generated: {private_key}")
        else:
            print("Unable to generate private key for target.")


if __name__ == '__main__':
    main()
