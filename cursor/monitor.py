from pynput import mouse
from controller import Cursor
import time

track = []

class CursorMonitor():
    """ Cursor Monitor """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.screen_number = 0

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        # if not pressed:
            # # Stop listener
            # return False

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

    def on_move(self, x, y):
        self.x, self.y = x, y
        print(self.x, self.y)
        track.append((self.x, self.y))

    def reach_border(self, x, y):
        pass

    def get_screen_size(self):
        width, height = 1440, 900
        return width, height

    def start_listener(self):
        listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        listener.start()
        time.sleep(10)
        listener.stop()
        print ('------------------------------------------------------------------------')
        time.sleep(2)


if __name__ == "__main__":
    cursor_monitor = CursorMonitor()
    cursor_monitor.start_listener()
    c = Cursor()
    for i in track:
        c.move_to(*i)
        time.sleep(0.01)

