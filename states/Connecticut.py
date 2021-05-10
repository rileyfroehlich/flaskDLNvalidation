def Connecticut_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [2,8]
    sex_X = True
    hair = False
    issue_date = issue_date
    state = "CT"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)


if ( __name__ == "__main__" ):
    print(Connecticut_is_valid("123456789", "01-01-2000", "02-04-2026", "BRO", "BRO", '5-11', "02-04-2020",'M', '160'))

"""
60f
Summary Comment for Connecticut:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = True,
    with hair, and expiration_length is 2 (65+) or 8 years
f06
"""
