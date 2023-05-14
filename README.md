Wordlist_Generator
![alt text](https://www.dropbox.com/s/2jgjgzzl4b7m4gg/Photo%2014-05-2023%2C%2012%2001%2056%20PM.jpg?raw=1)

The wordlist_generator program is a Python script that allows you to generate a list of random words and hash them using John the Ripper. You can use this tool for a variety of security testing and password cracking applications.

But that's not all! The program also includes functionality for generating private keys for a specified target hash. This can be really useful for generating private keys for cryptocurrency wallets or other applications that use hashed values for authentication or verification.

When you run the program, you can specify a target hash and the program will generate a wordlist. It then iterates over each word in the list, generates a private key from the word, and checks if the resulting public key matches the target address or wallet. This allows you to verify whether a given seed phrase corresponds to a particular cryptocurrency wallet or other application.
![alt text](https://www.dropbox.com/s/1x2avy6hc9qsned/Photo%2014-05-2023%2C%2011%2045%2049%20AM.jpg?raw=1)

The program uses a number of technologies to accomplish this. It relies on the John the Ripper tool for hashing the wordlist, and uses the cryptography library to generate private keys from the hashed values. It also uses the pybtc library for generating Bitcoin private keys, and the mnemonic library for generating BIP39 seed phrases.

Overall, the wordlist_generator program is a powerful tool that can help you with a variety of security testing and password cracking tasks, as well as generating private keys for cryptocurrency wallets and other applications.
Installation
![alt text](https://www.dropbox.com/s/8t4cem1pmf3vmow/Photo%2014-05-2023%2C%2011%2048%2052%20AM.jpg?raw=1)

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