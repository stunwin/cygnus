print("Starting...")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide
keyboard = KMKKeyboard()


keyboard.col_pins = (
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    )
keyboard.row_pins = (
    board.GP27,
    board.GP26,
    board.GP15,
    board.GP14,
    )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(use_pio=True, split_side=SplitSide.LEFT, data_pin = board.GP0)

keyboard.coord_mapping = [
    0,  1,  2,  3,  4,  5,  29, 28, 27, 26, 25, 24,
    6,  7,  8,  9, 10, 11,  35, 34, 33, 32, 31, 30,
    12, 13, 14, 15, 16, 17,  41, 40, 39, 38, 37, 36,
                18, 19, 20,  47, 46, 45,
]
layers = Layers()

keyboard.modules =[layers, split]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
        [
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,
                                            KC.LGUI,   _______,  KC.LCTRL,     KC.SPACE,   _______,  KC.RALT,
        ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
