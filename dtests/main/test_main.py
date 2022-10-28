from src.derivHelpers import derivative
def run_assertions(condition, field, expected, actual, test_name, funct_value=None):
    assert condition, f'Expected {field}: {expected}, actual: {actual}'
    print(f'{test_name} with value {funct_value} has passed.')


def test_sequence_returns(function, length):
    split_function = derivative.return_derivation_values(function)[0]
    run_assertions(len(split_function) == length, 'Length', length, len(split_function), 'test_sequence_returns', function)

def test_sequence_returns_enums(function, actual):
    result = derivative.return_derivation_values(function)[1]
    run_assertions(len(result) == len(actual), 'ENUMS', len(actual), len(result), 'test_sequence_returns_enums', actual)


def run_tests(values):
    for i in values:
        print(f'Testing {i[0]} ... ')
        test_sequence_returns(i[0], i[1])
        test_sequence_returns_enums(i[0], i[2])
        print('\n')
    return True