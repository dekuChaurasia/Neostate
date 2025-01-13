from flet import Text

#──────────────────────────────────────────────────
# StateNotifier Class
#──────────────────────────────────────────────────
class StateNotifier:
    """
    A utility class to manage shared state and notify listeners about updates.

    Attributes:
        _value: Holds the current value of the shared state.
        _listeners: A list of functions (listeners) that are triggered upon state changes.
    """
    def __init__(self, value):
        self._value = value  # Initial state value
        self._listeners = []  # List of listeners to notify

    @property
    def value(self):
        """Get the current value of the shared state."""
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Set a new value for the shared state.
        Automatically notifies listeners if the value changes.
        """
        if self._value != new_value:
            self._value = new_value
            self.notify_listeners()

    def add_listener(self, listener):
        """
        Add a listener function to be notified on state changes.

        Args:
            listener (function): A callback function to handle state updates.
        """
 
        
        self._listeners.append(listener)

    def remove_listener(self, listener):
        """
        Remove a listener function from the notification list.

        Args:
            listener (function): The listener to remove.
        """
        if listener in self._listeners:
            self._listeners.remove(listener)

    def notify_listeners(self):
        """
        Notify all registered listeners about the current state value.

        Raises:
            AttributeError: If a listener is invalid.

        ASCII Example:
        +-----------------------------------+
        | NOTIFYING ALL REGISTERED LISTENERS |
        +-----------------------------------+
        """
        for listener in self._listeners:
            try:
                listener(self._value)
            except Exception as e:
                print(f"[ERROR]: {e}")


#──────────────────────────────────────────────────
# Shared Class
#──────────────────────────────────────────────────
class Shared:
    """
    Bind a widget to a shared state using a StateNotifier.

    Automatically updates the widget when the state changes.

    Parameters:
        widget: The Flet widget to bind.
        state_notifier (StateNotifier): Manages the shared state.
        attribute (str): The widget attribute to update (e.g., "value").
        formatter (str, optional): A string formatter (only for ft.Text widgets).

    ASCII Example (for errors):

        +----------------------------------------+
        | ERROR: FORMATTER ONLY ALLOWED FOR TEXT |
        +----------------------------------------+

    """
    def __init__(self, widget, state_notifier, attribute, formatter=None):
        # Raise an error if formatter is used with non-ft.Text widgets
        if formatter and not isinstance(widget, Text):
            raise TypeError(
                f"""
        +------------------------------------------------+
        | ERROR: FORMATTER ONLY ALLOWED FOR TEXT WIDGETS |
        +------------------------------------------------+

         Provided: {type(widget).__name__}.
         Details: widget={widget}"""
            )

        self.widget = widget
        self.state_notifier = state_notifier
        self.attribute = attribute
        self.formatter = formatter

        # Subscribe to state changes
        self.state_notifier.add_listener(self.update_widget)
        if self.formatter:
                
                setattr(self.widget, self.attribute,  self.formatter.format(value=state_notifier.value))
        else:
                setattr(self.widget, self.attribute, state_notifier.value)

    def update_widget(self, value):
        """
        Update the widget's attribute when the shared state changes.

        Args:
            value: The new value to set.
        """
        try:
            if self.formatter:
                formatted_value = self.formatter.format(value=value)
                setattr(self.widget, self.attribute, formatted_value)
            else:
                setattr(self.widget, self.attribute, value)

            self.widget.update()
        except:
            pass    

    def detach(self):
        """
        Detach this widget from the StateNotifier's listeners.

        ASCII Example:

        +---------------------------+
        | DETACHING WIDGET LISTENER |
        +---------------------------+
        """
        self.state_notifier.remove_listener(self.update_widget)

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
  
