import logging
import time
import sys
from typing import Callable, Final

import keyboard
import pynput
import pygetwindow
import pywinctl
from returns.maybe import Maybe, Nothing, Some

class GolfBattleEmulator:
    emulator: pywinctl.Window

    def __init__(self, golf_battle_window: pywinctl.Window):
        self.emulator = golf_battle_window

class MainGolfBattleEmulator(GolfBattleEmulator):
    def __init__(self, golf_battle_window: pywinctl.Window):
        super().__init__(golf_battle_window)

def find_window_titles_with_prefix(prefix: str) -> list[str]:
    titles: list[str] = pygetwindow.getAllTitles()
    logging.debug(f"WINDOW TITLES: {titles}")
    starts_with_title: Callable[[str], bool] = lambda title: title.startswith(prefix)

    return list(filter(starts_with_title, titles))

def window_title_to_window(title: str) -> pywinctl.Window:
    return pywinctl.getWindowsWithTitle(title)[0]

def find_window_from_windows(windows: list[pywinctl.Window], title: str) -> Maybe[pywinctl.Window]:
    return next(Some(window for window in windows if window.title == title), Nothing)

def screenshot_windows(windows: list[pywinctl.Window], screenshot_key: str, pause: float):
    for window in windows:
        window.activate()
        time.sleep(pause)
        keyboard.press_and_release(screenshot_key)
        time.sleep(pause)

def screenshot():
    emulator_titles: list[str] = find_window_titles_with_prefix("KakaoTalk")
    emulator_windows: list[pywinctl.Window] = list(map(window_title_to_window, emulator_titles))
    # emulators: list[GolfBattleEmulator] = map(lambda window: GolfBattleEmulator(window), emulator_windows)

def handle_darwin(hotkey: str, callback: Callable[[], None]):
    with pynput.keyboard.GlobalHotKeys({ hotkey: callback }) as listener:
        listener.join()

def handle_windows(hotkey: str, callback: Callable[[], None]):
    keyboard.add_hotkey(hotkey, callback)
    keyboard.wait()

def logger_setup():
    logging.basicConfig(level=logging.DEBUG)

def main():
    DARWIN_HOTKEY: Final[str] = "<ctrl>+g"
    WINDOWS_HOTKEY: Final[str] = "ctrl+g"

    logger_setup()

    match sys.platform:
        case "darwin":
            handle_darwin(DARWIN_HOTKEY, screenshot)
        case "win32":
            handle_darwin(WINDOWS_HOTKEY, screenshot)
        case _:
            raise RuntimeError("ERROR: os not supported")

main()
