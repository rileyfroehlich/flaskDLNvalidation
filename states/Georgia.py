def Georgia_is_valid(dln, DOB, expiration_date, eyes, height, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [8]
    sex_X = False
    hair = False
    issue_date = False
    state = "GA"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)


if ( __name__ == "__main__" ):
    print(Georgia_is_valid("9999999", "01-01-2000", "02-04-2028", "BRO", '5-11', 'M', '170'))

"""
60f
Summary Comment for Georgia:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    hair = False, and expiration_length is 8 years
f06
"""
