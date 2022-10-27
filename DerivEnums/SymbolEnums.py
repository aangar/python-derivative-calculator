from enum import Enum

class SymbolEnums(Enum):
    """
    A class to enumerate every character in a function.
    """
    LETTER = 'character'
    NUMBER = 'number'
    LEFT_PARENTHESIS = 'leftParenthesis'
    RIGHT_PARENTHESIS = 'rightParenthesis'
    CARAT = 'carat'
    PLUS = 'plus'
    MINUS = 'minus'
    DIVIDE = 'divide'
    MULTIPLY = 'multiply'
    def determine_character(char):
        """
        Determines the ENUM value using the passed character.

        :param char: a character to be interpreted.
        :return: an ENUM of the according character.
        """
        decimal = ord(char.lower())
        if decimal > 47 and decimal < 58:
            return SymbolEnums.NUMBER
        elif decimal > 96 and decimal < 123:
            return SymbolEnums.LETTER
        elif decimal == 40:
            return SymbolEnums.LEFT_PARENTHESIS
        elif decimal == 41:
            return SymbolEnums.RIGHT_PARENTHESIS
        elif decimal == 94:
            return SymbolEnums.CARAT
        elif decimal == 43:
            return SymbolEnums.PLUS
        elif decimal == 45:
            return SymbolEnums.MINUS
        elif decimal == 47:
            return SymbolEnums.DIVIDE
        elif decimal == 42:
            return SymbolEnums.MULTIPLY
        return None