from flet import app, Text, Container, Column,FilledButton,TextSpan,TextStyle, FontWeight, ElevatedButton, MainAxisAlignment, alignment, AppView, WebRenderer, Page, View
try:
 from flet import Colors
except:
    from flet import colors as Colors
# Custom Page Class

# Global Route Registry and Configurations
class RoutingConfig:
    ROUTES = {}
    MIDDLEWARES = []
    GLOBAL_ERROR_PAGES = {
        "404": lambda page: [
           Container(   
            Column([
                Text('Page Not Found',weight=FontWeight.BOLD,opacity=.4,size=24),
                
                Text(
         spans=[
                TextSpan( '4 0 4',
                            TextStyle(color=Colors.BLACK54))
               
                
                ],size=150,weight=FontWeight.BOLD
           ,opacity=.8
          
        ),FilledButton("Go Home",on_click=lambda e:page.go('/'))
                       
                       ],horizontal_alignment='center',alignment=MainAxisAlignment.CENTER)
            ,alignment=alignment.center,expand=1
      
      )
    
        ],
        "not_allowed": lambda page: [ Container(   
            Column([
                Text('You Are Not Allowed',weight=FontWeight.BOLD,opacity=.4,size=24),
                
                Text(
         spans=[
                TextSpan( '4',
                            TextStyle(color=Colors.BLACK54))
                ,TextSpan( '❌',
                             TextStyle(size=140)
                             )
                ,TextSpan( '5',
                              TextStyle(color=Colors.BLACK54))
                
                ],size=150,weight=FontWeight.BOLD
           ,opacity=.8
          
        ),FilledButton("Go Home",on_click=lambda e:page.go('/'))
                       
                       ],horizontal_alignment='center',alignment=MainAxisAlignment.CENTER)
            ,alignment=alignment.center,expand=1
      
      )],
    }
    DEFAULT_REDIRECT = "/"
    ACTIVE_VIEWS = set()  # To track active routes and avoid duplicate views

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



# Optimized Routing Functions
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
def enhanced_app(target, name="",advanced_routing=False, host=None, port=0, view=AppView.FLET_APP, assets_dir="assets", upload_dir=None,
                 web_renderer=WebRenderer.CANVAS_KIT, use_color_emoji=False, route_url_strategy="path", export_asgi_app=False):
    def big_wrapper(page: Page):

      
          
        # Attach enhanced routing methods to the page object
       

        def swap(route: str, page_builder):
                
                """
                Navigate to a route by appending to the views stack.
                :param route: Route string for the page.
                :param page_builder: A function that builds and returns the page layout.
                """
                if not advanced_routing:
           
                    new_view = View(route=route, controls=page_builder(page))
                    page.views.append(new_view)
                    page.go(route, transition=None)
                else:
                     raise ValueError(
                        "⚠️ Error: You have chosen Advanced routing, but the function 'swap()' belongs to Basic routing. "
                        "🔧 To use this function, call the app with 'advanced_routing=False' "
                        "or Not pass Advanced routing Arguemnt at all. 🛠️"
                    )    

        def reach(route: str, page_builder):
                """
                Navigate to a route by clearing all existing views and setting a new view.
                :param route: Route string for the page.
                :param page_builder: A function that builds and returns the page layout.
                """
                if not advanced_routing:
                    new_view = View(route=route, controls=page_builder(page))
                    page.views.clear()
                    page.views.append(new_view)
                    page.go(route, transition=None)
                else:
                     raise ValueError(
                        "⚠️ Error: You have chosen Advanced routing, but the function 'reach()' belongs to Basic routing. "
                        "🔧 To use this function, call the app with 'advanced_routing=False' "
                        "or Not pass Advanced routing Arguemnt at all. 🛠️"
                    )     
    
        def back(optional=None):
                """
                Navigate to the previous view.
                If an optional route is provided, pop views until the optional route is reached.
                """
                if not advanced_routing:
                  if len(page.views) > 1:
                      if optional:
                          while len(page.views) > 1 and page.views[-1].route != optional:
                              page.views.pop()
                      else:
                          page.views.pop()
                      page.go(page.views[-1].route, transition=None)
                  else:
                      print("No previous view to go back to.")
                else:
                     raise ValueError(
                        "⚠️ Error: You have chosen Advanced routing, but the function 'back()' belongs to Basic routing. "
                        "🔧 To use this function, call the app with 'advanced_routing=False' "
                        "or Not pass Advanced routing Arguemnt at all. 🛠️"
                    )       
      
        def refresh(page_builder):
                """
                Refresh the current view by rebuilding it.
                :param page_builder: A function that builds and returns the refreshed layout.
                """
                if not advanced_routing:
                  if page.views:
                      current_view = page.views[-1]
                      refreshed_view = View(route=current_view.route, controls=page_builder(page))
                      page.views[-1] = refreshed_view
                      page.update()
                  else:
                      print("No view to refresh.")
                else:
                     raise ValueError(
                        "⚠️ Error: You have chosen Advanced routing, but the function 'refresh()' belongs to Basic routing. "
                        "🔧 To use this function, call the app with 'advanced_routing=False' "
                        "or Not pass Advanced routing Arguemnt at all. 🛠️"
                    )       
    
            # Attach the enhanced methods to the Page object
        
        page.swap = swap
        page.reach = reach
        page.back = back
        page.refresh = refresh
        if advanced_routing: 
         page.register_route = RoutingConfig.register_route
         page.register_middleware = RoutingConfig.register_middleware
         page.set_global_error_page = RoutingConfig.set_global_error_page
         page.set_default_redirect = RoutingConfig.set_default_redirect    
         enhanced_router(page)
        else:
           
            def set_global_error_page( error_type, page_builder):
                    raise ValueError(
                f"⚠️ Error: You have chosen Advanced routing, but the following functions "
                " set_global_error_page belong to Advanced routing. "
                "🔧 To use these functions, call the app with 'advanced_routing=True'  🛠️"
            )
        
            
            def set_default_redirect( route):
                 raise ValueError(
                f"⚠️ Error: You have chosen Advanced routing, but the following functions "
                " set_default_redirect belong to Advanced routing. "
                "🔧 To use these functions, call the app with 'advanced_routing=True'  🛠️"
            )
            
            def register_route( route: str, page_builder, guard=None, custom_redirect=None, custom_not_allowed_page=None):
                 raise ValueError(
                f"⚠️ Error: You have chosen Advanced routing, but the following functions "
                " register_route belong to Advanced routing. "
                "🔧 To use these functions, call the app with 'advanced_routing=True'  🛠️"
            )
        
            
            def register_middleware( middleware):
                raise ValueError(
                f"⚠️ Error: You have chosen Advanced routing, but the following functions "
                " register_middleware belong to Advanced routing. "
                "🔧 To use these functions, call the app with 'advanced_routing=True'  🛠️"
            )
            
            def apply_middlewares( page, route):
                raise ValueError(
                f"⚠️ Error: You have chosen Advanced routing, but the following functions "
                " apply_middlewares belong to Advanced routing. "
                "🔧 To use these functions, call the app with 'advanced_routing=True'  🛠️"
            )
            page.register_route = register_route
            page.register_middleware = register_middleware
            page.set_global_error_page = set_global_error_page
            page.set_default_redirect = set_default_redirect         
        target(page)
           
          
 
      

    app(target=big_wrapper, name=name, host=host, port=port, view=view, assets_dir=assets_dir, upload_dir=upload_dir,
           web_renderer=web_renderer, use_color_emoji=use_color_emoji, route_url_strategy=route_url_strategy, export_asgi_app=export_asgi_app)



