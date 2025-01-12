from flet import Page,View
class Page(Page):
    
    def swap(self, route: str, page_builder):
        """
        Navigate to a route by appending to the views.
        :param route: Route string for the page.
        :param page_builder: A function that builds and returns the page layout.
        """
        new_view = View(route=route, controls=page_builder(self))
        self.views.append(new_view)
        self.go(route, transition=None)

    def reach(self, route: str, page_builder):
        """
        Navigate to a route by clearing existing views and setting the new view.
        :param route: Route string for the page.
        :param page_builder: A function that builds and returns the page layout.
        """
        new_view = View(route=route, controls=page_builder(self))
        self.views.clear()
        self.views.append(new_view)
        self.go(route, transition=None)

    def back(self,optional=None):
        """Navigate to the previous view."""
        if len(self.views) > 1:
            self.views.pop()
            self.go(self.views[-1].route, transition=None)
        else:
            print("No previous view to go back to.")

    def refresh(self, page_builder):
        """Refresh the current view."""
        if self.views:
            current_view = self.views[-1]
            refreshed_view = View(route=current_view.route, controls=page_builder(self))
            self.views[-1] = refreshed_view
            self.update()
        else:
            print("No view to refresh.")
    def set_global_error_page(cls, error_type, page_builder):
        cls.GLOBAL_ERROR_PAGES[error_type] = page_builder

    
    def set_default_redirect(cls, route):
        cls.DEFAULT_REDIRECT = route

    
    def register_route(cls, route: str, page_builder, guard=None, custom_redirect=None, custom_not_allowed_page=None):
        cls.ROUTES[route] = {
            "page_builder": page_builder,
            "guard": guard,
            "custom_redirect": custom_redirect,
            "custom_not_allowed_page": custom_not_allowed_page,
        }

    
    def register_middleware(cls, middleware):
        cls.MIDDLEWARES.append(middleware)

    
    def apply_middlewares(cls, page, route):
        for middleware in cls.MIDDLEWARES:
            if not middleware(page, route):
                return False
        return True        
