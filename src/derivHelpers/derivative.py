from src.DerivEnums import SymbolEnums as SE
def convert_to_enum_list(sequence):
    """
    Converts a sequence of characters into enums of the function.

    :param sequence: the string to interpret into a list of enums.
    :return: a list of the interpreted enums.
    """
    if not len(sequence) > 0:
        print('Cannot convert an empty sequence.')
        return None
    enums = list()
    for i in sequence:
        enums.append(SE.SymbolEnums.determine_character(i))
    return enums

def return_derivation_values(sequence):
    """
    Parses the inputted function and returns the values to differentiate.

    :param seqeunce: the string representation of the function to derive.
    :return: a tuple containing two values. First being a list of the values to
    differentiate, the second being the operators that were removed.
    """
    enumMap = convert_to_enum_list(sequence)
    if not type(enumMap) == list and len(enumMap) < 1:
        print('Either list is not a list or list is lt 1!')
    positions = [-1]
    operators = list()
    for i in range(len(enumMap)):
        val = enumMap[i]
        conditional = val == SE.SymbolEnums.PLUS or val == SE.SymbolEnums.MINUS
        if conditional:
            operators.append(val)
            positions.append(i)
    values = list()
    for i in range(1, len(positions)):
        values.append(sequence[positions[i - 1] + 1:positions[i]])
    values.append(sequence[positions[len(positions) - 1] + 1: len(sequence)])
    return (values, operators)