# Shortening Messages Using Random Unicode
# Bold is \033[1m
smuru_guide = {
    "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "ɶ",
    "pi": "π", "ww": 'ʬ', "ts": "ʦ", "dz": "ʥ",
    "ue": "ᵫ", "ffi": "ﬃ", "ll": "‖"

}


def SMURU(smuru_input):
    smuru_input = str(smuru_input)
    for x in smuru_guide:
        if x in str(smuru_input):
            smuru_input = smuru_input.replace(x, smuru_guide[x])

    return smuru_input


print(SMURU(input()))