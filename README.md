# lain.la-link-shortener

URL Shortener using `s.lain.la` API.

## Installation

### Via PyPI (Recommended)

You have the option to choose between the standard version (lain-shorten) or the desktop version (lain-shorten[clipboard]), which adds clipboard support for auto-copying links.

> [!NOTE]
> For brevity, the examples below use the desktop version.

#### With pip (Basic)

```sh
pip install "lain-shorten[clipboard]"
```

#### With pipx (Isolated)

```sh
pipx install "lain-shorten[clipboard]"
```

#### With uv (Best)

The most efficient way to install or run the shortener.

```sh
# Permanent isolated installation
uv tool install "lain-shorten[clipboard]"

# Run once without installing
uvx --with "lain-shorten[clipboard]" lain-shorten <url1> <url2> <url3>

# Run in scripts or ad-hoc environments
uv run --with "lain-shorten[clipboard]" lain-shorten <url1> <url2> <url3>
```

### From Source (Development)

```sh
# Clone the repository and navigate to it
git clone git@github.com:NecRaul/lain.la-link-shortener.git
cd lain.la-link-shortener

# Install environment and all development dependencies (mandatory and optional)
uv sync --dev

# Install pre-commit hook
uv run pre-commit install

# Optional: Run all linters and type checkers manually
uv run pre-commit run --all-files

# Run the local version
uv run lain-shorten <url1> <url2> <url3>
```

## Usage

Simply provide a URL, and the tool will automatically handle protocol validation and formatting.

```sh
# Shorten a URL
lain-shorten https://kuroneko.dev

# Protocol-less (automatically prepends http://)
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

* Batch Processing: Shorten multiple URLs in a single command execution, saving time over individual manual requests.
* Validation: Uses `urllib` to ensure the URL is formatted correctly.
* API Request: Sends the `POST` request via `requests`.
* Normalization: Automatically adds `http://` if missing.
* Clipboard (Optional): If `pyperclip` is installed, the result is instantly copied to your clipboard.
