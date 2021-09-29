try:
    var = 100

    assert var == 100 # -> True
    assert var == 200, 'Expected 200' # -> False - Throw AssertionError
except AssertionError as error:
    print(">>> Assertion Error: \n" + str(error))