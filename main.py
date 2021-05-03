from dlnvalidation import is_valid
from datetime import date, datetime
from verify_DL import DLHelper

dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
    "APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
    "AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
    "NOVEMBER" : 11, "DECEMBER" : 12}

def get_state_abbr(state):
    state = str(state)

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New hampshire': 'NH',
        'New jersey': 'NJ',
        'New mexico': 'NM',
        'New york': 'NY',
        'North carolina': 'NC',
        'North dakota': 'ND',
        'Northern mariana islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto rico': 'PR',
        'Rhode island': 'RI',
        'South carolina': 'SC',
        'South dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    if len(state) == 2 and state in us_state_abbrev.values():
        return state.upper()

    state = state.capitalize()

    if state in us_state_abbrev.keys():
        return us_state_abbrev[state]
    
    #State not found return None
    return None

def check_is_valid(state_abbr, dln, fName, lName, mName, month, day, year, sex, dlDay, dlMonth, dlYear):
    state_abbr = get_state_abbr(state_abbr)
    if state_abbr is not None:

        if dlMonth.upper() not in dictMonths.keys():
            return "Invalid expiry month identified"
        else:
            dlMonth = dictMonths[dlMonth.upper()]
        if month.upper() not in dictMonths.keys():
            return "Invalid birth month identified"
        if len(dlYear) != 4 or len(year) != 4:
            return "Invalid year identified"
        if len(day) > 2 or len(dlDay) > 2:
            return "Invalid day identified"

        try:
            if is_valid(dln, state_abbr):
                #check expiry date if the DL format is correct
                expiration_date = str(dlYear) + '-' + str(dlMonth) + '-' + str(dlDay)
                if datetime.strptime(expiration_date,"%Y-%m-%d").date() < date.today():
                    return "Your Driver's License is Expired!"

                #call helper functions to verify DL number
                day = int(day)
                year = int(year)

                DLN = DLHelper( state_abbr, dln, fName, lName, mName, month, day, year, sex )
                print(DLN)
                if dln == DLN:
                    return True
                return "Your Driver's License Number is not Valid!"
            
            else:
                return "Your Driver's License Number is not Valid!"
        except Exception as e:
            print(str(e))
            return "Invalid State!"
    else:
        return "Invalid State"