import os
from django.core.asgi import get_asgi_application

# Ensure settings are loaded before any Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mysite.settings')

# Initialize Django application before importing channels modules
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from Mysite import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Using a separate variable ensures Django is fully loaded
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
