import flet as ft
class Center(ft.Container):
    def __init__(self, widget,force=False,expand=False):
        # Initialize the Container class
        super().__init__()
        if force:
            if isinstance(widget, ft.Row):
                if widget.alignment is None:
                    # Horizontally center the Row's children
                    widget.alignment = ft.MainAxisAlignment.CENTER
                if widget.vertical_alignment is None:
                    widget.vertical_alignment='center'
            
            if isinstance(widget, ft.Column):
                if widget.alignment is None:
                    # Vertically center the Column's children
                    widget.alignment = ft.MainAxisAlignment.CENTER
                if widget.horizontal_alignment is None:    
                    widget.horizontal_alignment='center'
        
        # Set the alignment for the container
        self.alignment = ft.alignment.center  # Center the widget in the container
        self.content = widget  # Set the passed widget as the content
        if expand:
            self.expand = True  # Allow the container to expand to fill space
            self.expand_loose = True  # Allow loose expansion

