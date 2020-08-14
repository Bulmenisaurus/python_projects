# Shortening Messages Using Random Unicode
# Bold is \033[1m
smuru_guide = {
    "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "ɶ",
    "pi": "π", "ww": 'ʬ', "ts": "ʦ", "dz": "ʥ",
    "ue": "ᵫ", "ffi": "ﬃ", "ll": "‖", "oo": "ꚙ",
    "sm": "℠", "SM": "℠", "TEL": "℡", "tel": "℡",
    "No": "№", "N0": "№", "NO": "№", "ac": "℀",
    "KK": "㏍", "AS": "⅍", "KB": "㎅","MB": "㎆",
    "GB": "㎇", "cal": "㎈", "da": "㍲", "in": "㏌",
    "th": "ᵺ", "ng": "🆖", "NG": "🆖"

}


def smuru(smuru_input):
    smurufied = str(smuru_input)
    for x in smurufied:
        if x in str(smurufied):
            smurufied = smurufied.replace(x, smuru_guide[x])

    return smuru_input


print(smuru(input()))