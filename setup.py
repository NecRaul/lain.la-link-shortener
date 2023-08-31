from setuptools import setup, find_packages

VERSION = "1.2"
DESCRIPTION = "URL Shortener using s.lain.la API."
LONG_DESCRIPTION = "s.lain.la can shorten URLs using curl. I tend to forget the curl syntax and arguments quite easily so I made a Python package to streamline things."
AUTHOR = "NecRaul"

setup(
    name="lain_shorten",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["requests", "pyperclip"],
    keywords=["python", "link shortener", "shortener", "lain", "lain.la", "s.lain.la"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP"
    ],
    py_modules=["shorten"],
    entry_points={
        "console_scripts": [
            "lain-shorten = lain_shorten.__init__:main",
        ],
    },
)