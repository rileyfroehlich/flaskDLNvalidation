from states.maryland_michigan_dln import generateDLNMarylandMichigan
from states.new_hampshire_dln import generateDLNNewHampshire
from states.Illinois_Florida_Wisconsin import generateDLNIllinoisFloridaWisconsin

def DLHelper(state_abbr, dln, fName, lName, middle, month, day, year, sex, dlMonth, dlYear):

    #FLORIDA, WISCONSIN, ILLINOIS
    if state_abbr == 'FL' or state_abbr == 'WI' or state_abbr == 'IL':
        return generateDLNIllinoisFloridaWisconsin( state_abbr, month, day, year, sex, fName, lName, middle )

    #MICHIGAN, MARYLAND
    elif state_abbr == 'MI' or state_abbr == 'MD':
        return generateDLNMarylandMichigan( state_abbr, month, day, year, sex, fName, lName, middle )

    #NEW HAMPSHIRE
    elif state_abbr == 'NH':
        return generateDLNNewHampshire( state_abbr, month, day, year, sex, fName, lName, middle )

    #state not included/something went wrong
    else:
        return False