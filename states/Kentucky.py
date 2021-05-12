def kentucky_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [8]
    sex_X = False
    hair = False
    issue_date = issue_date
    state = "KY"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)

"""
60f
Summary Comment for Kentucky:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    hair = False, and expiration_length is 8 years.
f06
"""
