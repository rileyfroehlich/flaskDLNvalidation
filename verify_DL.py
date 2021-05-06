from states.maryland_michigan_dln import generateDLNMarylandMichigan
from states.new_hampshire_dln import generateDLNNewHampshire
from states.Illinois_Florida_Wisconsin import generateDLNIllinoisFloridaWisconsin
from states.utah_dln_nums import generateDLN_UT_TN_NM_VT_MB_WA
from states.colorado import generateDLNColorado

#takes in all variables passed to main.py to call individual state DLN checkers
def DLHelper(state_abbr, dln, fName, lName, middle, month, day, year, sex, eyeColor, issueDay, issueMonth, issueYear ):

    #FLORIDA, WISCONSIN, ILLINOIS
    if state_abbr in [ 'FL', 'WI', 'IL' ]:
        return generateDLNIllinoisFloridaWisconsin( state_abbr, month, day, year, sex, fName, lName, middle )

    #MICHIGAN, MARYLAND
    elif state_abbr == 'MI' or state_abbr == 'MD':
        return generateDLNMarylandMichigan( state_abbr, month, day, year, sex, fName, lName, middle )

    #NEW HAMPSHIRE
    elif state_abbr == 'NH':
        return generateDLNNewHampshire( state_abbr, month, day, year, sex, fName, lName, middle )

    #UTAH, TENNESEE, VERMONT, NEW MEXICO, WASHINGTON, MANITOBA
    elif state_abbr in ['UT', 'TN', 'VT', 'NM', 'WA', 'MB']:
        return generateDLN_UT_TN_NM_VT_MB_WA( dln, state_abbr )

    #COLORADO
    elif state_abbr == 'CO':
        return generateDLNColorado(issueDay, issueMonth, issueYear)

    #state not included/something went wrong
    else:
        return False