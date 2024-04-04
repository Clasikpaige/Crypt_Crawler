import hashlib
import binascii
from pywallet import wallet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from mnemonic import Mnemonic
from bitcoinlib.keys import BitcoinPrivateKey
import argparse

def generate_wordlist(count):
    if count <= 0:
        return []

    mnemo = Mnemonic("english")
    wordlist = []
    for _ in range(count):
        word = mnemo.generate()
        wordlist.append(word)

    return wordlist

def hash_wordlist(wordlist, hash_type):
    hashed_wordlist = [hashlib.new(hash_type, word.encode()).hexdigest() for word in wordlist]
    return hashed_wordlist

def generate_private_key(word, target_address):
    backend = default_backend()
    salt = os.urandom(16)
    password = word.encode()
    
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    seed = Mnemonic.to_seed(password)
    key = kdf.derive(seed)
    private_key = binascii.hexlify(key).decode()
    
    try:
        if validate_private_key(private_key, target_address):
            return private_key
    except Exception as e:
        print(f"Error during private key validation: {e}")
    return None

def validate_private_key(private_key, target_address):
    try:
        key = BitcoinPrivateKey(private_key)
        address = key.public_key().address()
        return address == target_address
    except Exception as e:
        print(f"Error during private key validation: {e}")
        return False

def recover_recovery_phrase(wordlist, target_address):
    for word in wordlist:
        try:
            seed = wallet.mnemonic_to_seed(word)
            recovered_wallet = wallet.create_wallet(network="BTC", seed=seed, children=1)
            recovered_address = recovered_wallet['address']
        
            if target_address == recovered_address:
                return word
        except Exception as e:
            print(f"Error during recovery phrase recovery: {e}")

    return None

def main():
    parser = argparse.ArgumentParser(description='Generate a wordlist and hash it with John the Ripper.')
    parser.add_argument('--count', type=int, default=1, help='the number of words to generate in the wordlist')
    parser.add_argument('--hash-type', type=str, default='sha256', help='the type of hash to use')
    parser.add_argument('--target', type=str, default=None, help='the hostname or wallet to target')
    args = parser.parse_args()

    count = args.count
    hash_type = args.hash_type
    target = args.target

    if not target:
        target = input("Enter the target hostname or wallet address: ")

    wordlist = generate_wordlist(count)
    if not wordlist:
        return

    hashed_wordlist = hash_wordlist(wordlist, hash_type)

    private_key = None
    if wordlist and target:
        for hashed_word in hashed_wordlist:
            private_key = generate_private_key(hashed_word, target)
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
