print("Starting...")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.combos import Combos, Chord
from kmk.modules.macros import Macros, Press
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()
##########

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
                21, 22, 23,  47, 46, 45,
]
layers = Layers()
combos = Combos()
macros = Macros()
holdtap = HoldTap()

holdtap.tap_time = 200

keyboard.modules =[layers, split, MediaKeys(), combos, macros, holdtap]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO
DASHALT = KC.HT(KC.MINS, KC.LALT)
MODA = KC.HT(KC.A, KC.LGUI, prefer_hold = False, tap_interrupted = True)
MODS = KC.HT(KC.S, KC.LALT, prefer_hold = False, tap_interrupted = True)
MODD = KC.HT(KC.D, KC.LCTRL, prefer_hold = False, tap_interrupted = True)
MODF = KC.HT(KC.F, KC.LSHIFT, prefer_hold = False, tap_interrupted = True)
MODJ = KC.HT(KC.J, KC.RSHIFT, prefer_hold = False, tap_interrupted = True)
MODK = KC.HT(KC.K, KC.RCTRL, prefer_hold = False, tap_interrupted = True)
MODL = KC.HT(KC.L, KC.RALT, prefer_hold = False, tap_interrupted = True)
MODSCLN = KC.HT(KC.SCLN, KC.RGUI, prefer_hold = False, tap_interrupted = True)


def toggle_drive(keyboard):
    print('toggling usb drive') #serial feedback
    import microcontroller
    if microcontroller.nvm[0] == 0:
        microcontroller.nvm[0] = 1
    else:
        microcontroller.nvm[0] = 0

ToggleDrive = KC.MACRO(toggle_drive, Press(KC.RESET))
    
combos.combos = [
   Chord((KC.TAB, KC.BSPC, KC.Y), ToggleDrive),   
   Chord((KC.E, KC.R, KC.T), KC.FD(3)),
   Chord((KC.Y, KC.U, KC.I), KC.FD(0))
]



keyboard.keymap = [ 
        [ #qwerty
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,
        KC.BSLS,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M,    KC.COMM, KC.DOT, KC.SLSH, KC.ENTER,
                                            KC.LGUI,   KC.MO(2),  KC.LCTRL,     KC.SPACE,   KC.MO(1),  DASHALT,
        ],
        [ #navsymbol
        KC.ESC,  KC.EXLM, KC.AT,   KC.HASH, KC.DLR, KC.PERC,                         KC.HOME, KC.PGDOWN, KC.PGUP, KC.END,  XXXXXXX,  KC.DEL,
        _______, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,                        KC.LEFT, KC.DOWN,   KC.UP,  KC.RIGHT, XXXXXXX, XXXXXXX,
        _______, KC.GRV,  KC.EQL,  KC.MINS, KC.LBRC, KC.RBRC,                        XXXXXXX, XXXXXXX,   XXXXXXX, XXXXXXX, XXXXXXX, _______,
                                            _______,   KC.LALT,  _______,     _______,   _______,  KC.RALT,
        ],
        [ #numpadFunc
        KC.TAB,    KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                    KC.PLUS,  KC.N7, KC.N8, KC.N9, KC.P,  KC.BSPC,
        KC.LCTL,   KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,                   KC.MINUS, KC.N4, KC.N5, KC.N6, XXXXXXX, XXXXXXX,
        KC.LSFT,   KC.F11,   KC.F12,   KC.VOLD,  KC.VOLU,  KC.MUTE,                  KC.N0,    KC.N1, KC.N2, KC.N3, XXXXXXX, _______,
                                            KC.LALT,   _______,  KC.LCTRL,     KC.DOT,   KC.ASTR,  KC.SLSH,
        ],
        [#homerow mod test
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,
        KC.BSLS,   MODA,    MODS,    MODD,    MODF,    KC.G,                         KC.H,    MODJ,    MODK,    MODL, MODSCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M,    KC.COMM, KC.DOT, KC.SLSH, KC.ENTER,
         ]                                  KC.LGUI,   KC.MO(2),  KC.LCTRL,      KC.SPACE,  KC.MO(1),  DASHALT,
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
