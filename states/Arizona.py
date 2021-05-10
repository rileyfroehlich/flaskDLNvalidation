def Arizona_is_valid(dln, DOB, expiration_date, eyes, hair, height, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [8, 5]
    sex_X = False
    hair = hair
    issue_date = False
    state = "AZ"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, extra=extra)


if ( __name__ == "__main__" ):
    print(Alaska_is_valid("123456789", "01-01-2000", "02-04-2028", "BRO", "BRO", '5-11', 'M', '170'))

"""
60f
Summary Comment for Alaska:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    hair color is the actual abbreviations, and
    expiration_length is 8 years
    For investigations: if the user is over 65, then the
    license expires every 5 years
f06
"""
