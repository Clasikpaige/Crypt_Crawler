from setuptools import setup, find_packages

setup(
    name='Crypt_crawler',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pywallet',
        'cryptography',
        'mnemonic',
        'pybtc',
        'pandas',
    ],
    entry_points={
        'console_scripts': ['crypt-crawler=crypt_crawler:main']
    }
)
