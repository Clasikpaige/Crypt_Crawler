Wordlist Generator

The wordlist_generator tool is a Python script that generates a list of random words and hashes them using John the Ripper. This tool is useful for generating wordlists that can be used for security testing and password cracking.

Installation

To install and use the wordlist_generator tool, you will need to have Python 3 and John the Ripper installed on your system.

Install Python 3 if you don't have it already. You can download it from the official Python website: https://www.python.org/downloads/
Install John the Ripper. You can download it from the official John the Ripper website: https://www.openwall.com/john/
Once you have installed Python 3 and John the Ripper, you can clone this repository to your local machine:
```
git clone https://github.com/clasikpaige/wordlist_generator.git
After cloning the repository, navigate to the wordlist_generator directory and install the required packages:
```
```
cd wordlist_generator
pip install -r requirements.txt
```
##usage

To use the wordlist_generator tool, simply run the wordlist_generator.py script from the command line:

```
python wordlist_generator.py
```
This will generate a list of 20,000 random words and hash them using the MD5-Crypt algorithm. The generated wordlist will be saved to the wordlist/wordlist.txt file, and the hashes will be saved to the wordlist/wordlist.txt.hash file.

You can customize the length of the words, the number of words generated, and the hash algorithm used by modifying the variables at the top of the wordlist_generator.py file.


# Example usage of wordlist_generator.py
import os

# Generate a list of 10,000 random words and hash them using SHA-256
os.system('python wordlist_generator.py --num_words 10000 --hash_algorithm sha256')
Note that the wordlist_generator tool should only be used for ethical purposes, such as security testing and password recovery. Do not use this tool to engage in illegal activities or to harm others.
