def Maine_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [6]
    sex_X = True
    hair = hair
    issue_date = issue_date
    state = "ME"
    result = generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)
    if ( (not result) and (len(dln) == 8) ):
        #exception()
        pass
    return result


if ( __name__ == "__main__" ):
    print(Maine_is_valid("1234567", "01-01-2000", "02-04-2025", "BRO", "BRO", '5-11', "02-04-2020",'M', '160'))

"""
60f
Summary Comment for Maine:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    with hair, and expiration_length is 6 years.
    Note: dlnvalidation may be incorrect on this, so if
    there are lots of errors which come from Maine, we would
    need to most likely create our own version of dlnvalidation.
    It uses 7 digits, while some sources say Maine uses 7-8 digits.
    Just in that case, I've put generic_State_is_valid() equal to
    a variable, and if it's false and the dln is 8 digits long, it
    still invalidates the licenses, but also calls the exception function
    I created a pull request and updated the dlnvalidation repo on May 8,
    2021.
f06
"""
