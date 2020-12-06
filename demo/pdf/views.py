from pdf_reactor.views import PdfReactorAsyncView
from pdf_reactor import PdfReactor

from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render

reactor = PdfReactor()


class PdfAsyncView(PdfReactorAsyncView):
    async def get(self, request):
        return render(request, 'pdf/index_async.html')


class PdfWebsocketView(View):
    def post(self, request):
        job_id = reactor.from_url(
            request.build_absolute_uri(), options={'printBackground': True},
        )
        return JsonResponse({'job_id': job_id})

    def get(self, request):
        return render(request, 'pdf/index_socket.html')
