import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

keyboard.keymap = [
    [
        KC.Macro(Press(KC.LCTRL), Tap(KC.A), Release(KC.LCTRL)),
        KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),
        KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
        KC.Macro(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL)),
    ]
]

if __name__ == '__main__':
    keyboard.go()
