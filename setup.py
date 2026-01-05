from setuptools import find_packages, setup

VERSION = "1.15"
DESCRIPTION = "URL Shortener using s.lain.la API."
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
AUTHOR = "NecRaul"
AUTHOR_EMAIL = "necraul@kuroneko.dev"

setup(
    name="lain_shorten",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    keywords=[
        "python",
        "link shortener",
        "shortener",
        "lain",
        "lain.la",
        "s.lain.la",
        "kuroneko",
    ],
    url="https://github.com/NecRaul/lain.la-link-shortener",
    project_urls={
        "Documentation": "https://github.com/NecRaul/lain.la-link-shortener#readme",
        "Source": "https://github.com/NecRaul/lain.la-link-shortener",
        "Issues": "https://github.com/NecRaul/lain.la-link-shortener/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
    py_modules=["shorten"],
    entry_points={
        "console_scripts": [
            "lain-shorten = lain_shorten:main",
        ],
    },
)
