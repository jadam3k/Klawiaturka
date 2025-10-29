from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, MatrixScanner
from kmk.modules.rotary import RotaryEncoderModule
from kmk.extensions.media_keys import MediaKeys

import board
from kmk.modules.rotary import RotaryEncoder

keyboard = KMKKeyboard()


cols = [board.D4, board.D5, board.D6]
rows = [board.D11, board.D12, board.D13]

scanner = MatrixScanner(
    row_pins=rows,
    col_pins=cols,
    diode_orientation=DiodeOrientation.COL2ROW
)
keyboard.modules.append(scanner)


keyboard.extensions.append(MediaKeys())


encoder = RotaryEncoder(
    pins=(board.D3, board.D2),
    clockwise=MediaKeys.volume_up,
    counter_clockwise=MediaKeys.volume_down,
    button=board.D1,
    button_key=KC.ENTER 
)
keyboard.modules.append(encoder)


keyboard.keymap = [
    [
        [KC.A, KC.B, KC.C],    # ROW1
        [KC.D, KC.E, KC.F],    # ROW2
        [KC.G, KC.H, KC.I],    # ROW3
    ]
]

if __name__ == '__main__':
    keyboard.go()
