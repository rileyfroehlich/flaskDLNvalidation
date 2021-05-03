from dlnvalidation import is_valid

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

    if len(state) == 2:
        return state.upper()

    state = state.capitalize()
    print(state)

    if state in us_state_abbrev.keys():
        return us_state_abbrev[state]
    else:
        return None

def check_is_valid(state_abbr, dln):
    state_abbr = get_state_abbr(state_abbr)
    if state_abbr is not None:
        try:
            if is_valid(dln, state_abbr):
                #check state generator here
                return True
            else:
                return "Your Driver's License Number is not Valid!"
        except Exception as e:
            print(str(e))
            return "Invalid State!"
    else:
        return "Invalid State"