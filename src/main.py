import time
from typing import Callable, Final
import keyboard
import pygetwindow

HOTKEY: Final[str] = "ctrl+g"

class WindowTitle:
    @staticmethod
    def starts_with(name: str) -> list[str]:
        titles: list[str] = pygetwindow.getAllTitles()
        starts_with_title: Callable[[str], bool] = lambda title: title.startswith(name)
        return list(filter(starts_with_title, titles))

    @staticmethod
    def to_windows(titles: list[str]) -> list[pygetwindow.Win32Window]:
        title_to_window: Callable[[str], pygetwindow.Win32Window] = lambda title: pygetwindow.getWindowsWithTitle(title)[0]
        return list(map(title_to_window, titles))

def screenshot_windows(windows: list[pygetwindow.Win32Window], screenshot_key: str, pause: float):
    for window in windows:
        window.activate()
        time.sleep(pause)
        keyboard.press_and_release(screenshot_key)
        time.sleep(pause)

def screenshot():
    screenshot_windows(windows=WindowTitle.to_windows(WindowTitle.starts_with("MuMu Emu")), screenshot_key="F9", pause=1.0)

def main():
    keyboard.add_hotkey(HOTKEY, screenshot)
    keyboard.wait()

main()