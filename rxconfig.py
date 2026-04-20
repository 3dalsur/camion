import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="camion_app",
    disable_plugins=[SitemapPlugin],
)