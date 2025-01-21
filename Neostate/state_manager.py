import warnings
from typing import Callable
#──────────────────────────────────────────────────
# StateNotifier Class
#──────────────────────────────────────────────────
class StateNotifier:
    """
    A utility class to manage shared state and notify listeners about updates.

    Example:
        color = StateNotifier("red")
        color.value = "blue"  # Updates all listeners
    """
    def __init__(self, value):
        self._value = value
        self._listeners = []

    @property
    def value(self):
        """Get the current value of the shared state."""
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Set a new value for the shared state and notify listeners.
        """
        if self._value != new_value:
            self._value = new_value
            self.notify_listeners()

    def notify_listeners(self):
        """Notify all registered listeners about the current state value."""
        for listener in self._listeners:
            try:
                listener(self._value)
            except Exception as e:
                print(f"[ERROR]: {e}")

    def add_listener(self, listener):
        """Add a listener function to be notified on state changes."""
        self._listeners.append(listener)

    def remove_listener(self, listener):
        """Remove a listener function from the notification list."""
        if listener in self._listeners:
            self._listeners.remove(listener)

    def __str__(self):
        """String representation of the current value."""
        return str(self._value)

    def __repr__(self):
        return f"StateNotifier(value={self._value})"


#──────────────────────────────────────────────────
# Shared Class
#──────────────────────────────────────────────────
class Formatter:
    def __init__(self,value:StateNotifier,format: Callable[[any], any]) -> None:
        if not isinstance(value, StateNotifier):
            raise TypeError("value must be an instance of StateNotifier.")
        
        if not callable(format):
            raise TypeError("formatter must be a callable function.")
        
        self.value=value
        self.formatter=format
class Shared:
    """
    Automatically binds a Flet widget's attributes to shared states using StateNotifier.

    Example:
        State1 = StateNotifier("red")
        widget = Shared(Text(value=f"Color is {State1}", bgcolor=State1))
    """
    def __init__(self, widget,formatter = None):
        self.formatter = formatter
        self.widget = widget
        self.bind_attributes(widget)
    
    def bind_attributes(self, widget):
        """
        Binds widget attributes that reference StateNotifier objects.
        """
        # with warnings.catch_warnings():
        #   warnings.simplefilter("ignore", DeprecationWarning) 
        #   for attr_name in dir(widget):
        #     if not attr_name.startswith("_"):
        #         attr_value = getattr(widget, attr_name, None)
        #         if isinstance(attr_value, StateNotifier):
                    
        #             # Attach listener for StateNotifier
        #             attr_value.add_listener(lambda value, attr=attr_name: self.update_widget(attr, value))
        #             # Initialize with the current state value
                    
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning) 
            
            # Define a helper function for checking if attribute value is a StateNotifier
            def attach_listener(attr_name, widget):
                attr_value = getattr(widget, attr_name, None)
                if isinstance(attr_value, StateNotifier) :
                    # Attach listener for StateNotifier
                    attr_value.add_listener(lambda value, attr=attr_name: self.update_widget(attr, value))
                    # Initialize with the current state value
                    if self.formatter:
                        setattr(self.widget, attr_name,self.formatter(attr_value.value) )
                elif  isinstance(attr_value,Formatter):
                    attr_value.value.add_listener(lambda value,formatte=attr_value.formatter, attr=attr_name: self.formatted_update_widget(attr, value,formatte))
                    # Initialize with the current state value
                    
                    setattr(self.widget, attr_name,attr_value.formatter(attr_value.value.value) )        

            # Use filter to get attributes without the leading underscore
            attrs = filter(lambda attr: not attr.startswith("_"), dir(widget))
            
            # Apply the helper function for each relevant attribute
            list(map(lambda attr: attach_listener(attr, widget), attrs))
            del attrs
    def formatted_update_widget(self, attr_name, value,formatter):
        """
        Update the widget's attribute when the shared state changes.

        Args:
            value: The new value to set.
        """
        try:
           
            setattr(self.widget, attr_name,formatter(value) )  
            self.widget.update()
        except Exception as e:
            print(f"[ERROR in Shared]: {e}")    
    def update_widget(self, attr_name, value):
        """
        Update the widget's attribute when the shared state changes.

        Args:
            value: The new value to set.
        """
        try:
              
            setattr(self.widget, attr_name,self.formatter(value) if self.formatter else value)

            self.widget.update()
        except Exception as e:
            print(f"[ERROR in Shared]: {e}")
    def __getattr__(self, attr):
        """
        Fallback to the underlying widget's attributes.

        Raises:
            AttributeError: If the attribute does not exist.
        """
        if hasattr(self.widget, attr):
            return getattr(self.widget, attr)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        """
        Set attributes on the underlying widget unless they belong to Shared itself.

        Args:
            attr (str): Attribute name.
            value: Value to assign to the attribute.
        """
        if attr in {"widget", "state_notifier", "attribute", "formatter"}:
            super().__setattr__(attr, value)
        else:
            setattr(self.widget, attr, value)
  
    
    def __str__(self):
        return str(self.widget)

    def __repr__(self):
        return f"Shared(widget={self.widget})"


#──────────────────────────────────────────────────
# Usage Example
#──────────────────────────────────────────────────
# import flet as ft

# def main(page: ft.Page):
    

    
    
    
#     State1 = StateNotifier(0)
   
#     page.scroll=ft.ScrollMode.ALWAYS    
    
    
    
    
    
#     def Change_state(e):
#         State1.value=int(e.control.value)
        
    
#     colors=['red','blue','green','yellow','purple']
 
#     data =Center( 
#         ft.Column([Shared(ft.Text(weight=ft.FontWeight.BOLD,size=25,
#                               value=Formatter(value=State1,format=lambda value: f'border Radius is {value}')
#         )),
#         ft.Column([Shared(
#                         ft.Container(bgcolor=colors[color],
                                     
#                                     height=Formatter(value=State1,format= lambda value,color=color : value*(color+1)),
#                                     border_radius=State1,
#                                     animate=ft.animation.Animation(280, ft.AnimationCurve.EASE_IN_OUT),
#                                     width=200),
#                          )
#                    for color in range(len(colors))]
#                   )
      
#        ,ft.Slider(max=50,min=0,on_change=Change_state)
#     ]),force=True,expand=True)
    
#     page.add(data)


# ft.app(target=main)