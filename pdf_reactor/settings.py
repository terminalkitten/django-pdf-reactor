from functools import lru_cache

from django.conf import settings

if not settings.configured:
    settings.configure()

CONFIG_DEFAULTS = {
    'CHANNEL_NAME': 'pdf-reactor',
    'STATUS_CONSUMER': 'pdf_reactor.consumers.PdfReactorStatusConsumer',
}


@lru_cache()
def get_config():
    USER_CONFIG = getattr(settings, "PDF_REACTOR_CONFIG", {})
    CONFIG = CONFIG_DEFAULTS.copy()
    CONFIG.update(USER_CONFIG)
    return CONFIG


PDF_REACTOR_CONFIG = get_config()
