
##  🚀 Advanced Routing  🚀


When you set `advanced_routing=True`, routing is handled in a more dynamic way. You manage routes, permissions, and custom error handling using the methods provided by the `page` object.

#### **1. Register Routes with `page.register_route()`** 📝

You can register routes in the `page` object and specify which function (page builder) should handle each route. 

- **Example**:
  
```python
page.register_route("/home", home_page)
page.register_route("/login", login_page)
```
 register_route has optional 
 ```
 guard=None, custom_redirect=None, custom_not_allowed_page=None 
```
```
function :can be passed on guard which returns true or false

custom_redirect: eg ='/' only used when page not found or
user not authenticated it redirects to that page

custom_not_allowed_page: here function can be passed which return ui
just like homepage or abourpage

```
#### **2. Route Guards** 🚨

You can add **guards** to routes. A guard is a function that checks whether a user has permission to access a route. If the guard returns `False`, the route will not be accessed.

- **Example**:

```python
def check_user_logged_in():
    return user_is_logged_in()  # Returns True/False based on the user's login status

page.register_route("/dashboard", dashboard_page, guard=check_user_logged_in)
```

If the user is not logged in, the guard will redirect them to another page.

#### **3. Middleware** 🔧

**Middleware** functions run before a route change occurs. They are typically used for things like authentication or logging.

- **Example**:

```python
def auth_check(page, route):
    if not user_is_authenticated():
        page.go("/login")  # Redirect to login if not authenticated
        return False  # Prevent route change
    return True

page.register_middleware(auth_check)
```

This middleware ensures that only authenticated users can access certain routes.

#### **4. Error Pages** ⚠️

You can define custom **error pages** for situations like "Page Not Found" (404) or "Not Allowed".

- **Example**:

```python
def not_found_page(page):
    return [
        Text("404 - Page Not Found", size=30, weight=FontWeight.BOLD),
        FilledButton("Go Home", on_click=lambda e: page.go("/"))
    ]

def not_allowed_page(page):
    return [
        Text("You are not allowed to access this page", size=20),
        FilledButton("Go Home", on_click=lambda e: page.go("/"))
    ]

page.set_global_error_page("404", not_found_page)
page.set_global_error_page("not_allowed", not_allowed_page)
```

When a route is not found or access is denied, these custom error pages will be shown.

