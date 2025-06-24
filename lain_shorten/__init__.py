from .shorten import shorten_url
import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser(description="Shorten URLs using lain.la API")
    parser.add_argument("url", help="URL to be shortened")

    args = parser.parse_args()
    response = shorten_url(args.url)

    if response.startswith("http"):
        pyperclip.copy(response)
        print(f"Shortened URL: {response}\nCopied to clipboard.")
    else:
        print(response)


if __name__ == "__main__":
    main()
