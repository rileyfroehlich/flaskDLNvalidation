def florida_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [6,8]
    sex_X = False
    hair = False
    issue_date = issue_date
    state = "FL"
    result = generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)
    return result

"""
60f
Summary Comment for Florida:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    with hair, and expiration_length is 6 (80+) or 8 years
f06
"""