from states.maryland_michigan_dln import generateDLNMarylandMichigan
from states.new_hampshire_dln import generateDLNNewHampshire
from states.Illinois_Florida_Wisconsin import generateDLNIllinoisFloridaWisconsin
from states.utah_dln_nums import generateDLN_UT_TN_NM_VT_MB_WA

def DLHelper(state_abbr, dln, fName, lName, middle, month, day, year, sex ):

    #FLORIDA, WISCONSIN, ILLINOIS
    if state_abbr == 'FL' or state_abbr == 'WI' or state_abbr == 'IL':
        return generateDLNIllinoisFloridaWisconsin( state_abbr, month, day, year, sex, fName, lName, middle )

    #MICHIGAN, MARYLAND
    elif state_abbr == 'MI' or state_abbr == 'MD':
        return generateDLNMarylandMichigan( state_abbr, month, day, year, sex, fName, lName, middle )

    #NEW HAMPSHIRE
    elif state_abbr == 'NH':
        return generateDLNNewHampshire( state_abbr, month, day, year, sex, fName, lName, middle )

    elif state_abbr in ['UT', 'TN', 'VT', 'NM', 'WA', 'MB']:
        return generateDLN_UT_TN_NM_VT_MB_WA( dln, state_abbr )

    #state not included/something went wrong
    else:
        return False