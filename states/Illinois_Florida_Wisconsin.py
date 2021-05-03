"""
These states encode the surname, first name, middle initial,
date of birth, and sex
"""

def get_soundex(name):
	"""Get the soundex code for the string"""
	name = name.upper()

	soundex = ""
	soundex += name[0]

	dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

	for char in name[1:]:
		for key in dictionary.keys():
			if char in key:
				code = dictionary[key]
				if code != soundex[-1]:
					soundex += code

	soundex = soundex.replace(".", "")
	soundex = soundex[:4].ljust(4, "0")

	return str(soundex)

def name_middle_initial(name, last_name, middle_initial=None):
	#get soundex of given name
	sdx = get_soundex(last_name)

	name_dictionary = {'Albert':20, 'Frank':260,'Marvin':580,
						'Alice':20, 'George':300,'Mary':580,
						'Ann':40,'Grace':300, 'Melvin':600,
						'Anna':40,'Harold':340,'Mildred':600,
						'Anne':40,'Harriet':340, 'Patricia':680,
						'Annie':40, 'Harry':360, 'Paul':680,
						'Arthur':40, 'Hazel':360, 'Richard':740,
						'Bernard':80, 'Helen':380, 'Robert':760,
						'Bette':80, 'Henry':380, 'Ruby':740,
						'Bettie':80, 'James':440, 'Ruth':760,
						'Betty':80, 'Jane':440, 'Thelma':820,
						'Carl':120, 'Jayne':440, 'Thomas':820,
						'Catherine':120, 'Jean':460, 'Walter':900, 
						'Charles':140,'Joan':480, 'Wanda':900,
						'Dorthy':180, 'John':460, 'William':920,
						'Edward':220, 'Joseph':480, 'Wilma':920,
						'Elizabeth':220, 'Margaret':560,
						'Florence':260, 'Martin':560,
						'Donald':180,
						'Clara':140
						}

	dictionary = {"A" : 0, "B" : 60, "C" : 100, "D" : 160, "E" : 240, 
				  "G" : 280, "H" : 320, "I" : 400, "J" : 420, "K" : 500,
				  "L" : 520, "M" : 540, "N" : 620, "O" : 640, "P" : 660,
				  "Q" : 700, "R" : 720, "S" : 780, "T" : 800, "U" : 840,
				  "V" : 860, "W" : 880, "X" : 940, "Y" : 960, "Z" : 980
				  }


	#middle initial codes
	dict2 = {"NO" : 14, "PQ" : 15, "R" : 16, "S" : 17, "TUV" : 18, "WXYZ" : 19}
	alphabet2 = "ABCDEFGHIJKLM"

	for i in range(len(alphabet2)):
		dict2[alphabet2[i]] = i + 1
	
	middle_initial_encoding = 0
	for key in dict2.keys():
		if middle_initial in key:
			middle_initial_encoding = dict2[key]
			break
	name = name.capitalize()
	if name in name_dictionary:
		name0 = name_dictionary[name]
	else:
		name0 = dictionary[name[0]]
		name0 += middle_initial_encoding
		name0 = str(name0)
		if len(name0) < 3:
			for i in range(3 - len(name0)):
				name0 = "0" + name0
		sdx += str(name0)


	return sdx

def get_last_nums(month, day, year, whichState, sex, sdx):
	month = str(month)
	year = str(year)

	isFemaleTrue = 0
	if sex.lower() == 'f':
		isFemale = True
	else:
		isFemale = False

	if whichState.lower() == 'illinois':
		eachMonth = 31
		if isFemale == True:
			isFemaleTrue = 6
	elif whichState.lower() == 'florida' or whichState.lower() == 'wisconsin':
		eachMonth = 40
		if isFemale == True:
			isFemaleTrue = 5
	
	isFemale = True

	dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
		"APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
		"AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
		"NOVEMBER" : 11, "DECEMBER" : 12}

	year_sep = "-"

	year = year[-2:]

	monthEncoding = (dictMonths[month.upper()] - 1) * eachMonth + day

	if len(str(monthEncoding)) < 3:
		monthEncoding = str(monthEncoding)
		monthEncoding = monthEncoding[::-1]
		for i in range(3 - len(monthEncoding)):
			monthEncoding += '0'
		monthEncoding = monthEncoding[::-1]
	if isFemale == True:
		monthEncodingFirstNum = int(str(monthEncoding)[0])
		monthEncodingFirstNum += isFemaleTrue
		monthEncoding = str(monthEncodingFirstNum) + str(monthEncoding)[1:]

	sdx += str(year) + str(monthEncoding)
	return sdx


# One function to generate and format a driver's license number for 
# illinois, wisconsin, and florida
def generateDLN( state, month, day, year, sex, first, last, middle=None ):
	MyLicenseNumber = get_last_nums(month, day, year, state, sex, name_middle_initial(first,last, middle))
	state = state.lower()

	#formatting for individual states
	#overflow numbers are added at the end and represented as '0' or '00'
	if state == 'florida':
		MyLicenseNumber = MyLicenseNumber + '0'

	elif state == 'wisconsin':
		MyLicenseNumber = MyLicenseNumber + '00'
	return MyLicenseNumber

print(generateDLN('illinois', "January", 1, 2049, 'm','Opius','Henry', 'B'))