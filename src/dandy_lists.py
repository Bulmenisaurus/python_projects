import types


class DandyList(list):
    def apply(self, rule):
        # if rule is a function like eval() or a custom one
        if isinstance(rule, (types.FunctionType, types.BuiltinFunctionType, type)):
            applied = DandyList([rule(x) for x in self])

        # if the rule is a string that needs to be formatted
        elif isinstance(rule, str):
            applied = DandyList([rule.format(x) for x in self])



def p_10(i):
    return i + 10


a = DandyList([1, 2, 3, 4, 5, 6, 7, 8, 9])
a.apply("{} + 2")
print(a)
