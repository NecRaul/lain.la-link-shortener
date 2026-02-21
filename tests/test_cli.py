import io
import unittest
from unittest.mock import MagicMock, patch

from lain_shorten import cli


class CliTests(unittest.TestCase):
    def test_shortens_url_and_prints_to_stdout(self):
        self.mock_shortened = "http://short.url/abc123"
        fake_pyperclip = MagicMock()

        with (
            patch("lain_shorten.cli.shorten_url", return_value=self.mock_shortened),
            patch("sys.argv", ["lain-shorten", "https://example.com"]),
            patch("sys.stdout", new_callable=io.StringIO) as stdout,
            patch("sys.stderr", new_callable=io.StringIO) as stderr,
            patch.dict("sys.modules", {"pyperclip": fake_pyperclip}),
        ):
            cli.main()

            self.assertIn(self.mock_shortened, stdout.getvalue())
            self.assertIn("URL(s) copied to clipboard", stderr.getvalue())

    # def test_shortens_url_and_prints_to_stdout(self):
    #     self.mock_shortened = "http://short.url/abc123"
    #
    #     with (
    #         patch("lain_shorten.cli.shorten_url", return_value=self.mock_shortened),
    #         patch("sys.argv", ["lain-shorten", "https://example.com"]),
    #         patch("sys.stdout", new_callable=io.StringIO) as stdout,
    #         patch("sys.stderr", new_callable=io.StringIO) as stderr,
    #     ):
    #         cli.main()
    #
    #         self.assertIn(self.mock_shortened, stdout.getvalue())
    #         self.assertIn("URL(s) copied to clipboard", stderr.getvalue())

    def test_opens_browser_when_flag_is_used(self):
        shortened_url = "http://short.url/abc123"

        fake_webbrowser = MagicMock()
        with (
            patch("lain_shorten.cli.shorten_url", return_value=shortened_url),
            patch("lain_shorten.cli.webbrowser", fake_webbrowser),
            patch("sys.argv", ["lain-shorten", "-o", "https://example.com"]),
            patch("sys.stdout", new_callable=io.StringIO),
            patch("sys.stderr", new_callable=io.StringIO),
        ):
            cli.main()

            fake_webbrowser.open_new_tab.assert_called_once_with(shortened_url)

    def test_invalid_url_prints_error_and_exits(self):
        invalid_response = "not-a-url"

        with (
            patch("lain_shorten.cli.shorten_url", return_value=invalid_response),
            patch("sys.argv", ["lain-shorten", "https://badexample.com"]),
            patch("sys.stdout", new_callable=io.StringIO),
            patch("sys.stderr", new_callable=io.StringIO) as stderr,
            self.assertRaises(SystemExit) as ctx,
        ):
            cli.main()

            self.assertEqual(ctx.exception.code, 1)
            self.assertIn("Error: API returned invalid format", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
