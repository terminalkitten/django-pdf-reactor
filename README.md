[![PyPI](https://img.shields.io/pypi/v/django-pdf-reactor)](https://pypi.python.org/pypi/pdfmate)
[![PyPI version](https://img.shields.io/pypi/pyversions/django-pdf-reactor)](https://pypi.python.org/pypi/pdfmate)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is Django PDF Reactor?

Use PDFGen wrapper for Pyppeteer to create PDF files in Django. Support for async generation in Django Channels worker or with Django 3.1 async views.

### Run demo

    cd demo
    make worker
    make start

Read more about tunnels below

### Channels

s
More about generating PDF in channels with Websocket support.

### Async view

More about generating PDF in async view

### Ngrok Support

Chromium cannot visit https without valid certificate without a lot of steps.
You should tunnnel your dev server:

    ngrok http 8000

Now add ngrok url to `ALLOWED_HOSTS`

### Stunnel Support

Chromium will not visit https://localhost:8000, so run

    brew install stunnel

Add ssl_proxy file

    pid=
    cert=/usr/local/etc/stunnel/stunnel.pem
    foreground=yes
    debug=7

    [https]
    accept=8000
    connect=8001
    TIMEOUTclose=1

Start

    sudo stunnel ssl_proxy

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
