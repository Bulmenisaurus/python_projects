import json
import requests
import sys

if sys.argv[0] != 'python':
    class Colors:
        PURPL = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[32m'
        YELLO = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
else:
    class Colors:
        PURPL = ''
        BLUE = ''
        GREEN = ''
        YELLO = ''
        RED = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

if sys.argv[0] != 'python':
    def get_color_escape(r, g, b, background=False):
        # from https://stackoverflow.com/a/45782972
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b) + '\033[0m'
else:
    def get_color_escape(*args):
        return ''


def clr_from_hex(hexclr: str) -> dict:
    color_url = "https://colornames.org/search/json/?hex=" + hexclr.strip("#")
    json_data = requests.get(color_url).text
    color = json.loads(json_data)
    return color


def fresh_colors() -> list:
    color_url = "https://colornames.org/fresh/json/"
    json_data = requests.get(color_url).text
    colors = json.loads(json_data)
    return colors


def format_clr(clr: dict) -> str:
    rgb = tuple(int(clr['hexCode'][i:i + 2], 16) for i in (0, 2, 4))
    color = get_color_escape(*rgb) + clr['hexCode']

    formatstring = (clr['name'],  # name of color, such as `red`
                    color,  # hex code of color, such as `#ff0000`
                    ("ID: " if 'nameId' in clr else '') + str(clr.get('nameId')))  # id of color, such as `ID: 1`

    formatted_clr = "{}: #{}\n{}\n".format(*formatstring)
    return formatted_clr


print(f"""\nWould you like to:
 {Colors.PURPL}[0]{Colors.ENDC} 100 FRESHEST colors
 {Colors.BLUE}[1]{Colors.ENDC} See the name of a specific color (1/16 chance it exists)
 {Colors.GREEN}[2]{Colors.ENDC} raw data of 100 freshest colors
 {Colors.YELLO}[3]{Colors.ENDC} raw data of specific color""")

choice = input()

if choice == '0':
    # list of 100 formatted colors
    print(''.join([format_clr(x) for x in fresh_colors()]))
elif choice == '1':
    # see spe
    hex_clr = clr_from_hex(input("What hexadecimal color would you like to view?"))
    print(format_clr(hex_clr))
elif choice == '2':
    ''
elif choice == '3':
    ''
else:
    print("Not a valid option :(")
