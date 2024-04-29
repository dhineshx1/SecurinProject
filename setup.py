from setuptools import setup, find_packages

setup(
    name='Securin_Project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pymongo',
        'schedule',
        'flask',
    ],
)

