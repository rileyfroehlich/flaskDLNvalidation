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

    date = str(year) + '-' + str(month) + '-' + str(day)
    day_of_year = datetime.strptime(date,"%Y-%m-%d").date().strftime('%j')

    print(day_of_year)

    if int(year) <= 1992:
        year = 1992
    sdx += str(year)[2:]
    sdx += str(day_of_year)

    #####OVERFLOW NUM#####
    sdx += '0001'
    print(sdx)
    return sdx


# One function to generate and format a driver's license number for 
# illinois, wisconsin, and florida
def generateDLNColorado( dayIssue, monthIssue, yearIssue ):
	MyLicenseNumber = get_num(dayIssue, monthIssue, yearIssue)
	return MyLicenseNumber