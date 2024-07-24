import hashlib
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
import argparse

def generate_mnemonic():
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=256)  # Generate a 24-word mnemonic

def mnemonic_to_private_key(mnemonic_phrase):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_phrase)
    hd_key = HDKey.from_seed(seed)
    return hd_key.wif()

def validate_private_key(private_key, target_address):
    try:
        key = HDKey.from_wif(private_key)
        address = key.address()
        return address == target_address
    except Exception as e:
        print(f"Error during private key validation: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Generate a mnemonic phrase and validate it against a target address.')
    parser.add_argument('--target', type=str, required=True, help='The target wallet address to validate against')
    args = parser.parse_args()

    target_address = args.target

    # Generate a mnemonic phrase
    mnemonic_phrase = generate_mnemonic()
    print(f"Generated mnemonic phrase: {mnemonic_phrase}")

    # Convert mnemonic phrase to private key
    private_key = mnemonic_to_private_key(mnemonic_phrase)
    print(f"Derived private key: {private_key}")

    # Validate the private key against the target address
    if validate_private_key(private_key, target_address):
        print("The derived private key is valid for the target address!")
    else:
        print("The derived private key does not match the target address.")

if __name__ == '__main__':
    main()