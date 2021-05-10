'''
New Hampshire uses the month(2 digits), first letter last name,
last letter last name, first letter first name, last two digits
of the year, the day(2 digits), and 1 overflow num
'''

def get_num(month, day, year, whichState, sex, first, last, middle=None):
    sdx = ''
    first = first.upper()
    last = last.upper()
    month = str(month)

    dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
		"APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
		"AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
		"NOVEMBER" : 11, "DECEMBER" : 12}

    #change month and find num code
    if month.upper() in dictMonths:
        month_num = dictMonths[month.upper()]
        month_code = str(month_num).zfill(2)

    if len(str(year)) != 4:
        return "Bad Year"
    if day < 1 or day > 31:
        return "Bad Day"

    #put DL number together
    sdx += month_code
    sdx += last[0] + last[len(last) - 1] + first[0]
    sdx += str(year)[2:]
    sdx += str(day).zfill(2)
    
    #overflow num - default '0'
#    sdx += '0'
    return sdx

def new_hampshire_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [5]
    sex_X = True
    hair = hair
    issue_date = issue_date
    state = "NH"
    result = generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)
    return result

# One function to generate and format a driver's license number for 
# new hampshire
def generateDLNNewHampshire( state, month, day, year, sex, first, last, middle=None):
    results = new_hampshire_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
    if results != True:
        return results
    MyLicenseNumber = get_num(month, day, year, state, sex, first,last, middle)
    return MyLicenseNumber

"""
60f
Summary Comment for New Hampshire:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = True,
    with hair, and expiration_length is 5 years
f06
"""

