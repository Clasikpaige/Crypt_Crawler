# Crypt_crawler
![alt text](https://www.dropbox.com/s/9wcqezhdhutty5r/Photo%2024-05-2023%2C%2012%2045%2031%20AM%20%281%29.jpg?raw=1)

 

 # wordlist_generator 
 program is a powerful tool that can help you with a variety of security testing and password cracking tasks, as well as generating private keys for cryptocurrency wallets and other applications.

The program takes several command-line arguments:
`--count`: the number of words to generate in the wordlist (default is 1)
`--output`: the name of the output file (default is "wordlist.csv")
`--hash-type`: the type of hash to use with John the Ripper (default is "md5crypt")
`--target`: the hostname or wallet to target (optional)
`--target-hash`: the hash of the target to generate the private key for (optional)


If the `target` and `target-hash` arguments are not specified, the user will be prompted to enter them. The program generates a wordlist, hashes it using the specified hash type, and then checks each word in the list to see if it generates a private key that matches the target address or wallet. If a matching private key is found, the program will indicate that the private key is valid. Otherwise, it will indicate that no matching password was found for the target hash.





![alt text](https://www.dropbox.com/s/1x2avy6hc9qsned/Photo%2014-05-2023%2C%2011%2045%2049%20AM.jpg?raw=1)



The program uses a number of technologies to accomplish this. It relies on the `John the Ripper` tool for hashing the wordlist, and uses the `cryptography` library to generate private keys from the hashed values. It also uses the `pybtc` library for generating Bitcoin private keys, and the `mnemonic` library for generating BIP39 seed phrases.

# Installation

![alt text](https://www.dropbox.com/s/8t4cem1pmf3vmow/Photo%2014-05-2023%2C%2011%2048%2052%20AM.jpg?raw=1)

To install and utilize the `Crypt_crawler` program, you must have Python 3 and John the Ripper installed on your system.
```
git clone https://github.com/clasikpaige/Crypt_crawler.git
```
After cloning the repository, navigate to the `Crypt_crawler` directory and install the required packages:
bash
```
cd Crypt_crawler
pip install -r requirements.txt
```
# Usage

To use the wordlist_generator tool, simply run the wordlist_generator.py script from the command line:

```
 python Crypt_crawler.py
```
1. Generate a list of 20,000 random words and hash them using the MD5-Crypt algorithm. 

2. Customize the length of the words, the number of words generated, and the hash algorithm used by modifying the variables at the top of the `Crypt_crawler.py` file.

3. Specify a target hostname or wallet address by using the `--target` flag.

```
 python Crypt_crawler.py --target example.com
```
This will generate a wordlist and hash it, using the MD5-Crypt algorithm, with the goal of cracking a password associated with the target hostname example.com. If you want to crack a password associated with a specific wallet address, you can use the --wallet flag:

```
 python Crypt_crawler.py --wallet 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
```
This will generate a wordlist and hash it, using the MD5-Crypt algorithm, with the goal of cracking a password associated with the wallet address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.

# Contributing

If you have any ideas to optimize and improve its performance, feel free to make a pull request!


Note that the Crypt_crawler tool should only be used for ethical purposes, such as security testing and password recovery. Do not use this tool to engage in illegal activities or to harm others.
