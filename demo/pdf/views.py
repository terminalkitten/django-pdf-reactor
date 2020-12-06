import pdfmate
import asyncio

from io import BytesIO

from django.utils.decorators import classonlymethod

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pdf_reactor import PdfReactor

reactor = PdfReactor()


class PdfAsyncView(View):
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
