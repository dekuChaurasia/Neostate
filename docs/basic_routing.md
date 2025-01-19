# Easy and Basic Routing with Neostate 🚀

Welcome to **NeoRoute**! A simple and effective routing system for building Flet applications with easy navigation between pages. This guide will explain how to use routing features like `swap()`, `refresh()`, and `back()`, with simple examples to help you get started.

## Features ✨

- **Easy Routing**: Link pages with minimal code.
- **Navigation Functions**: Use functions like `swap()`, `refresh()`, and `back()` to control page behavior.
- **Global AppBar**: Automatically apply a global AppBar for all pages.
- **Reach**: Define routes easily and associate them with specific page functions.

## How to Use 🚦

### 1. Basic Setup

First, you'll need to import the required libraries and define the **main** function where the app logic will reside. Here’s how to set things up:

```python
import flet as ft
from Neostate import app, Page

def main(page: Page):
    # Center align all content
    page.horizontal_alignment = 'center'

    # Set global behavior for the "Back" button
    page.on_view_pop = page.back

    # Define the initial page route
    page.reach("/home", home_page)

# Run the app
app(target=main)
```

In the above example:
- The `page.on_view_pop = page.back` sets a default action for when the user navigates back from a page.
- `page.reach("/home", home_page)` defines a route `/home` and links it to the `home_page` function.

### 2. Defining Pages and Navigation

Now, let’s define the pages and see how to navigate between them.

#### Home Page 🏠

```python
def home_page(page: Page):
    return [ft.Text("Welcome to the Home Page!"),
    ft.Button("Go to Next Page", on_click=lambda e: page.swap())]
```

In this example:
- The `home_page` adds a **Text** widget and a **Button**.
- When the button is clicked, it triggers the `page.swap()` function, which swaps the current page with a new one.


#### Full Navigation Example 🔄

```python
import flet as ft
from Neostate import app, Page

# Home page function
def home_page(page: Page):
    return [ft.Text("Welcome to the Home Page!"),
    ft.Button("Go to Next Page", on_click=lambda e: page.swap())]

# Next page function
def next_page(page: Page):
    return [ft.Text("This is the Next Page"),
    ft.Button("Back to Home", on_click=lambda e: page.back())]

def main(page: Page):
    page.horizontal_alignment = 'center'

    # Set global action for page view pop
    page.on_view_pop = page.back

    # Set initial page
    page.reach("/home", home_page)

# Run the app
app(target=main)
```

### 3. Page Functions and Navigation Methods

Here’s a breakdown of the main navigation functions:

- **`page.swap()`**: This clears the current page view and swaps to a new one. It’s ideal for replacing the entire page when you want to show completely different content.

- **`page.refresh()`**: Refreshes the current page, re-rendering its contents. This is useful if you want to update the page without navigating away.

- **`page.back()`**: Goes back to the previous page. This method can be triggered automatically by setting `page.on_view_pop = page.back` (as seen in the examples above) or called manually.

### 4. Example of Using `page.refresh()`

Sometimes, instead of swapping or navigating, you may want to refresh the current page, especially if there’s new data to display.

```python
page.refresh()   #it refreshes the current page
```

In this example, clicking the "Refresh Again" button will trigger the `page.refresh()` method, causing the page to refresh.

### 5. Example of Using `page.back()`

To navigate back to the previous page, you can use the `page.back()` method, like this:

```python
page.back()  
```

In this case, the button will take the user back to the Home page when clicked.

## Summary 📚

In this guide, we learned how to use NeoRoute for simple page navigation in Flet apps. Here's a recap of the main points:
- **`page.swap()`**: Swaps the current page with a new one.
- **`page.refresh()`**: Refreshes the current page.
- **`page.back()`**: Takes the user back to the previous page.
- **`page.reach()`**: Links a route to a page function.

With these functions, you can easily build a multi-page app with intuitive navigation and seamless page transitions. Enjoy building with NeoRoute! 😊

## Installation 🔧

To get started, install the necessary libraries:

1. Install Flet:
   ```bash
   pip install flet
   ```

2. Install Neostate:
   ```bash
   pip install Neostate
   ```
Ah, I see what you're aiming for now! Let's clear things up and explain it correctly.

### `page.reach()` vs `page.swap()` 🔄

Here’s a correct breakdown of both methods:

---

### 1. **When to use `page.reach()`** 📍

**`page.reach()` is used when you want to **append** a page to the current view or navigate to a new page in a stack-like manner.**

- **Stacking Pages**: `page.reach()` essentially "pushes" a new page onto the view stack. You can use it to **navigate to a new page** without completely replacing the current page. The previous page is still accessible, and when you hit "back," it returns to the previous page.
- **Back Navigation**: The app automatically manages the back button functionality, and when you press back (or the system back), it goes back to the previous page that was reached with `page.reach()`.

#### Example Use Cases for `page.reach()`:
- **Navigating to a new page while keeping the old one**: This is useful in apps where users navigate between several pages or views and want to go back to the previous page later.
  
```python
# Pushes the home page onto the view stack
page.reach("/home", home_page)

# When you navigate to the next page using page.reach()
page.reach("/next", next_page)
```

In this example, using `page.reach()` on `/home` and then `/next` will stack both pages in the history. Pressing back will bring the user back to the `/home` page.

---

### 2. **When to use `page.swap()`** 🔄

**`page.swap()` replaces the current page's content with a new page or view entirely.**

- **Replacing the Entire View**: `page.swap()` clears the current page and replaces it with a new one. This is like doing a "full-page" switch where the previous content is no longer visible, and the new content takes over the entire view.
- **No Back Stack**: Since `page.swap()` doesn’t stack pages, you won’t be able to go back to the previous page using the back button.

#### Example Use Cases for `page.swap()`:
- **Switching Views or Content**: If you want to replace the current content with something new immediately, like when a user clicks a button to change the page's content.
  
```python
# Replaces current view with the next page
page.swap(next_page)
```

In this case, the current content is replaced with the new page, and there is no "going back" unless you define custom navigation logic.

---

### Key Differences:

| **Feature**             | **`page.reach()`**                                          | **`page.swap()`**                                       |
|-------------------------|------------------------------------------------------------|---------------------------------------------------------|
| **Behavior**            | Appends a new page to the view stack, allowing back navigation. | Replaces the current page/view entirely.                |
| **Navigation Type**     | Stack navigation (previous pages can be accessed via back). | Full-page transition with no history.                   |
| **Back Button**         | Works with the back button to navigate to the previous page. | Does not support back navigation by default.            |
| **Example Use**         | Adding a new page (e.g., `/home`, `/about`) and returning back. | Replacing content with a new page or view.              |

---

### Correct Example with `page.reach()`:

```python
import flet as ft
from Neostate import app, Page

# Home page function
def home_page(page: Page):
   return [ ft.Text("Welcome to the Home Page!"),
    ft.Button("Go to Next Page", on_click=lambda e: page.reach("/next", next_page))]

# Next page function
def next_page(page: Page):
    return [ft.Text("This is the Next Page"),
    ft.Button("Back to Home", on_click=lambda e: page.back())]  # This will return to the home page

# Main app function
def main(page: Page):
    page.horizontal_alignment = 'center'

    # Set up the initial page
    page.reach("/home", home_page)

# Run the app
app(target=main)
```

### Here’s what happens:
1. The app starts on the home page.
2. When the user clicks the button on the home page, `page.reach("/next", next_page)` pushes the next page onto the view stack.
3. The user can press the back button to return to the home page, as both pages are in the view stack.

### Correct Example with `page.swap()`:

```python
import flet as ft
from Neostate import app, Page

# Home page function
def home_page(page: Page):
    return [ft.Text("Welcome to the Home Page!"),
    ft.Button("Go to Next Page", on_click=lambda e: page.swap(next_page))]

# Next page function
def next_page(page: Page):
    return [ft.Text("This is the Next Page"),
    ft.Button("Back to Home", on_click=lambda e: page.swap(home_page))] # Swap back to home page

# Main app function
def main(page: Page):
    page.horizontal_alignment = 'center'

    # Set up the initial page
    page.reach("/home", home_page)

# Run the app
app(target=main)
```

### Here’s what happens:
1. The app starts on the home page.
2. When the user clicks the button on the home page, `page.swap(next_page)` replaces the home page with the next page.
3. The user cannot use the back button to return because `page.swap()` doesn’t stack pages. Instead, pressing the button on the next page calls `page.swap(home_page)` to replace it back to the home page.

---

### Summary:

- **Use `page.reach()`** when you want to add a page to the view stack and keep it in history, allowing the user to go back to the previous page.
- **Use `page.swap()`** when you want to completely replace the current page or content with something new and don’t need a back button to return.

I hope that clears up the confusion! 😊

Happy coding! 🎉
