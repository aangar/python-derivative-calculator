from derivHelpers import derivative
LINEAR_TEST = '3x+2'
BINOMIAL_POSITIVE_TEST = 'x^2+2x2-3'
TRINOMIAL_POS_TEST = '4x^4+3x^3-2x^2-4'

if __name__ == '__main__':
    linear_t1 = derivative.return_derivation_values(LINEAR_TEST)
    print(linear_t1[0])
    binomial_t1 = derivative.return_derivation_values(BINOMIAL_POSITIVE_TEST)
    print(binomial_t1[1])