from random import randint

import pdfgen
from io import BytesIO
import asyncio

from django.utils.decorators import classonlymethod

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pdf_reactor import PdfReactor

import nanoid
from nanoid.resources import alphabet

reactor = PdfReactor()

from wsgiref.util import FileWrapper


class PdfAsyncView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self, request):

        job_id = nanoid.generate(alphabet=alphabet[2:])
        output = f'files/{job_id}.pdf'

        path = await pdfgen.from_url(
            request.build_absolute_uri(), None, options={'printBackground': True}
        )

        file_stream = BytesIO(path)

        # generate the file
        response = HttpResponse(file_stream.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={job_id}.pdf'
        return response

    # return JsonResponse({'job_id': job_id, 'path': path})

    async def get(self, request):
        return render(request, 'pdf/index_async.html')


class PdfWebsocketView(View):
    def post(self, request):
        job_id = reactor.from_url(
            request.build_absolute_uri(), options={'printBackground': True},
        )
        return JsonResponse({'job_id': job_id})

    def get(self, request):
        return render(request, 'pdf/index.html')
