# cygnus

![cygnus](/images/keeb1.jpeg)

*A short description of the keyboard/project*

* Keyboard Maintainer: [steve unwin](https://github.com/stunwin)
* Hardware Supported: *The PCBs, controllers supported*
* Hardware Availability: *Links to where you can find this hardware*

Make example for this keyboard (after setting up your build environment):

    make cygnus:chordal

Flashing example for this keyboard:

    make cygnus:chordal:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 2 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Keycode in layout**: Press `R`+`T`+`Y`+`U` to trigger the `QK_BOOT` command

# Keymap Summary

### Base Layer (`_BASE`)

While this does techincally have a full set of home row mods enabled, I really only ever use shift, since I vastly prefer ctrl and gui on a thumb, and alt is really not a major part of my workflow. Still, we kind of have a belt-and-suspenders thing going on with lots of room for improvement and streamlining.

```
┌───────┬───────┬───────┬───────┬───────┬───────┐       ┌───────┬───────┬───────┬───────┬───────┬───────┐
│  Tab  │   Q   │   W   │   E   │   R   │   T   │       │   Y   │   U   │   I   │   O   │   P   │  Bspc │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│   \   │    A  │    S  │  ^/D  │  ⇧/F  │   G   │       │   H   │  ⇧/J  │  ^/K  │  L    │  Scln │   '   │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│  Sft  │   Z   │   X   │   C   │   V   │   B   │       │   N   │   M   │   ,   │   .   │   /   │  Ent  │
└───────┴───────┴───────┴───────┴───────┴───────┘       └───────┴───────┴───────┴───────┴───────┴───────┘
                        ┌───────┬───────┬───────┐   ┌───────┬───────┬───────┐
                        │  GUI  │  Num  │  Ctl  │   │  Spc  │  Nav  │  ⌥/-  │
                        └───────┴───────┴───────┘   └───────┴───────┴───────┘
```

### Nav/Symbol Layer (`_NAVSYM`)

The first two rows of symbols are just a standard keyboard row cut in half and stacked. This nicely puts the parenthesis at the end which forms a clean grouping with the brackets.

```
┌───────┬───────┬───────┬───────┬───────┬───────┐       ┌───────┬───────┬───────┬───────┬───────┬───────┐
│  Esc  │   !   │   @   │   #   │   $   │   %   │       │ Home  │ PgDn  │ PgUp  │  End  │       │  Del  │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│       │   ^   │   &   │   *   │   (   │   )   │       │   ←   │   ↓   │   ↑   │   →   │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│       │   `   │   =   │   -   │   [   │   ]   │       │  TUp  │  TDn  │  TPr  │       │       │       │
└───────┴───────┴───────┴───────┴───────┴───────┘       └───────┴───────┴───────┴───────┴───────┴───────┘
                        ┌───────┬───────┬───────┐   ┌───────┬───────┬───────┐
                        │       │  Alt  │       │   │       │       │   \   │
                        └───────┴───────┴───────┘   └───────┴───────┴───────┘
```

### Numpad/Function Layer (`_NUMFN`)

```
┌───────┬───────┬───────┬───────┬───────┬───────┐       ┌───────┬───────┬───────┬───────┬───────┬───────┐
│  Tab  │  F1   │  F2   │  F3   │  F4   │  F5   │       │   +   │   7   │   8   │   9   │   P   │  Bspc │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│  Ctl  │  F6   │  F7   │  F8   │  F9   │  F10  │       │   -   │   4   │   5   │   6   │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│  Sft  │  F11  │  F12  │  VoD  │  VoU  │  Mut  │       │   0   │   1   │   2   │   3   │       │       │
└───────┴───────┴───────┴───────┴───────┴───────┘       └───────┴───────┴───────┴───────┴───────┴───────┘
                        ┌───────┬───────┬───────┐   ┌───────┬───────┬───────┐
                        │  Alt  │       │  Ctl  │   │   .   │   *   │   /   │
                        └───────┴───────┴───────┘   └───────┴───────┴───────┘
```

### No Homerow Mods Layer (`_NOHRM`)

```
┌───────┬───────┬───────┬───────┬───────┬───────┐       ┌───────┬───────┬───────┬───────┬───────┬───────┐
│  Tab  │   Q   │   W   │   E   │   R   │   T   │       │   Y   │   U   │   I   │   O   │   P   │  Bspc │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│   \   │   A   │   S   │   D   │   F   │   G   │       │   H   │   J   │   K   │   L   │   ;   │   '   │
├───────┼───────┼───────┼───────┼───────┼───────┤       ├───────┼───────┼───────┼───────┼───────┼───────┤
│  Sft  │   Z   │   X   │   C   │   V   │   B   │       │   N   │   M   │   ,   │   .   │   /   │  Ent  │
└───────┴───────┴───────┴───────┴───────┴───────┘       └───────┴───────┴───────┴───────┴───────┴───────┘
                        ┌───────┬───────┬───────┐   ┌───────┬───────┬───────┐
                        │  GUI  │  Num  │  Ctl  │   │  Spc  │  Nav  │  ⌥/-  │
                        └───────┴───────┴───────┘   └───────┴───────┴───────┘
```

### Additional Features

This keymap includes several advanced QMK features to enhance functionality, including Homerow Mods, layer-switching combos, and other useful chords.

#### Homerow Mods

The base layer utilizes **Homerow Mods**, which allows dual-function keys on the home row. Tapping a key produces the standard character, while holding it down activates a modifier. This allows for comfortable access to modifiers without leaving the home row.

Like I said above, I'm not actually using all of these definitions in the current version of this keymap, but they're all defined in there for you to swap out if you want to try them.

| Key      | Tapped     | Held          |
| :------- | :--------- | :------------ |
| **A**        | `a`          | Left GUI (⌘)  |
| **S**        | `s`          | Left Alt (⌥)  |
| **D**        | `d`          | Left Control  |
| **F**        | `f`          | Left Shift    |
| **J**        | `j`          | Right Shift   |
| **K**        | `k`          | Right Control |
| **L**        | `l`          | Right Alt (⌥) |
| **;**        | `;`          | Right GUI (⌘) |

A custom tapping term of 300ms is set for the `S` and `L` keys to fine-tune their behavior.

#### Combos (Chords)

Combos, or chords, allow you to trigger an action by pressing multiple keys simultaneously.

| Keys Pressed Simultaneously | Action                               | Description                                                                 |
| :-------------------------- | :----------------------------------- | :-------------------------------------------------------------------------- |
| `Tab` + `Backspace`         | Switch to `_NOHRM` layer             | Disables the homerow mods for gaming or when you just ge sick of them.|
| `\` + `'`                   | Switch to `_BASE` layer              | Re-enables the homerow mods.                                                |
| `F` + `J`                   | Toggle Caps Word (`CW_TOGG`)         | Capitalizes the next word you type. good for, say, typing out qmk keycodes.  |
| `R` + `T` + `Y` + `U`       | Reboot to Bootloader (`QK_BOOT`)     | Puts the keyboard into bootloader mode for flashing new firmware.           |

```

