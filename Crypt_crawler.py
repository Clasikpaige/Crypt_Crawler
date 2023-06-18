iimport os
import subprocess
import argparse
import pandas as pd
import binascii
from pywallet import wallet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from mnemonic import Mnemonic
from bitcoinlib.keys import BitcoinPrivateKey

def generate_wordlist(count, output_file):
    mnemonic = Mnemonic("english")
    words = mnemonic.generate(strength=128)
    df = pd.DataFrame([words.split()], columns=['word'])
    df.to_csv(output_file, index=False)
    return words

def hash_wordlist(hash_type, wordlist_file):
    hash_command = f'john --wordlist={wordlist_file} --format={hash_type}'
    subprocess.run(hash_command, shell=True)

def generate_private_key(word, target_address):
    backend = default_backend()
    salt = os.urandom(16)
    password = word.encode()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    seed = Mnemonic.to_seed(password)
    key = kdf.derive(seed)
    private_key = binascii.hexlify(key).decode()
    
    if validate_private_key(private_key, target_address):
        return private_key
    else:
        return None

def validate_private_key(private_key, target_address):
    key = BitcoinPrivateKey(private_key)
    address = key.public_key().address()
    return address == target_address

def recover_recovery_phrase(wordlist, target_address):
    for word in wordlist:
        seed = wallet.mnemonic_to_seed(word)
        recovered_wallet = wallet.create_wallet(network="BTC", seed=seed, children=1)
        recovered_address = recovered_wallet['address']
        
        if target_address == recovered_address:
            return word
    
    return None

def main():
    parser = argparse.ArgumentParser(description='Generate a wordlist and hash it with John the Ripper.')
    parser.add_argument('--count', type=int, default=1, help='the number of words to generate in the wordlist')
    parser.add_argument('--output', type=str, default='wordlist.csv', help='the name of the output file')
    parser.add_argument('--hash-type', type=str, default='md5crypt', help='the type of hash to use with John the Ripper')
    parser.add_argument('--target', type=str, default=None, help='the hostname or wallet to target')
    args = parser.parse_args()

    count = args.count
    output_file = args.output
    hash_type = args.hash_type
    target = args.target

    if not target:
        target = input("Enter the target hostname or wallet address: ")

    wordlist_file = os.path.join('wordlist', output_file)
    wordlist = generate_wordlist(count, wordlist_file)
    hash_wordlist(hash_type, wordlist_file)

    private_key = None
    if wordlist and target:
        for word in wordlist:
            private_key = generate_private_key(word, target)
            if private_key:
                break

    if private_key:
        print(f"Private key generated: {private_key}")
        is_valid = validate_private_key(private_key, target)
        if is_valid:
            print("Private key is valid!")
        else:
            print("Generated private key is invalid.")
    else:
        print("No matching password found.")

    recovery_word = recover_recovery_phrase(wordlist, target)

    if recovery_word:
        print(f"Recovered recovery phrase: {recovery_word}")
    else:
        print("Recovery phrase not found.")

if __name__ == '__main__':
    main()
