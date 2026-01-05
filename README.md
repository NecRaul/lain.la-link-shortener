# lain.la-link-shortener

URL Shortener using `s.lain.la` API.

## Installation

### Via PyPI (Recommended)

```sh
# Basic installation
pip install lain-shorten

# With clipboard support (recommended for desktop)
pip install lain-shorten[clipboard]
```

### From Source (Development)

```sh
git clone git@github.com:NecRaul/lain.la-link-shortener.git
cd lain.la-link-shortener
# You can skip the next two commands
# for installing it globally
python -m venv .venv
source .venv/bin/activate
pip install -e .[clipboard,dev,build]
```

## Usage

Simply provide a URL, and the tool will automatically handle protocol validation and formatting.

```sh
# Shorten a URL
lain-shorten https://kuroneko.dev

# Protocol-less (automatically prepends https://)
lain-shorten kuroneko.dev
```

## Dependencies

* [requests](https://github.com/psf/requests): send the API request for shortening.

### Optional

* [pyperclip](https://github.com/asweigart/pyperclip): copy the shortened URL to the clipboard.

## How it works

The `s.lain.la` service allows shortening URLs via a `POST` request.

This tool automates the process to avoid typing long `curl` strings.

### The Manual Way

```sh
curl -d "url=https://kuroneko.dev" https://s.lain.la
```

### The lain-shorten way

* Validation: Uses `urllib` to ensure the URL is formatted correctly.
* API Request: Sends the `POST` request via `requests`.
* Normalization: Automatically adds `https://` if missing.
* Clipboard (Optional): If `pyperclip` is installed, the result is instantly copied to your clipboard.
