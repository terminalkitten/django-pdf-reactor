# -*- coding: utf-8 -*-

__version__ = '0.1.3'
__license__ = 'MIT'

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import nanoid
from nanoid.resources import alphabet
from pdf_reactor.settings import PDF_REACTOR_CONFIG

channel_layer = get_channel_layer()

default_app_config = 'pdf_reactor.apps.PdfReactorConfig'


class PdfReactor:
    def from_url(self, url, output=None, options={}):

        job_id = nanoid.generate(alphabet=alphabet[2:])

        if not output:
            output = f'files/{job_id}.pdf'

        async_to_sync(channel_layer.send)(
            PDF_REACTOR_CONFIG['CHANNEL_NAME'],
            {
                'type': 'from_url',
                'job_id': job_id,
                'url': url,
                'output': output,
                'options': options,
            },
        )

        return job_id
