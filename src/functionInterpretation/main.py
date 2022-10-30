from src.derivHelpers import derivative as deriv
from src.DerivEnums.SymbolEnums import SymbolEnums as Symbols
from src.DerivEnums.ValueWithEnum import ValueWithEnum as VWE

def find_parenthesis_indecies(enums):
        rparind = 0
        lparind = 0
        for ind in range(0, len(enums)):
            if enums[ind] == Symbols.LEFT_PARENTHESIS:
                lparind = ind
                break
        for ind in range(len(enums) - 1, -1, -1):
            if enums[ind] == Symbols.RIGHT_PARENTHESIS:
                rparind = ind
                break
        return (lparind + 1, rparind)


def format_parenthesis_quantity(enums, complete = []):
    inside_format = ''
    shallow = list()
    for i in enums:
        shallow.append(i)
    if Symbols.LEFT_PARENTHESIS in enums and Symbols.RIGHT_PARENTHESIS in enums:
        inds = find_parenthesis_indecies(enums)
        expr = ''
        for i in range(inds[0], inds[1]):
            expr += complete[i].value
        print(expr)
    offset = 0
    for ind in range(1, len(enums)):
        if enums[ind - 1] == Symbols.NUMBER and enums[ind] == Symbols.LEFT_PARENTHESIS:
            shallow.insert(ind + offset, Symbols.MULTIPLY)
            offset += 1
    return enums

def interpret_function(string, x_value=0):
    value_list = list()
    to_interpret = string.replace('x', str(x_value))
    for i in to_interpret:
        value_list.append(VWE(i, Symbols.determine_character(i)))
    complete_map =  deriv.convert_to_enum_list(to_interpret)
    if Symbols.LEFT_PARENTHESIS in complete_map and Symbols.RIGHT_PARENTHESIS in complete_map:
        format_parenthesis_quantity(complete_map, value_list)