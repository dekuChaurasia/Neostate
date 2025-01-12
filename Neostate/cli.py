import sys
import os


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "create":
        print("Usage: neostate create <appname>")
        sys.exit(1)

    app_name = sys.argv[2]
    create_structure(app_name)


def create_structure(app_name):
    # Root folders and files
    root = app_name
    folders = [
        f"{root}/assets/images",
        f"{root}/assets/fonts",
        f"{root}/App/components",
        f"{root}/App/pages",
        f"{root}/App/services",
        f"{root}/App/state",
        f"{root}/App/utils"
    ]
    files = [
        f"{root}/App/main.py",
        f"{root}/main.py",
        f"{root}/requirements.txt",
        f"{root}/README.md"
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Create empty files
    for file in files:
        with open(file, "w") as f:
            pass
    
    # Write default content
    write_app_py(f"{root}/App/main.py")
    write_app_py2(f"{root}/main.py")
    write_requirements_txt(f"{root}/requirements.txt")
    write_readme_md(f"{root}/README.md")
    
    print(f"Your Flet app '{app_name}' has been created successfully!")
    print(f"To run the app in hot reload mode: flet run {app_name}/main.py")
def write_app_py(filepath):
        code = """import flet as ft
from Neostate import Page, StateNotifier, Shared, Center

# Home Page
def home_page(page: Page):
    return [Center(force=1, widget=
        ft.Column(
            [
                ft.Text("🏠 Welcome to the Interactive Documentation", size=36, weight="bold", color="blue600"),
                ft.Text(
                    "This app will teach you how to use routing, StateNotifier, and Shared() in NeoState.",
                    size=18,
                ),
                ft.ElevatedButton(
                    "➡️ Learn About Routing",
                    icon=ft.icons.NAVIGATE_NEXT,
                    bgcolor="green",
                    color="white",
                    on_click=lambda e: page.reach("/routing", routing_page),
                ),
                ft.ElevatedButton(
                    "📋 Explore StateNotifier",
                    icon=ft.icons.MANAGE_ACCOUNTS,
                    bgcolor="orange",
                    color="white",
                    on_click=lambda e: page.swap("/state", state_page),
                ),
                ft.ElevatedButton(
                    "🔗 Understand Shared()",
                    icon=ft.icons.LINK,
                    bgcolor="purple",
                    color="white",
                    on_click=lambda e: page.swap("/shared", shared_page),
                ),
            ],
            alignment="center",
            spacing=20,
        )
    )]

# Routing Page
def routing_page(page: Page):
    return [Center(force=1, widget=
        ft.Column(
            [
                ft.Text("🚀 Routing in NeoState", size=36, weight="bold", color="green600"),
                 ft.Text('''Routing allows you to navigate between different views effortlessly. 
                    NeoState provides two powerful methods for navigation:
                    
                    
                    1️⃣ **page.reach**: For navigating to predefined routes.
                    
                    2️⃣ **page.swap**: For dynamic navigation without predefined routes.''',
                    size=18,
                ),
                ft.Text(
                    '''# Example: Using page.reach
page.reach("/home", home_page)

# Example: Using page.swap
page.swap("/contact", contact_page)
                    '''
                ),
                ft.ElevatedButton(
                    "⬅️ Back to Home",
                    icon=ft.icons.HOME,
                    bgcolor="blue",
                    color="white",
                    on_click=lambda e: page.reach("/home", home_page),
                ),
                ft.ElevatedButton(
                    "📋 Explore StateNotifier",
                    icon=ft.icons.MANAGE_ACCOUNTS,
                    bgcolor="orange",
                    color="white",
                    on_click=lambda e: page.swap("/state", state_page),
                ),
            ],
            alignment="center",
            spacing=20,
        )
    )]

# StateNotifier Page
def state_page(page: Page):
    return [Center(force=1, widget=
        ft.Column(
            [
                ft.Text("📋 StateNotifier in NeoState", size=36, weight="bold", color="orange600"),
                ft.Text(
                    "StateNotifier allows you to manage and share state across widgets. "
                    "This ensures that your app remains dynamic and responsive.",
                    size=18,
                ),
                ft.Text(
                    '''# Example: Using StateNotifier

class MyState(StateNotifier):
    def __init__(self):
        self.count = 0

state = MyState()
state.increment()
                    ''',
                    
                ),
                ft.Text(
                    "➡️ StateNotifier ensures all widgets dependent on state are updated automatically.",
                    size=18,
                    italic=True,
                ),
                ft.ElevatedButton(
                    "⬅️ Back to Home",
                    icon=ft.icons.HOME,
                    bgcolor="blue",
                    color="white",
                    on_click=lambda e: page.reach("/home", home_page),
                ),
                ft.ElevatedButton(
                    "🔗 Learn About Shared()",
                    icon=ft.icons.LINK,
                    bgcolor="purple",
                    color="white",
                    on_click=lambda e: page.swap("/shared", shared_page),
                ),
            ],
            alignment="center",
            spacing=20,
        )
    )]

# Shared Page
def shared_page(page: Page):
    return [Center(force=1, widget=
        ft.Column(
            [
                ft.Text("🔗 Shared() in NeoState", size=36, weight="bold", color="purple600"),
                ft.Text(
                    "Shared() allows you to bind widgets to shared state, making them automatically update when the state changes.",
                    size=18,
                ),
                ft.Text(
                    '''# Example: Using Shared()




# Bind widget to shared state

                    ''',
                    
                ),
                ft.Text(
                    "➡️ With Shared(), you can ensure a consistent UI across your app.",
                    size=18,
                    italic=True,
                ),
                ft.ElevatedButton(
                    "⬅️ Back to Home",
                    icon=ft.icons.HOME,
                    bgcolor="blue",
                    color="white",
                    on_click=lambda e: page.reach("/home", home_page),
                ),
                ft.ElevatedButton(
                    "🚀 Learn About Routing",
                    icon=ft.icons.NAVIGATE_NEXT,
                    bgcolor="green",
                    color="white",
                    on_click=lambda e: page.reach("/routing", routing_page),
                ),
            ],
            alignment="center",
            spacing=20,
        )
   ) ]

# Main Page
def main(page: Page):
    # Set page properties
    page.title = "Interactive NeoState Documentation"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20

    # AppBar for navigation
    page.appbar = ft.AppBar(
        title=ft.Text("NeoState Documentation", weight="bold"),
        bgcolor="blue600",
    )

    # Set the initial view
    page.reach("/home", home_page)
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)


# Writing the content to a Python file

    

def write_app_py2(filepath):
    content = """import flet as ft
from Neostate import Page, app
from App.main import main as runner


def main(page: ft.Page):
    runner(page)

app(target=main)
"""
    with open(filepath, "w") as f:
        f.write(content)


def write_requirements_txt(filepath):
    content = """flet
requests
"""
    with open(filepath, "w") as f:
        f.write(content)


def write_readme_md(filepath):
    content = """# My Flet App

This is a production-ready Flet app.

## Folder Structure
- **assets/**: Static files like images, fonts, etc.
- **components/**: Reusable UI components.
- **pages/**: App pages/screens.
- **services/**: Business logic and APIs.
- **state/**: State management.
- **utils/**: Helper functions and utilities.

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
"""