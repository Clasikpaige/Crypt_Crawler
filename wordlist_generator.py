import os
import subprocess
import string
import random


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
    length = 8
    count = 20000
    output_file = 'wordlist.txt'
    hash_type = 'md5crypt'
    wordlist_file = os.path.join('wordlist', output_file)
    generate_wordlist(length, count, wordlist_file)
    hash_wordlist(hash_type, wordlist_file)


if __name__ == '__main__':
    main()
