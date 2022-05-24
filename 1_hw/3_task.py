import string
import timeit

letters = string.ascii_lowercase
numbers = '0123456789'


def addCheckRemove(test_key, added_sym, _key):
    test_key += added_sym
    if test_key == _key:
        print('YES')
        statement = True
    else:
        statement = False
        test_key = test_key[:-1]
    return test_key, statement


def findKey(example_key_8_bit='0xcf'):
    main_key_start = "0x"

    statement = False

    for num in numbers:
        test_key = main_key_start + num
        for num_1 in numbers:
            test_key, statement = addCheckRemove(test_key, num_1, example_key_8_bit)
            if statement: break
        else:
            for let_1 in letters:
                test_key, statement = addCheckRemove(test_key, let_1, example_key_8_bit)
                if statement: break

    if not statement:
        for let in letters:
            test_key = main_key_start + let
            for num_1 in numbers:
                test_key, statement = addCheckRemove(test_key, num_1, example_key_8_bit)
                if statement: break
            else:
                for let_1 in letters:
                    test_key, statement = addCheckRemove(test_key, let_1, example_key_8_bit)
                    if statement: break


if __name__ == '__main__':
    print("Average time function: ", timeit.timeit(findKey, number=10))
