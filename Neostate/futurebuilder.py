from inspect import iscoroutinefunction
from flet import Container, Text, ProgressRing,Row


class Snapshot:
    """Represents the state of an operation (loading, completed, or error)."""

    def __init__(self, state: str, data=None, error=None):
        self.state = state  # 'loading', 'completed', 'error'
        self.data = data
        self.error = error


class FutureBuilder(Container):
    """Custom widget for handling async operations dynamically."""

    def __init__(
        self,
        future,
        on_data,
        on_loading=lambda: Row([ProgressRing(), Text("Loading...")]),
        on_error=lambda snapshot: Text(f"Error: {snapshot.error}",color='red'),
        refreshable=False
    ):
        """
        Initialize the FutureBuilder and prepare for async execution.

        Args:
            future (Callable): The async operation to execute.
            on_loading (Callable): Function to handle the loading state.
            on_data (Callable): Function to handle the completed state.
            on_error (Callable): Function to handle the error state.
        """
        super().__init__()
        self.future = future
        self.on_loading = on_loading
        self.on_data = on_data
        self.on_error = on_error
        self.content = self.on_loading()
        self._task = None
        self.refreshable=refreshable

    def did_mount(self):
        """Start the async task when the widget is mounted."""
        self._task = self.page.run_task(self.execute_task)

    def will_unmount(self):
        """Cancel the async task when the widget is unmounted."""
        if self._task and not self._task.done():
            self._task.cancel()
            
    def refresh(self):
      if self.refreshable:  
        self.content=self.on_loading()
        self.update()
        """Refresh the FutureBuilder by re-executing the task."""
        if self._task and not self._task.done():
            self._task.cancel()
        self._task = self.page.run_task(self.execute_task)        

    async def execute_task(self):
        """Execute the async task and update UI accordingly."""
        try:
            # Await the future (async function)
            if iscoroutinefunction(self.future):
                result = await self.future()
            else:
                result = self.future()
            self.content = self.on_data(Snapshot("completed", data=result))
        except Exception as e:
            self.content = self.on_error(Snapshot("error", error=str(e)))
        finally:
            if not self.refreshable:  
               del self._task
            self.update()


import flet as ft
import time
def fetch_data_async():
    """Simulate an async data-fetching operation."""
    time.sleep(2)
    return 'opnion' # Simulate delay

def main(page: ft.Page):
    page.title = "FutureBuilder Widget Example"
    page.scroll = "adaptive"

    # Create a FutureBuilder widget
    #supports both sync/async functions
    future_widget = FutureBuilder(
        future=fetch_data_async,
        on_data=lambda snapshot: ft.Text(f"Data loaded: {snapshot.data}"),
        on_error=lambda e: ft.Text('data ki chud chuki hai'),
        refreshable=True


    )


    page.add(future_widget,ft.ElevatedButton('refresh',on_click=lambda e : future_widget.refresh() ))


if __name__ == "__main__":


    import asyncio
    ft.app(target=main)
