from setuptools import setup, find_packages

VERSION = "1.10"
DESCRIPTION = "URL Shortener using s.lain.la API."
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
AUTHOR = "NecRaul"

setup(
    name="lain_shorten",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["requests", "pyperclip"],
    keywords=["python", "link shortener", "shortener", "lain", "lain.la", "s.lain.la"],
    url="https://github.com/NecRaul/lain.la-link-shortener",
    project_urls={
        "Documentation": "https://github.com/NecRaul/lain.la-link-shortener#readme",
        "Source": "https://github.com/NecRaul/lain.la-link-shortener",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
    py_modules=["shorten"],
    entry_points={
        "console_scripts": [
            "lain-shorten = lain_shorten.main:main",
        ],
    },
)
