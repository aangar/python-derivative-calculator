import os
import sys
from time import sleep
from src.derivHelpers import derivative
from src.DerivEnums import SymbolEnums as se
from dtests.main import test_main as dtest
from src.functionInterpretation import main as funcInt
LINEAR_TEST = '3x+2'
NON_VARIABLE = '22+12'
BINOMIAL_POSITIVE_TEST = 'x^2+2x^2-3'
TRINOMIAL_POS_TEST = '4x^4+3x^3-2x^2-4'

if __name__ == '__main__':
    if not sys.argv[1] == '-nt':
        test_list_static = list()
        test_list_static.append((LINEAR_TEST, 2, [se.SymbolEnums.PLUS]))
        test_list_static.append((BINOMIAL_POSITIVE_TEST, 3, [se.SymbolEnums.PLUS, se.SymbolEnums.MINUS]))
        test_list_static.append((TRINOMIAL_POS_TEST, 4, [se.SymbolEnums.PLUS, se.SymbolEnums.MINUS, se.SymbolEnums.MINUS]))
        if dtest.run_tests(test_list_static):
            print('Clearing test output in five seconds', end =' ', flush=True)
            sleep(0.25)
            print('.', end ='', flush=True)
            sleep(0.25)
            print('.', end ='', flush=True)
            sleep(0.25)
            print('.', end ='', flush=True)
            sleep(5)
            clear_val = 'clear' if os.name == 'posix' else 'clear'
            os.system(clear_val)
    else:
        # linear_t1 = derivative.return_derivation_values(LINEAR_TEST)
        # print(linear_t1[0])
        # binomial_t1 = derivative.return_derivation_values(BINOMIAL_POSITIVE_TEST)
        # print(binomial_t1[1])
        funcInt.interpret_function('3((x+2)^2)')