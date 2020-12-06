import pdfmate
import asyncio

from io import BytesIO

from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import classonlymethod

pdfmate.configuration(options={'debug': False}, pyppeteer={'emulateMedia': 'print'})


class PdfReactorAsyncView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self, request):

        path = await pdfmate.from_url(
            request.build_absolute_uri(), None, options={'printBackground': True}
        )

        # get filestream async generated file
        file_stream = BytesIO(path)

        # generate downloadable file
        response = HttpResponse(file_stream.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=demo.pdf'
        return response

