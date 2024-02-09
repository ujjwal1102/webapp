"""
ASGI config for webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
import chatbot.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

application = ProtocolTypeRouter({

    'https':get_asgi_application(),
    'websocket': URLRouter(chatbot.routing.websocket_urlpatterns)

})

# django.setup()
# application = get_default_application()