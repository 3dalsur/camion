import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="camion_app",
    backend_host="0.0.0.0",
    backend_port=10000,
    disable_plugins=[SitemapPlugin],
)