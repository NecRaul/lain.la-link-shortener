from urllib.parse import urlparse

import requests


def ensure_url_has_scheme(url):
    if not url.startswith(("http://", "https://")):
        return f"http://{url}"
    return url


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except ValueError:
        return False


def shorten_url(url):
    url = url.strip()
    url = ensure_url_has_scheme(url)

    if not is_valid_url(url):
        raise ValueError(f"'{url}' is not a valid web URL.")

    response = requests.post(
        "https://s.lain.la",
        data={"url": url},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=10,
    )
    response.raise_for_status()
    result = response.text.strip()
    if not result:
        raise ValueError("Server returned an empty response.")

    return result
