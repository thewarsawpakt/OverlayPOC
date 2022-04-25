import time
import pygame
import win32con
import win32gui
import keyboard

WIN_SIZE = (400, 400)
WIN_TITLE = "Window Overlay POC"
currently_hidden = False

pygame.init()
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption(WIN_TITLE)


def window_handler(hwnd, *args):
    if win32gui.IsWindowVisible(hwnd):
        if WIN_TITLE in win32gui.GetWindowText(hwnd):
            if currently_hidden:
                _ = win32con.HWND_BOTTOM
            else:
                _ = win32con.HWND_TOPMOST
            win32gui.SetWindowPos(hwnd, _, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def main():
    global currently_hidden
    time_since_last_change = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        win32gui.EnumWindows(window_handler, None)
        if keyboard.is_pressed("k"):
            if time_since_last_change < time.time_ns() - 250000000:
                currently_hidden = not currently_hidden
                time_since_last_change = time.time_ns()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
