def get_num(month, day, year, whichState, sex, first, last, middle=None):
    sdx = ''
    first = first.upper()
    last = last.upper()
    month = str(month)

    dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
		"APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
		"AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
		"NOVEMBER" : 11, "DECEMBER" : 12}

    if month.upper() in dictMonths:
        month_num = dictMonths[month.upper()]
        month_code = str(month_num).zfill(2)

    if len(str(year)) != 4:
        return "Bad Year"
    if day < 1 or day > 31:
        return "Bad Day"

    sdx += month_code
    sdx += last[0] + last[len(last) - 1] + first[0]
    sdx += str(year)[2:]
    sdx += str(day).zfill(2)
    #overflow num - default '0'
    sdx += '0'
    return sdx


# One function to generate and format a driver's license number for 
# illinois, wisconsin, and florida
def generateDLNNewHampshire( state, month, day, year, sex, first, last, middle=None):
	MyLicenseNumber = get_num(month, day, year, state, sex, first,last, middle)
	return MyLicenseNumber

print(generateDLNNewHampshire('michigan', "January", 1, 2049, 'm','Opius','Henry', 'B'))