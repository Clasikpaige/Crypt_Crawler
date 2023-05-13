import os
import subprocess
import string
import random
import argparse


def generate_wordlist(length, count, output_file):
    words = []
    for i in range(count):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        words.append(word)
    with open(output_file, 'w') as f:
        f.write('\n'.join(words))
    return words


def hash_wordlist(hash_type, wordlist_file):
    hash_command = f'john --wordlist={wordlist_file} --format={hash_type}'
    subprocess.run(hash_command, shell=True)


def main():
    parser = argparse.ArgumentParser(description='Generate a wordlist and hash it with John the Ripper.')
    parser.add_argument('--length', type=int, default=8, help='the length of each word in the wordlist')
    parser.add_argument('--count', type=int, default=20000, help='the number of words to generate in the wordlist')
    parser.add_argument('--output', type=str, default='wordlist.txt', help='the name of the output file')
    parser.add_argument('--hash-type', type=str, default='md5crypt', help='the type of hash to use with John the Ripper')
    parser.add_argument('--target', type=str, default=None, help='the hostname or wallet to target')
    args = parser.parse_args()

    length = args.length
    count = args.count
    output_file = args.output
    hash_type = args.hash_type
    target = args.target

    wordlist_file = os.path.join('wordlist', output_file)
    generate_wordlist(length, count, wordlist_file)
    hash_wordlist(hash_type, wordlist_file)

    if target:
        print(f"Generating private key for target {target}...")
        # Add code here to generate a private key for the target


if __name__ == '__main__':
    main()
