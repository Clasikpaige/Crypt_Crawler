Wordlist Generator

The wordlist_generator program is a Python script designed to generate a list of randomized words and then hash them using John the Ripper. This program can be useful for generating wordlists that can be utilized for security testing and password cracking.

In addition to generating wordlists, the program includes built-in functionality for generating private keys for a specified target hash. This can be particularly useful for generating private keys for cryptocurrency wallets or other applications that utilize hashed values for authentication or verification.

To use this functionality, simply specify a target hash when running the program. The program will then generate a wordlist, iterate over each word, and generate a private key from the word that matches the target hash.

Installation

To install and utilize the wordlist_generator program, you must have Python 3 and John the Ripper installed on your system.
```
git clone https://github.com/clasikpaige/wordlist_generator.git
```
After cloning the repository, navigate to the wordlist_generator directory and install the required packages:
bash
```
cd wordlist_generator
pip install -r requirements.txt
```
Usage

To use the wordlist_generator tool, simply run the wordlist_generator.py script from the command line:

```
 python wordlist_generator.py
```
This will generate a list of 20,000 random words and hash them using the MD5-Crypt algorithm. The generated wordlist will be saved to the wordlist/wordlist.txt file, and the hashes will be saved to the wordlist/wordlist.txt.hash file.

You can customize the length of the words, the number of words generated, and the hash algorithm used by modifying the variables at the top of the wordlist_generator.py file.
You can also specify a target hostname or wallet address by using the --target flag:

```
 python wordlist_generator.py --target example.com
```
This will generate a wordlist and hash it, using the MD5-Crypt algorithm, with the goal of cracking a password associated with the target hostname example.com. If you want to crack a password associated with a specific wallet address, you can use the --wallet flag:

```
 python wordlist_generator.py --wallet 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
```
This will generate a wordlist and hash it, using the MD5-Crypt algorithm, with the goal of cracking a password associated with the wallet address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.

Note that the wordlist_generator tool should only be used for ethical purposes, such as security testing and password recovery. Do not use this tool to engage in illegal activities or to harm others.