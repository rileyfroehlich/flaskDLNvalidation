def new_york_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [8]
    sex_X = False
    hair = False
    issue_date = issue_date
    state = "NY"
    result = generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)
    return result


if ( __name__ == "__main__" ):
    print(new_york_is_valid("1234567", "01-01-2000", "02-04-2025", "BRO", "BRO", '5-11', "02-04-2020",'M', '160'))

"""
60f
Summary Comment for New York:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    with hair, and expiration_length is 8 years
f06
"""