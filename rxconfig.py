import reflex as rx

config = rx.Config(
    app_name="camion_app",

    # ?? CLAVE PARA RENDER
    backend_host="0.0.0.0",
    backend_port=10000,

    # Evita auto-plugins innecesarios
    disable_plugins=[
        "reflex.plugins.sitemap.SitemapPlugin"
    ]
)