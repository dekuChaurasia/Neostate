### Neostate 🎨✨

*Elegant State Management for Flet Applications*

---

Welcome to **Neostate**! 🌈 A lightweight and intuitive library for managing shared states in Flet applications. With Neostate, you can bind widgets to a shared state effortlessly, enabling seamless updates across your UI components with minimal boilerplate.

---

## 🔧 Features

- 🔄 **Reactive State Management**: Automatically update UI components when the state changes.
- 💪 **Simple Widget Binding**: Use the `Shared` class to bind Flet widgets dynamically to shared states.
- 🔧 **Formatter Support**: Customize how state values are displayed with flexible formatting strings.
- 🌍 **Complex Widget Attributes**: Update attributes like `content`, `value`, or `controls` dynamically.
- ⏳ **Detachable Listeners**: Add or remove widgets from state listeners as needed.
- 🚀 **Inline State Updates**: Use intuitive operations like `shared_state.value += 1`.
- 📓 **Easy to Learn and Use**: Minimal learning curve with a clean, developer-friendly API.

---

## 💡 Installation

Install the package from PyPI:

```bash
pip install Neostate
```

---

## 🌐 Documentation Overview

This guide will take you from the basics to advanced use cases, teaching you how to:
1. Bind widgets to a shared state.
2. Use formatters for custom value display.
3. Handle complex controls and attributes.

### 🔗 **Basic Example**: Reactive State Binding

Let’s start with a simple example where a `Text` widget is bound to a shared counter.

```python
import flet as ft
from Neostate import StateNotifier, Shared

def main(page: ft.Page):
    # Shared state
    shared_state = StateNotifier(0)

    # Create a Text widget bound to shared_state
    text_widget = Shared(
        ft.Text(),
        shared_state,
        "value",  # Attribute to update
        formatter="Counter: {value}"
    )

    # Button to increment the counter
    def increment_value(e):
        shared_state.value += 1  # Automatically updates the Text widget

    page.add(
        text_widget,  # Add the bound widget
        ft.ElevatedButton("Increment", on_click=increment_value)
    )

ft.app(target=main)
```

**Explanation:**
- `StateNotifier` manages the shared state.
- `Shared` binds the `Text` widget to the state and dynamically updates it whenever the state changes.
- The `formatter` parameter customizes how the value is displayed.

---

### 🔧 **Intermediate Example**: Multiple Widgets Bound to the Same State

In this example, multiple `Text` widgets and a `Container` are updated whenever the state changes.

```python
import flet as ft
from Neostate import StateNotifier, Shared

def main(page: ft.Page):
    # Shared state
    shared_state = StateNotifier("Initial Value")

    # Widgets bound to the shared state
    text1 = Shared(
        ft.Text(),
        shared_state,
        "value",
        formatter="Text 1: {value}"
    )
    text2 = Shared(
        ft.Text(),
        shared_state,
        "value",
        formatter="Text 2: {value}"
    )
    container = Shared(
        ft.Container(bgcolor="blue", width=200, height=100),
        shared_state,
        "content"  # Attribute to update dynamically
    )

    # Input field to update the state
    input_field = ft.TextField(
        label="Update Value",
        on_change=lambda e: setattr(shared_state, 'value', e.control.value)
    )

    page.add(
        ft.Column([text1, text2, container]),
        input_field
    )

ft.app(target=main)
```

**Explanation:**
- `Shared` can bind various widget types like `Text` and `Container` to the same shared state.
- Dynamic updates are reflected across all bound widgets when the state changes.
- The `attribute` parameter determines which attribute (e.g., `value`, `content`) is updated.

---

### 🌟 **Advanced Example**: Complex Layout with Columns and Rows

Here’s a more advanced example that combines multiple widgets in a complex layout:

```python
import flet as ft
from Neostate import StateNotifier, Shared

def main(page: ft.Page):
    # Shared state
    shared_state = StateNotifier(0)

    # Create a ListView with multiple bound Text widgets
    listview = ft.ListView([
        Shared(
            ft.Text(),
            shared_state,
            "value",
            formatter=f"Text Widget {i+1}: {{value}}"
        ) for i in range(5)
    ])

    # Container bound to shared_state
    bound_container = Shared(
        ft.Container(bgcolor="green", width=300, height=150),
        shared_state,
        "content"
    )

    # Increment Button
    def increment_value(e):
        shared_state.value += 1

    page.add(
        ft.Column([
            ft.Row([listview, bound_container]),
            ft.ElevatedButton("Increment", on_click=increment_value)
        ])
    )

ft.app(target=main)
```

**Key Highlights:**
- Combine multiple widgets like `ListView`, `Container`, and `Row` in a complex layout.
- State updates propagate to all widgets, ensuring a fully reactive UI.

---

### 🎨 Dynamic Examples: Interactive Widgets

#### 🌐 Real-Time Text Transformation
```python
import flet as ft
from Neostate import StateNotifier, Shared

def main(page: ft.Page):
    # Shared state
    shared_state = StateNotifier("")

    # TextField to input text
    input_field = ft.TextField(
        label="Enter text",
        on_change=lambda e: setattr(shared_state, 'value', e.control.value)
    )

    # Text widget to display transformed text
    transformed_text = Shared(
        ft.Text(),
        shared_state,
        "value",
        formatter="Uppercase: {value.upper()}"
    )

    page.add(
        input_field,
        transformed_text
    )

ft.app(target=main)
```

---

#### 🎩 Dynamic Styling Example
```python
import flet as ft
from Neostate import StateNotifier, Shared

def main(page: ft.Page):
    # Shared state for background color
    color_state = StateNotifier("red")

    # Container with dynamic background color
    dynamic_container = Shared(
        ft.Container(width=200, height=100),
        color_state,
        "bgcolor"
    )

    # Dropdown to change color
    dropdown = ft.Dropdown(
        options=["red", "blue", "green"],
        on_change=lambda e: setattr(color_state, 'value', e.control.value)
    )

    page.add(
        dynamic_container,
        dropdown
    )

ft.app(target=main)
```

---

## 🔧 Deep Dive: Parameters in `Shared`

### **Parameters**
- **`widget`**: Any Flet widget (e.g., `ft.Text`, `ft.Container`, `ft.ListView`).
- **`state_notifier`**: The `StateNotifier` managing the shared state.
- **`attribute`**: The widget attribute to update (e.g., `value`, `content`, `controls`).
- **`formatter`**: A string to format state values, applicable only to `ft.Text` widgets.

### **Attributes You Can Bind**
| Widget Type    | Attribute   | Description                          |
|----------------|-------------|--------------------------------------|
| `ft.Text`      | `value`     | Updates the text content             |
| `ft.Container` | `bgcolor`   | Dynamically updates background color |
| `ft.ListView`  | `controls`  | Dynamically updates child widgets    |

---

## 📊 Roadmap
- Add support for more widget types.
- Improve error messages and debugging tools.
- Provide hooks for advanced customizations.

---

## 🚀 Get Started
Install Neostate today and build reactive Flet applications with ease!

---

