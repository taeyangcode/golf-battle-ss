import time
from typing import Callable, Final
import keyboard
import pygetwindow
from returns.maybe import Maybe, Nothing

HOTKEY: Final[str] = "ctrl+g"

class GolfBattle:
    @staticmethod
    def start_game(main_window: pygetwindow.Win32Window):
        print(main_window.box)

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
    
def window_from_windows(windows: list[pygetwindow.Win32Window], title: str) -> pygetwindow.Win32Window:
    return next(window for window in windows if window.title == title)

def screenshot_windows(windows: list[pygetwindow.Win32Window], screenshot_key: str, pause: float):
    for window in windows:
        window.activate()
        time.sleep(pause)
        keyboard.press_and_release(screenshot_key)
        time.sleep(pause)

def screenshot():
    emulator_windows: list[pygetwindow.Win32Window] = WindowTitle.to_windows(WindowTitle.starts_with("MuMu Emu"))
    main_window: pygetwindow.Win32Window = window_from_windows(emulator_windows, "MuMu Emu 1")
    screenshot_windows(windows=emulator_windows, screenshot_key="F9", pause=0.5)
    # GolfBattle.start_game(main_window=main_window)

def main():
    keyboard.add_hotkey(HOTKEY, screenshot)
    keyboard.wait()

main()