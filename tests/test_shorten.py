import time
import unittest
from urllib.parse import urlparse

import requests

from lain_shorten.shorten import shorten_url


class ShortenIntegrationTests(unittest.TestCase):
    BASE_HOST_SUFFIX = "lain.la"

    def _assert_short_url(self, url, verify_redirect=True):
        self.assertTrue(url)
        self.assertTrue(url.startswith("http"))

        parsed = urlparse(url)
        self.assertTrue(parsed.hostname)
        self.assertTrue(parsed.hostname.endswith(self.BASE_HOST_SUFFIX))

        if not verify_redirect:
            return

        last_error = None
        for _ in range(5):
            try:
                r = requests.get(url, timeout=10, allow_redirects=False)
                self.assertIn(r.status_code, (301, 302, 303, 307, 308))
                return
            except requests.RequestException as e:
                last_error = e
                time.sleep(1)

        self.fail(f"Short URL not reachable: {last_error}")

    def test_shorten_http_url(self):
        url = shorten_url("https://example.com")
        self._assert_short_url(url)

    def test_shorten_https_url(self):
        url = shorten_url("https://kuroneko.dev")
        self._assert_short_url(url)

    def test_shorten_irc_url(self):
        url = shorten_url("irc://irc.example.com/#test")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_ircs_url(self):
        url = shorten_url("ircs://irc.example.com/#test")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_ssh_url(self):
        url = shorten_url("ssh://user@example.com")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_mailto(self):
        url = shorten_url("mailto:test@example.com")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_xmpp(self):
        url = shorten_url("xmpp:test@example.com")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_sms(self):
        url = shorten_url("sms:+15551234567")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_tel(self):
        url = shorten_url("tel:+15551234567")
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_magnet(self):
        magnet = "magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567&dn=test"
        url = shorten_url(magnet)
        self._assert_short_url(url, verify_redirect=False)

    def test_shorten_without_scheme(self):
        url = shorten_url("example.com")
        self._assert_short_url(url)

    def test_invalid_url_fails(self):
        with self.assertRaises(ValueError):
            shorten_url("ftp://example.com")


if __name__ == "__main__":
    unittest.main()
