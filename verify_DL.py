#DL Algo generated imports
from states.maryland_michigan_dln import generateDLNMarylandMichigan
from states.new_hampshire_dln import generateDLNNewHampshire
from states.Illinois_Florida_Wisconsin import generateDLNIllinoisFloridaWisconsin
from states.utah_dln_nums import generateDLN_UT_TN_NM_VT_MB_WA
from states.colorado import generateDLNColorado

#generic state imports
from states.Alabama import Alabama_is_valid
from states.Alaska import Alaska_is_valid
from states.Arizona import Arizona_is_valid
from states.Arkansas import Arkansas_is_valid
from states.California import Califonia_is_valid
from states.Delaware import delaware_is_valid
from states.District_of_Columbia import district_of_columbia_is_valid
from states.Georgia import Georgia_is_valid
from states.Hawaii import Hawaii_is_valid
from states.Idaho import Idaho_is_valid
from states.Indiana import Indiana_is_valid
from states.Iowa import Iowa_is_valid
from states.Kansas import Kansas_is_valid
from states.Louisiana import Louisiana_is_valid
from states.Maine import Maine_is_valid
from states.Mississipi import mississipi_is_valid
from states.Missouri import missouri_is_valid
from states.Nebraska import nebraska_is_valid
from states.Nevada import nevada_is_valid
from states.New_York import new_york_is_valid
from states.North_Carolina import north_carolina_is_valid
from states.North_Dakota import north_dakota_is_valid
from states.Ohio import ohio_is_valid
from states.Oklahoma import oklahoma_is_valid
from states.Oregon import oregon_is_valid
from states.Pennsylvania import pennsylvania_is_valid
from states.Rhode_Island import rhode_island_is_valid
from states.South_Carolina import south_carolina_is_valid
from states.Texas import texas_is_valid
from states.West_Virginia import west_virginia_is_valid
from states.Wyoming import wyoming_is_valid

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

    #Generic state algos
    


    #if state abbrv does not match return false
    else:
        return False