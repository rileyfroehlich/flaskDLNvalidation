def Kansas_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [6]
    sex_X = False
    hair = False
    issue_date = issue_date
    state = "KS"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)


if ( __name__ == "__main__" ):
    print(Kansas_is_valid("123456789", "01-01-2000", "02-04-2025", "BRO", '5-11', "02-04-2020",'M', '160'))

"""
60f
Summary Comment for Kansas:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    hair = False, and expiration_length is 6 years.
f06
"""
