# lain.la-link-shortener

URL Shortener using s.lain.la API.

## Requirements

`requests` is used for CUrl command.

`pyperclip` is used to copy link to the clipboard.

If you want to build this on your own, you can install the requirements with

```Python
pip install -r requirements.txt
```

or install the package by running

```Python
pip install lain-shorten
```

Python's native `re` (used to check validity of the url), `argparse` (parse return request and set command argument) and `setuptools` (used to build the script) packages are also used.

## How it works

`s.lain.la` can shorten URLs using CUrl. I tend to forget the CUrl syntax and arguments quite easily so I made a Python package to streamline things. Below is the aforementioned CUrl command.

```CUrl
curl -X POST -d 'url=https://yoururlhere.com' https://s.lain.la
```

I just wrapped it inside Python and added validation to check for links and copied the return address to clipboard for ease of use.

You can run the script with

```Python
lain-shorten <your-url-here>
```

I added support for links not starting with http/https as well.
