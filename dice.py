d1, d2 = "|⚬     ⚬|", "|       |"
d3, d4 = "|   ⚬   |", "|      ⚬|"
dice_list = [
    f"{d2}\n{d3}\n{d2}",
    f"{d4[::-1]}\n{d2}\n{d4}",
    f"{d4}\n{d3}\n{d4[::-1]}",
    f"{d1}\n{d2}\n{d1}",
    f"{d1}\n{d3}\n{d1}",
    f"{d1} \n{d1} \n{d1}"]


def prnt_dice(num):
    print(" "+"_"*7)
    print(dice_list[int(num)-1])
    print(" "+"‾"*7)
