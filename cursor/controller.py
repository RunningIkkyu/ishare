from pynput.mouse import Button, Controller

class Cursor():
    """Cursor class"""
    def __init__(self):
        self.screen_number = 0
        self.x = 0
        self.y = 0
        self.mouse = Controller()

    def move_to(self, x, y):
        self.mouse.position = (x, y)

    def press(self):
        self.mouse.press(Button.Left)

    def release(self):
        self.mouse.release(Button.Right)

    def double_click(self):
        self.mouse.click(Button.left, 2)


if __name__ == "__main__":
    c = Cursor()
    c.move_to(100,100)
