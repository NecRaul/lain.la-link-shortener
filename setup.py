from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "URL Shortener using lain.la API."
LONG_DESCRIPTION = "s.lain.la can shorten URLs using CUrl. I tend to forget the CUrl syntax and arguments quite easily so I made a Python package to streamline things."
AUTHOR = "NecRaul"

setup(
    name="lainla_shorten",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["requests", "setuptools"],
    keywords=["python", "link shortener", "shortener", "lain", "lain.la", "s.lain.la"],
    classifiers=[
        "Development Status :: Ongoing",
        "Intended Audience :: Everybody",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    py_modules=["shorten"],
    entry_points={
        "console_scripts": [
            "lainla = lainla_shorten.__init__:main",
        ],
    },
)