from setuptools import setup, find_packages

setup(
    name = 'booklover',
    version = '1.0.0',
    url = 'https://github.com/atchiado/ds5100_m09_homework',
    author = 'Anthony Chiado',
    author_email = 'anthonychiado97@gmail.com',
    description = 'This package is for booklovers',
    license = 'MIT',
    packages = find_packages(),
    install_requires = ['pandas >= 2.0.3']
)