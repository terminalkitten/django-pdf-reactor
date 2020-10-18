import json
import os
import logging

import pdfgen
from io import BytesIO
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


logger = logging.getLogger('pdf_reactor')


pdfgen.configuration(pyppeteer={'emulateMedia': 'print'})


def split_filepath(path):
    path_list = path.split(os.sep)
    filename = path_list.pop()
    return (filename, '/'.join(path_list))


class PdfReactorStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.job_id = self.scope['url_route']['kwargs']['job_id']
        await self.channel_layer.group_add(self.job_id, self.channel_name)
        await self.accept()

    async def send_status(self, params):
        await self.send(bytes_data=params['blob'],)


class PdfReactorConsumer(AsyncConsumer):
    async def from_url(self, params):
        job_id = params['job_id']
        url = params['url']
        output = params['output']
        options = params['options']

        logger.info(f'[pdf-reactor] Started job - {job_id}')

        path = await pdfgen.from_url(url, None, options=options)
        # filename, path = split_filepath(path)

        file_stream = BytesIO(path)

        await self.channel_layer.group_send(
            job_id, {"type": "send_status", "blob": file_stream.getvalue(),},
        )

        logger.info(f'[pdf-reactor] Finished job - {job_id}')

