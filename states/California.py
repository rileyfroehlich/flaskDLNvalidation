def Califonia_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [5]
    sex_X = True
    hair = hair
    issue_date = issue_date
    state = "CA"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)


if ( __name__ == "__main__" ):
    print(Califonia_is_valid("123456789", "01-01-2000", "02-04-2026", "BRO", "BRO", '5-11', "02-04-2020",'M', '160'))

"""
60f
Summary Comment for California:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = True,
    with hair, and expiration_length is 5 years
f06
"""
