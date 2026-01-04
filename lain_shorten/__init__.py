import argparse

from .shorten import shorten_url

try:
    import pyperclip

    CLIP_OK = pyperclip.is_available()
except Exception:
    CLIP_OK = False


def main():
    parser = argparse.ArgumentParser(description="Shorten URLs using lain.la API")
    parser.add_argument("url", help="URL to be shortened")

    args = parser.parse_args()
    response = shorten_url(args.url)

    if response.startswith("http"):
        print(f"Shortened URL: {response}")
        if CLIP_OK:
            pyperclip.copy(response)
            print("Copied to clipboard.")
    else:
        print(response)


if __name__ == "__main__":
    main()
