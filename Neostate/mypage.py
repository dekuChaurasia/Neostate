from flet import Page,View

# Custom Page Class
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