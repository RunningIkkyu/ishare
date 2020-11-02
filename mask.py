import tkinter as tk
import autopy

class MouseIntercepter:
    def __init__(self):
        self.window = tk.Tk()

        # Start mouse intercepter fullscreen.
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False

        # Bind exit key.
        self.window.bind("<F11>", self.toggle_full_screen)
        self.window.bind("<Escape>", self.quit_full_screen)
        self.window.bind("<Motion>", self.motion)

        # Record current screen size, used to detect border.
        self.window_width = 1439
        self.window_height = 899

        # DEBUG
        self.label = tk.Label(text="Hello")
        self.label2 = tk.Label(text="World")
        self.label.pack()
        self.label2.pack()

        # Set window to transparent, let it be invisible.
        self.set_transparent_value(0.1)
        # Hide cursor.
        self.window.config(cursor="none")

        self.window.mainloop()

    def set_transparent_value(self, transparent):
        """Set transparent of current window.

        Args:
            transparent (float, optional): transparent of the
            window, should in the range of [0, 1].
        """
        self.window.wait_visibility(self.window)
        # TODO: Self define the error.
        if transparent > 1 or transparent < 0:
            raise Exception("Error: transparent should in the range of [0, 1].")
        self.window.attributes('-alpha', transparent)

    def reset_mouse(self, x, y):
        """Keep mouse away from boarder

        Keep mouse away from border.

        Args:
            x (float): current mouse location x.
            y (float): current mouse location y.
        """
        margin = 100
        if x < margin:
            autopy.mouse.move(margin, y)
        if y < margin:
            autopy.mouse.move(x, margin)
        border_right = self.window_width - margin
        if x > border_right:
            autopy.mouse.move(border_right, y)
        border_down = self.window_height - margin
        if y > border_down:
            autopy.mouse.move(x, border_down)

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        # self.window.attributes("-fullscreen", self.fullScreenState)
        # self.window.state('zoomed')
        self.full_screen_toggle()

    def motion(self, event):
        """Handle mouse moving event.

        If mouse move:
            (1) update mouse location, make it away from border.
            (2) Send coor to client.


        Args:
            event (event): Mouse event.
        """
        x, y = event.x, event.y
        self.reset_mouse(x,y)
        # s = autopy.mouse.location()
        self.label.config(text="tk location: ({}, {})".format(x,y))
        # self.label2.config(text=f"mouse location: {s})")
        print(x, y)


    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = MouseIntercepter()
