import time
from typing import Callable, Final
import keyboard
import pygetwindow
from pygetwindow import Win32Window

class GolfBattleEmulator:
    emulator: pygetwindow.Win32Window

    def __init__(self, golf_battle_window: Win32Window):
        self.emulator = golf_battle_window

class MainGolfBattleEmulator(GolfBattleEmulator):
    def __init__(self, golf_battle_window: Win32Window):
        super().__init__(golf_battle_window)
    
    def start_game(self):
        print(self.emulator.center)

def find_window_titles_with_prefix(prefix: str) -> list[str]:
    titles: list[str] = pygetwindow.getAllTitles()
    starts_with_title: Callable[[str], bool] = lambda title: title.startswith(prefix)
    return list(filter(starts_with_title, titles))

def window_titles_to_windows(titles: list[str]) -> list[Win32Window]:
    title_to_window: Callable[[str], Win32Window] = lambda title: pygetwindow.getWindowsWithTitle(title)[0]
    return list(map(title_to_window, titles))
    
def find_window_from_windows(windows: list[Win32Window], title: str) -> Win32Window:
    return next(window for window in windows if window.title == title)

def screenshot_windows(windows: list[Win32Window], screenshot_key: str, pause: float):
    for window in windows:
        window.activate()
        time.sleep(pause)
        keyboard.press_and_release(screenshot_key)
        time.sleep(pause)

def screenshot():
    emulator_titles: list[str] = find_window_titles_with_prefix("MuMu Emu")
    emulator_windows: list[Win32Window] = window_titles_to_windows(emulator_titles)
    main_window: Win32Window = find_window_from_windows(emulator_windows, "MuMu Emu 1")
    screenshot_windows(windows=emulator_windows, screenshot_key="F9", pause=0.5)
    # GolfBattle.start_game(main_window=main_window)

def main():
    HOTKEY: Final[str] = "ctrl+g"

    keyboard.add_hotkey(HOTKEY, screenshot)
    keyboard.wait()

main()