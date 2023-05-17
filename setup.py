from setuptools import setup, find_packages

setup(
    name='Crypt_crawler',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pywallet==0.3.1',
        'cryptography==3.4.8',
        'mnemonic==0.20',
        'pybtc==0.3.4',
        'pandas==1.3.0',
    ],
    entry_points={
        'console_scripts': ['crypt-crawler=crypt_crawler:main']
    }
)
