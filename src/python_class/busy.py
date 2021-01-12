import random
import string


def filename(code_extensions=('py', 'pym', 'cpp', 'jasm'),
             secondary_extensions=('min', 'obf', 'asset', 'v3'),
             asset_extensions=('js', 'jpeg', 'jpg', 'png', 'svg'),
             length_cap=False):

    name = ''.join([random.choice(string.hexdigits) for _ in range(30)])
    extensions = ''

    if random.choice([True, False]):
        if random.choice([True, False]):
            extensions = '.' + random.choice(secondary_extensions)  # add secondary extension if needed
        extensions += '.' + random.choice(code_extensions)
        if length_cap:
            return (name + extensions)[:length_cap]
        else:
            return name + extensions
    else:
        if length_cap:
            return (name + '.' + random.choice(asset_extensions))[:length_cap]
        else:
            return name + '.' + random.choice(asset_extensions)


print(filename())
