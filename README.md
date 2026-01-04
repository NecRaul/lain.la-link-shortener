# lain.la-link-shortener

URL Shortener using `s.lain.la` API.

## Installation

### Via PyPI (Recommended)

```sh
# Basic installation
pip install lain-shorten

# With clipboard support (recommended for desktop)
pip install lain-shorten[default]
```

### From Source (Development)

```sh
git clone git@github.com:NecRaul/lain.la-link-shortener.git
cd lain-la-link-shortener
pip install -e .[dev]
```

## Usage

Simply provide a URL. The tool automatically handles protocol validation and formatting.

```sh
# Standard usage
lain-shorten https://kuroneko.dev

# Protocol-less (automatically prepends https://)
lain-shorten kuroneko.dev
```

## Dependencies

* [requests](https://github.com/psf/requests): send the API request for shortening.
  * [urllib3](https://github.com/urllib3/urllib3): check validity of the URL provided.

### Optional

* [pyperclip](https://github.com/asweigart/pyperclip) - copy the shortened URL to the clipboard. (optional)

## How it works

The `s.lain.la` service allows shortening URLs via a `POST` request. This tool automates the process to avoid typing long `curl` strings:

### The Manual Way

```sh
curl -X POST -d 'url=https://kuroneko.dev' https://s.lain.la
```

### The lain-shorten way

* Validation: Uses `urllib3` to ensure the URL is formatted correctly.
* Normalization: Automatically adds `https://` if missing.
* API Request: Sends the `POST` request via `requests`.
* Clipboard (Optional): If `pyperclip` is installed, the result is instantly copied to your clipboard.
