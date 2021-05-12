# Montana DLN Verification

# 1Alpha+8Numeric or 13Numeric or 9Numeric or 14Numeric
# https://ntsi.com/drivers-license-format/
# Example: A12345678 OR 0123456789123 / 123456789 / 01234567891234
# Possible solution: **(month of birth)***(  )****(year of birth)**( 41 )**(day of birth)
# Class-D Licenses Valid for 4-8 years / Typically expires on driver's Birthday

# https://dojmt.gov/driving/driver-licensing/
# Real ID –  Renewal, Replacement and Out of State Transfer
# Non-Real ID – Renewal, Replacement and Out of State Transfer

# Required Docs:
# proof of identity
# proof of Montana residency
# proof of authorized presence

def get_num(first, month, year, day, sex):
    sdx = ''
    first = first.upper()
    month = str(month)
    year = str(year)
    day = int(day)
    sex = str(sex)

    if len(str(year)) != 4:
        return "Bad Year"
    if day < 1 or day > 31:
        return "Bad Day"

    dictMonths = {"JANUARY": 1, "FEBRUARY": 2, 'MARCH': 3, "APRIL": 4,
                  "MAY": 5, "JUNE": 6, "JULY": 7, "AUGUST": 8, "SEPTEMBER": 9,
                  "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}

    if sex == 'M' or 'MALE':
        sex_code = '14'
    else:
        sex_code = '15'

    if month.upper() in dictMonths:
        month_num = dictMonths[month.upper()]
        month_code = str(month_num).zfill(2)
    else:
        return"Month not found"

    sdx += first[0]
    sdx += month_code
    sdx += sex_code
    sdx += year
    sdx += 41
    sdx += str(day).zfill(2)

    return sdx


def montana_is_valid(first, sex, month, year, day):
    #set up params for generic state
    expiration_length = [4]
    sex_X = False
    hair = False
    issue_date = issue_date
    state = "MT"
    reuslts = generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)
    if reuslts != True:
        return reuslts

    #Generate number
    mylicensenumber = get_num(first, sex, month, year, day)
    return mylicensenumber

"""
60f
Summary Comment for Montana:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = False,
    with hair, and expiration_length is 4(75+) or 8 years
f06
"""
