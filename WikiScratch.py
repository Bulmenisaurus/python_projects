def eval_input(variables_list, to_eval, type_code):
    if type_code in ('int', 'float'):  # shouldn't evaluate the string fo the name of the variable
        for var in variables_list:
            if var in to_eval:
                to_eval = to_eval.replace(var, variables_list[var])
        return eval(to_eval)
    else:
        return '\"' + str(to_eval) + '\"'






def compile_(input_):
    """Compile code by lexifying it"""
    code = input_.split('\n')
    variables_list = {}
    for (count, i) in enumerate(code):
        try:
            line = i.strip().split(' ')
            if substs(line, ['set', 'to']):
                if i[-1] == ')':
                    value = eval_input(variables_list, line[-1], 'int')
                    line = f"{line[1]} = {value}"
                    variables_list[line[1]] = value
                elif i[-1] == ']':
                    line = f"{line[1]} = \'{eval(line[-1])[0]}\'"
            elif substs(line, ['change', 'by']):
                if i[-1] == ')':  # since you can only add numbers in scratch
                    line = f"{line[1]} += {int(eval(line[-1]))}"
            elif substs(line, ['say']):
                if i[-1] == ')':
                    line = f"print({int(eval(line[-1]))})"
                elif i[-1] == ']':
                    line = f"print(\'{str(line[-1])}\')"

            else:
                error(count, 'Syntax')
            print(line)
        except:
            error(count, 'Compile')


def error(error_line, type):  # for errors of all types
        print(f"\033[91mBeep boop line {error_line} sucks! ({type} error)\033[0m")


def substs(st, subst):
    for y in subst:
        if not y in st:
            return False
    return True



while True:
    x = input('Your code?\n')
    compile_(x)
