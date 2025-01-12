

<div align="center">

# 🔥Neostate 🎨✨
[![github](https://img.shields.io/badge/my_profile-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dekuChaurasia)[![pypi](https://img.shields.io/badge/Pypi-0A66C2?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/neostate)

[![image](https://img.shields.io/pypi/pyversions/neostate.svg)](https://pypi.python.org/pypi/neostate) [![image](https://img.shields.io/pypi/v/neostate.svg)](https://pypi.python.org/pypi/neostate)  [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Downloads](https://static.pepy.tech/badge/neostate)](https://pepy.tech/project/neostate)



`Neostate` is a package designed to simplify and optimize state management in [`Flet`](https://github.com/flet-dev/flet) apps. It provides a clean and easy way to handle global and scoped states, allowing you to build apps with a simpler and more powerful state management system.

</div>





*Elegant Routing ,State Management & More for Flet Applications*

---

Welcome to **Neostate**! 🌈 A lightweight and intuitive library for managing shared states in Flet applications,Use routing with Ease and much more, With Neostate, you can bind widgets to a shared state effortlessly, enabling seamless updates across your UI components with minimal boilerplate.


## 💡 Installation

Install the package from PyPI:

```bash
pip install Neostate
```

---

# 🔄  Shared State  🔄

---

### **🛠 StateNotifier Class**  
**What is it?**  
Think of **StateNotifier** like a **magic box** where we store important information, like a **score** in a game. When the score changes, it **shouts out to everyone** that it's been updated!

**How it works**:  
- We create a **StateNotifier** with a starting score.  
- If the score changes, **StateNotifier** tells everyone who’s listening, like other parts of your app, to **update** and show the new score!  

**Fun part** 🎉: You can add or remove listeners, like telling certain parts of the app to pay attention when the score changes.

---

## 🔧 Features

- 🔄 **Reactive State Management**: Automatically update UI components when the state changes.
- 💪 **Simple Widget Binding**: Use the `Shared` class to bind Flet widgets dynamically to shared states.
- 🔧 **Formatter Support**: Customize how state values are displayed with flexible formatting strings.
- 🌍 **Complex Widget Attributes**: Update attributes like `content`, `value`, or `controls` dynamically.
- ⏳ **Detachable Listeners**: Add or remove widgets from state listeners as needed.
- 🚀 **Inline State Updates**: Use intuitive operations like `shared_state.value += 1`.
- 📓 **Easy to Learn and Use**: Minimal learning curve with a clean, developer-friendly 

### **🔗 Shared Class** 

**What is it?**  
Imagine you have a **cool widget** (like a **score display**) and you want it to **automatically change** when the score updates. **Shared** makes this happen!

**How it works**:  
- **Shared** links the **score widget** to the **StateNotifier** (the magic box from above).  
- When the score changes, the **widget** instantly **updates itself** to show the new score. No need to do anything manually!  

**What’s special** 💫:  
- If you have a special **formatting** (like showing the score as **“Score: 10”**), you can tell **Shared** to format it for you.
- It will always keep the widget **in sync** with the score!

---

### 🧑‍🏫 **How They Work Together**:  
- **StateNotifier** keeps the **score** (or any value) safe.
- **Shared** makes sure your **widgets** (like score displays) stay updated with the **new value** whenever it changes!

It’s like a **team** where one member holds the information (StateNotifier) and the other makes sure everything looks correct and up-to-date (Shared).

---

**And that’s how you make your app super interactive!** 🎮

Let me know if you'd like more details or adjustments! 😊📚

<a href="/docs/statenotifier.md" target="_blank">
  <img src="https://img.shields.io/badge/Explore%20Full%20Documentation-blue-1abc9c?style=for-the-badge&logo=read-the-docs" alt="Explore Documentation" />
</a>

<hr style="border: 1px  #1abc9c; background-color: #1abc9c; height: px;"/>




# Routing Modes 🚥

### **Basic Routing 🚶‍♂️**

Basic routing allows you to manage navigation between pages in a simple way, using predefined methods like `swap`, `reach`, `back`, and `refresh`.

##### How it works:
here function means : the function which return ui like ```return [ft.Container(height=100) ]```
1. **swap(route, function)**: This method adds a new page to the views stack and navigates to it. It appends the new view without removing the existing ones.
2. **reach(route, function)**: This method replaces the entire view stack with a new page.
3. **back()**: This method allows you to go back to the previous view.
4. **refresh()**: This method refreshes the current view.

To **activate Basic Routing**, you just need to call the app with `advanced_routing=False`:

```python
enhanced_app(target, advanced_routing=False)
```

Example:
```python
def home_page(page):
    return Column([Text("Welcome to Home!")])

def about_page(page):
    return Column([Text("About Us")])

# Basic Routing with swap and reach methods
page.swap("/home", home_page)
page.reach("/about", about_page)
```

---

#### **Advanced Routing 🚀**

Advanced routing gives you more control by using `RoutingConfig` to register routes, middlewares, and error pages. This mode is ideal for complex applications where you need more flexibility.

##### How it works:
1. **RoutingConfig.register_route**: Register routes with optional guards, custom redirects, and custom error pages.
2. **apply_middlewares**: Apply middleware functions to routes for conditions like authentication.
3. **Global error pages**: Define custom error pages for "404", "not allowed", etc.

To **activate Advanced Routing**, you call the app with `advanced_routing=True`:

```python
enhanced_app(target, advanced_routing=True)
```

Example:
```python
page.register_route("/home", home_page)
page.register_route("/about", about_page)
page.set_global_error_page("404", page_not_found)
page.register_middleware(auth_middleware)
```

---

## Switch Between Routing Modes 🔄

You can easily switch between **Basic** and **Advanced** routing modes:

- **For Basic Routing**, set `advanced_routing=False`:
  ```python
  enhanced_app(target, advanced_routing=False)
  ```

- **For Advanced Routing**, set `advanced_routing=True`:
  ```python
  enhanced_app(target, advanced_routing=True)
  ```

**When to Choose Which?** 🤔

🚗 **Basic Routing:** Best for mobile and desktop apps, providing simple and fast navigation.  
🏎️ **Advanced Routing:** Perfect for websites and web apps, supporting complex setups with middleware and role-based access.

---
<div align="center">

  <!-- Basic Routing Button -->
  <a href="/docs/basic_routing.md" target="_blank">
    <img src="https://img.shields.io/badge/Basic%20Routing-docs-1abc9c?style=for-the-badge&logo=read-the-docs" alt="Basic Routing" />
  </a>

  <!-- Advanced Routing Button -->
  <a href="/docs/advanced_route.md" target="_blank">
    <img src="https://img.shields.io/badge/Advanced%20Routing-docs-1abc9c?style=for-the-badge&logo=read-the-docs" alt="Advanced Routing" />
  </a>

</div>

<hr style="border: 1px  #1abc9c; background-color: #1abc9c; height: px;"/>

# Extras
Here’s the updated changelog with the emojis added back in:

---



- 🛠️ **Neostate App Creation Command**  
  Creating a new app template is now easier than ever! Use the `neostate create appname` command in the terminal to generate your app structure. Here's the generated directory structure:
  
  ```plaintext
  <appname>/
  ├── assets/
  │   ├── fonts/
  │   └── images/
  ├── App/
  │   ├── components/
  │   ├── pages/
  │   ├── services/
  │   ├── state/
  │   ├── utils/
  │   └── main.py
  ├── main.py
  ├── requirements.txt
  └── README.md
  ```
#### Just Use this command inside terminal/cmd in empty folder
``` bash
Neostate create <appname> 
```
``` <appname> ``` can be anything like ``` firstapp ```

---

- 🎯 **Center Widget Support**  
  Added a `Center` widget to simplify centering any widget. Whether it's a `Column`, `Row`, or `Container` simply wrap it with `Center(ft.column([]))` to achieve perfect centering. The `force` and `expand` arguments are optional.
```
#usage
from Neostate Import Center
Center(ft.Column([])  #or can be any widget

)
```
#### it has two optional argument ``` force ``` and ``` expand ``` , True or False can be passed , test it out yourself

Enjoy these new features to enhance your app development workflow!

---
