from channels.auth import AuthMiddlewareStack
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from pdf_reactor import consumers
from pdf_reactor.settings import PDF_REACTOR_CONFIG

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                [
                    url(
                        r"^status/(?P<job_id>\w+)/$",
                        consumers.PdfReactorStatusConsumer,
                    ),
                ]
            )
        ),
        "channel": ChannelNameRouter(
            {PDF_REACTOR_CONFIG['CHANNEL_NAME']: consumers.PdfReactorConsumer,}
        ),
    }
)
