import re
from urllib.parse import urlparse

import requests


def ensure_url_has_scheme(url):
    return url if urlparse(url).scheme else f"https://{url}"


def is_valid_url(url):
    url_pattern = re.compile(
        r"^https?://"
        r"(?:www\.)?"
        r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
        r"[a-zA-Z0-9()]{1,6}\b"
        r"(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$"
    )
    return bool(url_pattern.match(url))


def shorten_url(url):
    url = ensure_url_has_scheme(url)

    if not is_valid_url(url):
        return "Error: Not a valid url."

    try:
        response = requests.post(
            "https://s.lain.la",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"url": url},
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Request failed: {e}"
