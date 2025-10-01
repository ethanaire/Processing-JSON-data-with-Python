import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        # Create a Canvas widget
        canvas = tk.Canvas(self)
        
        # Create a scrollbar for the canvas
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        # Create a regular Tkinter Frame to hold the content
        self.scrollable_frame = ttk.Frame(canvas)

        # Bind the frame's size changes to the canvas's scrollregion
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        # Put the scrollable frame inside the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Link the scrollbar to the canvas's view
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar into the outer ScrollableFrame
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill=tk.BOTH)

    def destroy(self):
        # Clean up resources when the ScrollableFrame is destroyed
        scrollbar.destroy()
        canvas.destroy()