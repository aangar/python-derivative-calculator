import os
from time import sleep
from derivHelpers import derivative
from DerivEnums import SymbolEnums as se
from derivtests import test_main as dtest
LINEAR_TEST = '3x+2'
BINOMIAL_POSITIVE_TEST = 'x^2+2x^2-3'
TRINOMIAL_POS_TEST = '4x^4+3x^3-2x^2-4'

if __name__ == '__main__':
    test_list_static = list()
    test_list_static.append((LINEAR_TEST, 2, [se.SymbolEnums.PLUS]))
    test_list_static.append((BINOMIAL_POSITIVE_TEST, 3, [se.SymbolEnums.PLUS, se.SymbolEnums.MINUS]))
    test_list_static.append((TRINOMIAL_POS_TEST, 4, [se.SymbolEnums.PLUS, se.SymbolEnums.MINUS, se.SymbolEnums.MINUS]))
    if (dtest.run_tests(test_list_static)):
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
        linear_t1 = derivative.return_derivation_values(LINEAR_TEST)
        print(linear_t1[0])
        binomial_t1 = derivative.return_derivation_values(BINOMIAL_POSITIVE_TEST)
        print(binomial_t1[1])