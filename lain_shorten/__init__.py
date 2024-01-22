from .shorten import shorten_url
import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser(description="Shorten URLs using lain.la API")
    parser.add_argument("url", help="URL to be shortened")

    args = parser.parse_args()
    shortened_url = shorten_url(args.url)

    if shortened_url != "Not a valid url.":
        pyperclip.copy(shortened_url)
        print(f"Shortened URL: {shortened_url}\nCopied to clipboard.")
    else:
        print(shortened_url)


if __name__ == "__main__":
    main()
