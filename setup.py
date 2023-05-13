from setuptools import setup, find_packages

setup(
    name='wordlist-generator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'john>=1.9.0',
    ],
    entry_points={
        'console_scripts': ['wordlist-generator=wordlist_generator:main']
    }
)
