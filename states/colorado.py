from datetime import date, datetime

def get_num(day, month, year):
    sdx = ''

    expiration_date = str(year) + '-' + str(month) + '-' + str(day)
    day_of_year = datetime.strptime(expiration_date,"%Y-%m-%d").date().strftime('%j')
    print(day_of_year)

    sdx += str(year)[2:]
    sdx += str(day_of_year)

    #####OVERFLOW NUM#####
    sdx += '0001'
    return sdx


# One function to generate and format a driver's license number for 
# illinois, wisconsin, and florida
def generateDLNColorado( dayIssue, monthIssue, yearIssue ):
	MyLicenseNumber = get_num(dayIssue, monthIssue, yearIssue)
	return MyLicenseNumber