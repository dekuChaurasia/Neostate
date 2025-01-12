from flet import Page, View, app, WebRenderer, AppView


def enhanced_app(
    target,
    name="",
    host=None,
    port=0,
    view=AppView.FLET_APP,
    assets_dir="assets",
    upload_dir=None,
    web_renderer=WebRenderer.CANVAS_KIT,
    use_color_emoji=False,
    route_url_strategy="path",
    export_asgi_app=False,
):
    def wrapper(page: Page):
        """
        Wrapper function to enhance the Page object dynamically with additional methods
        for improved navigation and view management.
        """

        # Cache views by their route for better memory management and performance
        
        def swap(route: str, page_builder):
            """
            Navigate to a route by appending to the views stack.
            :param route: Route string for the page.
            :param page_builder: A function that builds and returns the page layout.
            """
            new_view = View(route=route, controls=page_builder(page))
            page.views.append(new_view)
            page.go(route, transition=None)

        def reach(route: str, page_builder):
            """
            Navigate to a route by clearing all existing views and setting a new view.
            :param route: Route string for the page.
            :param page_builder: A function that builds and returns the page layout.
            """
            new_view = View(route=route, controls=page_builder(page))
            page.views.clear()
            page.views.append(new_view)
            page.go(route, transition=None)

        def back(optional=None):
            """
            Navigate to the previous view.
            If an optional route is provided, pop views until the optional route is reached.
            """
            if len(page.views) > 1:
                if optional:
                    while len(page.views) > 1 and page.views[-1].route != optional:
                        page.views.pop()
                else:
                    page.views.pop()
                page.go(page.views[-1].route, transition=None)
            else:
                print("No previous view to go back to.")

        def refresh(page_builder):
            """
            Refresh the current view by rebuilding it.
            :param page_builder: A function that builds and returns the refreshed layout.
            """
            if page.views:
                current_view = page.views[-1]
                refreshed_view = View(route=current_view.route, controls=page_builder(page))
                page.views[-1] = refreshed_view
                page.update()
            else:
                print("No view to refresh.")

        # Attach the enhanced methods to the Page object
        page.swap = swap
        page.reach = reach
        page.back = back
        page.refresh = refresh

        # Pass the enhanced page to the target function
        target(page)

    # Use the wrapper as the app entry point
    app(
        target=wrapper,
        name=name,
        host=host,
        port=port,
        view=view,
        assets_dir=assets_dir,
        upload_dir=upload_dir,
        web_renderer=web_renderer,
        use_color_emoji=use_color_emoji,
        route_url_strategy=route_url_strategy,
        export_asgi_app=export_asgi_app,
    )
