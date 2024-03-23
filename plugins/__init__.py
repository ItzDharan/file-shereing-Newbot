from aiohttp import web
from .route import routes


async def create_web_app():
    """
    Create and configure the aiohttp web application.
    """
    # Create a new web application instance with a maximum client size of 30MB
    web_app = web.Application(client_max_size=30000000)

    # Add routes to the web application
    web_app.add_routes(routes)

    return web_app
