from flet import app,Text,Container,Column,FontWeight,ElevatedButton,MainAxisAlignment,alignment,AppView,WebRenderer,Page,View
# Custom Page Class

# Global Route Registry and Configurations
class RoutingConfig:
    ROUTES = {}
    MIDDLEWARES = []
    GLOBAL_ERROR_PAGES = {
        "404": lambda page: [
            Container(
                content=Column(
                    [
                        Text("Oops!", size=50, weight=FontWeight.BOLD, color="red"),
                        Text("404 - Page not found", size=30),
                        Container(
                            content=ElevatedButton("Go Home", on_click=lambda e: page.go("/")),
                            margin=20,
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                width=500,
                height=400,
                alignment=alignment.center,
                padding=20,
                border_radius=20,
                bgcolor="lightblue",
            )
        ],
        "not_allowed": lambda page: [Text("401 - Not authorized")],
    }
    DEFAULT_REDIRECT = "/"

    @classmethod
    def set_global_error_page(cls, error_type, page_builder):
        cls.GLOBAL_ERROR_PAGES[error_type] = page_builder

    @classmethod
    def set_default_redirect(cls, route):
        cls.DEFAULT_REDIRECT = route

    @classmethod
    def register_route(cls, route: str, page_builder, guard=None, custom_redirect=None, custom_not_allowed_page=None):
        cls.ROUTES[route] = {
            "page_builder": page_builder,
            "guard": guard,
            "custom_redirect": custom_redirect,
            "custom_not_allowed_page": custom_not_allowed_page,
        }

    @classmethod
    def register_middleware(cls, middleware):
        cls.MIDDLEWARES.append(middleware)

    @classmethod
    def apply_middlewares(cls, page, route):
        for middleware in cls.MIDDLEWARES:
            if not middleware(page, route):
                return False
        return True

# Enhanced Routing Functions
def enhanced_router(page: Page):
    def route_change_handler(route_event):
        route = route_event.route

        # Apply middlewares (optional)
        if not RoutingConfig.apply_middlewares(page, route):
            new_view = View(
                route="/not_allowed",
                controls=RoutingConfig.GLOBAL_ERROR_PAGES["not_allowed"](page)
            )
            page.views.append(new_view)
            page.update()
            return

        # Handle unknown routes (404)
        route_config = RoutingConfig.ROUTES.get(route)
        if not route_config:
            error_page_builder = RoutingConfig.GLOBAL_ERROR_PAGES["404"]
            new_view = View(
                route="/404",
                controls=error_page_builder(page)
            )
            # Add the 404 page view if it's not already the last one
            if len(page.views) == 0 or page.views[-1].route != "/404":
                page.views.append(new_view)
            page.update()
            return

        # Check for guard conditions
        guard = route_config.get("guard")
        custom_redirect = route_config.get("custom_redirect")
        custom_not_allowed_page = route_config.get("custom_not_allowed_page")
        if guard:
            guard_result = guard() if callable(guard) else guard
            if not guard_result:
                if custom_redirect:
                    page.go(custom_redirect)
                    return

                if custom_not_allowed_page:
                    new_view = View(
                        route="/custom_not_allowed",
                        controls=custom_not_allowed_page(page)
                    )
                    # Add the custom "not allowed" page view if it's not already the last one
                    if len(page.views) == 0 or page.views[-1].route != "/custom_not_allowed":
                        page.views.append(new_view)
                    page.update()
                    return

                new_view = View(
                    route="/not_allowed",
                    controls=RoutingConfig.GLOBAL_ERROR_PAGES["not_allowed"](page)
                )
                # Add the "not allowed" page view if it's not already the last one
                if len(page.views) == 0 or page.views[-1].route != "/not_allowed":
                    page.views.append(new_view)
                page.update()
                return

        # Build and add the new view
        page_builder = route_config["page_builder"]
        new_view = View(route=route, controls=page_builder(page))

        # Avoid appending duplicate views
        if len(page.views) == 0 or page.views[-1].route != route:
            page.views.append(new_view)

        page.update()

    def on_pop_handler(e):
        # Handle back navigation
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)
        else:
            print("No views to go back to. Exiting or staying on current view.")
        page.update()

    # Attach handlers to the page
    page.on_route_change = route_change_handler
    page.on_pop = on_pop_handler

    # Initialize the router with the current URL
    page.go(page.route)

# Main Application Function
def enhanced_app(target, name="", host=None, port=0, view=AppView.FLET_APP, assets_dir="assets", upload_dir=None,
                 web_renderer=WebRenderer.CANVAS_KIT, use_color_emoji=False, route_url_strategy="path", export_asgi_app=False):
    def wrapper(page: Page):
        # Attach enhanced routing methods to the page object
        page.register_route = RoutingConfig.register_route
        page.register_middleware = RoutingConfig.register_middleware
        page.set_global_error_page = RoutingConfig.set_global_error_page
        page.set_default_redirect = RoutingConfig.set_default_redirect
        
        enhanced_router(page)
        target(page)

    app(target=wrapper, name=name, host=host, port=port, view=view, assets_dir=assets_dir, upload_dir=upload_dir,
           web_renderer=web_renderer, use_color_emoji=use_color_emoji, route_url_strategy=route_url_strategy, export_asgi_app=export_asgi_app)
