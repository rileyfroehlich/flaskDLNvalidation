from datetime import date, datetime

'''
Colorado uses the last 2 digits of year, if before 92' it becomes 1992
then the date of the year issued eg. Jan 1 = 001/ Dec 31 = 365
The last 4 digits are sequential to the license issued that day
at that DMV
'''

dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
    "APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
    "AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
    "NOVEMBER" : 11, "DECEMBER" : 12}

def get_num(day, month, year):
    sdx = ''
    month = month.upper()

    if month in dictMonths.keys():
        month = dictMonths[month]

    #finds the day of the year
    date = str(year) + '-' + str(month) + '-' + str(day)
    day_of_year = datetime.strptime(date,"%Y-%m-%d").date().strftime('%j')

    #before 1992, change year
    if int(year) <= 1992:
        year = 1992
    sdx += str(year)[2:]
    sdx += str(day_of_year)

    #####OVERFLOW NUM#####
#    sdx += '0001'
    return sdx

#Use the generic state validator to verify inputs
def Colorado_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight, extra=None):
    from Generic_State import generic_State_is_valid
    expiration_length = [5]
    sex_X = True
    hair = hair
    issue_date = issue_date
    state = "CO"
    return generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X, hair, extra=extra)

# One function to generate and format a driver's license number for 
# illinois, wisconsin, and florida
def generateDLNColorado( dayIssue, monthIssue, yearIssue ):
    result = Colorado_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
    if result != True:
        return result
    MyLicenseNumber = get_num(dayIssue, monthIssue, yearIssue)
    return MyLicenseNumber

"""
60f
Summary Comment for Colorado:
    Imports Generic State Validator function and passes its
    parameters to it, with the addition of sex_X = True,
    with hair, and expiration_length is 5 years
f06
"""
