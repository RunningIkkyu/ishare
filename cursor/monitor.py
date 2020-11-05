from pynput import mouse
from controller import Cursor
from cursor_common import *
import time


class CursorMonitorBase():
    """ Cursor Monitor """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 1920
        self.height = 1080
        self.screen_number = 0
        self.listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)

    def switch_screen(self):
        pass

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        # if not pressed:
            # # Stop listener
            # return False

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

    def on_move(self, x, y):
        # self.x, self.y = x, y
        print(x, y)
        border = self.reach_border(x, y)
        if border:
            print(f'reach border: {border}')

    def reach_border(self, x, y, delta=1.1):
        """ """
        if x <= 0 + delta:
            return BORDOR_LEFT
        if y <= 0 + delta:
            return BORDOR_TOP
        if x >= self.width - delta:
            return BORDOR_RIGHT
        if y >= self.height - delta:
            return BORDOR_BOTTOM


    def get_screen_size(self):
        width, height = 1440, 900
        return width, height

    def start_listener(self):
        self.listener.start()

    def stop_listener(self):
        self.listener.stop()


if __name__ == "__main__":
    cursor_monitor = CursorMonitorBase()
    cursor_monitor.start_listener()

