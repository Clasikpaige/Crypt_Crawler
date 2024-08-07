# Crypt_crawler
![alt text](https://www.dropbox.com/s/9wcqezhdhutty5r/Photo%2024-05-2023%2C%2012%2045%2031%20AM%20%281%29.jpg?raw=1)

 

 # Pollard's Rho Algorithm for ECDLP on secp256k1 Curve

This script uses Pollard's Rho algorithm to solve the Elliptic Curve Discrete Logarithm Problem (ECDLP) on the secp256k1 curve, commonly used in Bitcoin. It can be run in parallel using multiple workers to expedite the process.

## Requirements

Ensure you have the necessary dependencies installed. You can install them using `pip` and the provided `requirements.txt` file.

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-repo/pollards-rho-ecdlp.git
    cd Crypt_crawler.py 
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script

The script requires the following arguments:
- `--wallet_address`: The target Bitcoin wallet address.
- `--max_iter`: (Optional) Maximum iterations for Pollard's Rho algorithm (default: 500000).
- `--num_workers`: (Optional) Number of parallel workers (default: 4).

### Example Command

To run the script, use the following command:

```bash
python Crypt_crawler.py --wallet_address <your_bitcoin_wallet_address> --max_iter 500000 --num_workers 4

Output

The script will output the found private key if the algorithm successfully solves the ECDLP. The process may take significant time depending on the complexity and available computational resources.

Files

	•	Crypt_crawler.py: The main script file containing the Pollard’s Rho algorithm implementation.
	•	requirements.txt: Lists the Python dependencies needed to run the script.
	•	README.md: This file providing instructions on how to use the script.

Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
