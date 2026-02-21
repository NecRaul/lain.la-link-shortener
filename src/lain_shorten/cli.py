import argparse
import sys
import webbrowser

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
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="open each generated short URL in your default browser",
    )
    parser.add_argument("urls", nargs="+", help="URL(s) to be shortened")

    args = parser.parse_args()

    shortened_urls = []
    has_error = False

    for url_full in args.urls:
        try:
            url_short = shorten_url(url_full)
            if url_short.startswith("http"):
                print(f"Shortened URL: {url_short}")
                shortened_urls.append(url_short)
            else:
                print(
                    f"Error: API returned invalid format for {url_full}: {url_short}",
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
            print("\nURL(s) copied to clipboard", file=sys.stderr)
        except Exception:
            pass

        if args.open:
            for url_short in shortened_urls:
                webbrowser.open_new_tab(url_short)

    if has_error:
        sys.exit(1)
