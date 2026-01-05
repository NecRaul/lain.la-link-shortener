import argparse

from .shorten import shorten_url


def main():
    parser = argparse.ArgumentParser(description="Shorten URLs using lain.la API")
    parser.add_argument("url", help="URL to be shortened")

    args = parser.parse_args()
    response = shorten_url(args.url)

    if response.startswith("http"):
        print(f"Shortened URL: {response}")

        try:
            import pyperclip

            pyperclip.copy(response)
            print("Copied to clipboard.")
        except Exception:
            pass
    else:
        print(response)


if __name__ == "__main__":
    main()
