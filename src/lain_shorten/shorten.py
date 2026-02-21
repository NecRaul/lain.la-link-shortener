from urllib.parse import parse_qs, urlparse

import requests

NETWORK_URL_SCHEMES = {
    "http",
    "https",
    "irc",
    "ircs",
    "ssh",
}

HANDLE_SCHEMES = {
    "mailto",
    "xmpp",
}

PHONE_SCHEMES = {
    "sms",
    "tel",
}


def ensure_url_has_scheme(url):
    if urlparse(url).scheme:
        return url

    if not url.startswith(("//",)):
        return f"http://{url}"
    return url


def is_valid_url(url):
    try:
        result = urlparse(url)
        scheme = result.scheme

        if scheme in NETWORK_URL_SCHEMES:
            return bool(result.netloc)

        if scheme in HANDLE_SCHEMES:
            return bool(result.path and "@" in result.path)

        if scheme in PHONE_SCHEMES:
            return bool(result.path)

        if scheme == "magnet":
            query = parse_qs(result.query)
            return bool(query.get("xt"))

        return False
    except ValueError:
        return False


def shorten_url(url):
    url = url.strip()
    url = ensure_url_has_scheme(url)

    if not is_valid_url(url):
        raise ValueError(f"'{url}' is not a valid supported URL.")

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
