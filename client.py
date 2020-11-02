# This demo shows how to create a transparent window in Linux, tested with
# Gnome5 on Arch.

# Refs About Fullscreen
# https://stackoverflow.com/questions/58157159/making-a-fullscreen-paint-program-with-transparent-background-of-my-application https://stackoverflow.com/questions/48837909/tkinter-transparent-background-linux https://stackoverflow.com/questions/18394597/is-there-a-way-to-create-transparent-windows-with-tkinter/18430628

# Import module
from tkinter import *
# Create object
root = Tk()
# Adjust size
TK_SILENCE_DEPRECATION=1
root.geometry("400x400")
# Create transparent window
root.wait_visibility(root)
root.attributes('-alpha',0)
# root.overrideredirect(False)
root.attributes("-fullscreen", True)
# root.wm_attributes("-topmost", 1)
# Execute tkinter
root.mainloop()
