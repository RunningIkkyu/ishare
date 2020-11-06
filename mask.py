import tkinter as tk
import time

class MouseIntercepter:
    def __init__(self):
        self.window = tk.Tk()

        # Start mouse intercepter fullscreen.
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False

        # Bind exit key.
        # self.window.bind("<F11>", self.toggle_full_screen)
        # self.window.bind("<Escape>", self.quit_full_screen)

        # Record current screen size, used to detect border.
        self.window_width = 1439
        self.window_height = 899

        # DEBUG
        self.label = tk.Label(text="Hello")
        self.label2 = tk.Label(text="World")
        self.label.pack()
        self.label2.pack()

        # Set window to transparent, let it be invisible.
        self.set_transparent_value(0.9)
        # Hide cursor.
        self.window.config(cursor="none")
        self.window.mainloop()

    def show(self):
        self.window.update()
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()

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

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        # self.window.attributes("-fullscreen", self.fullScreenState)
        # self.window.state('zoomed')
        self.window.attributes("-fullscreen", self.fullScreenState)


    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = MouseIntercepter()
    print('a')
    time.sleep(2)
    app.hide()
    time.sleep(2)
    app.show()
