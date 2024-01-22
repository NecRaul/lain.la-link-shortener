import requests
import re


def url_check(url):
    pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return re.match(pattern, url) is not None


def shorten_url(url):
    # checking if the url is valid
    is_valid_url = url_check(url)

    # adding https:// to the start of the string if url is not valid
    url = f"https://{url}" if not is_valid_url else url

    # checking if the url is valid again
    is_valid_url = url_check(url)

    if not is_valid_url:
        return "Not a valid url."

    data = f"url={url}"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post("https://s.lain.la", headers=headers, data=data)
    return response.text
