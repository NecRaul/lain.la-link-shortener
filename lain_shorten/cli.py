import argparse
import sys

import requests

from .shorten import shorten_url
from .version import __version__


def main():
    parser = argparse.ArgumentParser(
        description="Shorten URLs using lain.la API",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example: %(prog)s https://kuroneko.dev/",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("urls", nargs="+", help="URL(s) to be shortened")

    args = parser.parse_args()

    shortened_urls = []
    has_error = False

    for url_full in args.urls:
        try:
            url = shorten_url(url_full)
            if url.startswith("http"):
                print(f"Shortened URL: {url}\n")
                shortened_urls.append(url)
            else:
                print(
                    f"Error: API returned invalid format for {url_full}",
                    file=sys.stderr,
                )
                has_error = True
        except ValueError as e:
            print(f"Value Error: {e}", file=sys.stderr)
            has_error = True
            continue
        except requests.RequestException as e:
            print(f"Network error: {e}", file=sys.stderr)
            has_error = True
            continue

    if shortened_urls:
        all_urls = "\n".join(shortened_urls)
        try:
            import pyperclip

            pyperclip.copy(all_urls)
            print("\n URL(s) copied to clipboard")
        except Exception:
            pass

    if has_error:
        sys.exit(1)
