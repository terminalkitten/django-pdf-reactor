[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is Django PDF Reactor?

Combines PDFGen wrapper for Pyppeteer with Django Channels Worker backend.
It supports multiple

### Support for PDF/A

For MacOSX:

     brew install poppler ghostscript

For Ubuntu / Debian:

     apt-get install poppler ghostscript

A PDF/A document is just a PDF document that uses a specific subset of PDF that is designed to ensure it is 'self-contained'. It's not permitted to be reliant on information from external sources (e.g. font programs and hyperlinks).

From wikipedia:

Other key elements to PDF/A compatibility include:

- Audio and video content are forbidden.
- JavaScript and executable file launches are forbidden.
- All fonts must be embedded and also must be legally embeddable for
  unlimited, universal rendering. This also applies to the so-called  
  PostScript standard fonts such as Times or Helvetica.
- Colorspaces specified in a device-independent manner.
- Encryption is disallowed.
- Use of standards-based metadata is mandated.

### Is it any good?

[Yes.](http://news.ycombinator.com/item?id=3067434)

#### Credits

- [PDFGen-Python](https://pypi.org/project/pdfgen/)
- [Pyppeteer](https://pypi.org/project/pyppeteer/)

