  
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