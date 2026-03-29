from setuptools import setup, find_packages

setup(
    name="humncode",
    version="1.0",
    packages=find_packages(),
    py_modules=["main"],
    entry_points={
        'console_scripts': [
            'humncode=main:main',
        ],
    },
)