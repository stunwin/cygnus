// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "quantum.h"
#include "features/achordion.h"

// Layer definitions
enum layers {
    _BASE,
    _NAVSYM,
    _NUMFN
};

// Homerow mods
#define HM_A LGUI_T(KC_A)
#define HM_S LALT_T(KC_S)
#define HM_D LCTL_T(KC_D)
#define HM_F LSFT_T(KC_F)
#define HM_J RSFT_T(KC_J)
#define HM_K RCTL_T(KC_K)
#define HM_L RALT_T(KC_L)
#define HM_SCLN RGUI_T(KC_SCLN)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* Base Layer (_BASE):
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │Tab│ Q │ W │ E │ R │ T │       │ Y │ U │ I │ O │ P │Bsp│
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │ \ │⌘/A│⌥/S│⌃/D│⇧/F│ G │       │ H │⇧/J│⌃/K│⌥/L│⌘/;│ ' │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │Sft│ Z │ X │ C │ V │ B │       │ N │ M │ , │ . │ / │Ent│
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───┘
     *                 ┌───┬───┬───┐   ┌───┬───┬───┐
     *                 │GUI│Num│Ctl│   │Spc│Nav│⌥/-│
     *                 └───┴───┴───┘   └───┴───┴───┘
     */
    [_BASE] = LAYOUT(
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,                         KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_BSPC,
        KC_BSLS, HM_A,    HM_S,    HM_D,    HM_F,    KC_G,                         KC_H,    HM_J,    HM_K,    HM_L,    HM_SCLN, KC_QUOT,
        KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,                         KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_ENT,
                                            KC_LGUI, MO(_NUMFN), KC_LCTL,    KC_SPC, MO(_NAVSYM), LALT_T(KC_MINS)
    ),

    /* Nav/Symbol Layer (_NAVSYM):
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │Esc│ ! │ @ │ # │ $ │ % │       │Hom│PgD│PgU│End│   │Del│
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │   │ ^ │ & │ * │ ( │ ) │       │ ← │ ↓ │ ↑ │ → │   │   │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │   │ ` │ = │ - │ [ │ ] │       │   │   │   │   │   │   │
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───┘
     *                 ┌───┬───┬───┐   ┌───┬───┬───┐
     *                 │   │Alt│   │   │   │   │Alt│
     *                 └───┴───┴───┘   └───┴───┴───┘
     */
    [_NAVSYM] = LAYOUT(
        KC_ESC,  KC_EXLM, KC_AT,   KC_HASH, KC_DLR,  KC_PERC,                      KC_HOME, KC_PGDN, KC_PGUP, KC_END,  KC_NO,   KC_DEL,
        _______, KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN,                      KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, KC_NO,   KC_NO,
        _______, KC_GRV,  KC_EQL,  KC_MINS, KC_LBRC, KC_RBRC,                      DT_UP,   DT_DOWN, DT_PRNT, KC_NO,   KC_NO,   _______,
                                            _______, KC_LALT,  _______,      _______, _______, KC_RALT
    ),

    /* Numpad/Function Layer (_NUMFN):
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │Tab│F1 │F2 │F3 │F4 │F5 │       │ + │ 7 │ 8 │ 9 │ P │Bsp│
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │Ctl│F6 │F7 │F8 │F9 │F10│       │ - │ 4 │ 5 │ 6 │   │   │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │Sft│F11│F12│VoD│VoU│Mut│       │ 0 │ 1 │ 2 │ 3 │   │   │
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───┘
     *                 ┌───┬───┬───┐   ┌───┬───┬───┐
     *                 │Alt│   │Ctl│   │ . │ * │ / │
     *                 └───┴───┴───┘   └───┴───┴───┘
     */
    [_NUMFN] = LAYOUT(
        KC_TAB,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,                        KC_PLUS, KC_7,    KC_8,    KC_9,    KC_P,    KC_BSPC,
        KC_LCTL, KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,                       KC_MINS, KC_4,    KC_5,    KC_6,    KC_NO,   KC_NO,
        KC_LSFT, KC_F11,  KC_F12,  KC_VOLD, KC_VOLU, KC_MUTE,                      KC_0,    KC_1,    KC_2,    KC_3,    KC_NO,   _______,
                                            KC_LALT, _______, KC_LCTL,       KC_DOT,  KC_ASTR, KC_SLSH
    )
};
bool process_record_user(uint16_t keycode, keyrecord_t* record) {
if (!process_achordion(keycode, record)) {return false;}

    return true;

}

void housekeeping_task_user(void) {
  achordion_task();
}

uint16_t get_tapping_term(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case HM_S:
            return 300;
        case HM_L:
            return 300;
        default:
            return TAPPING_TERM;
    }
}

