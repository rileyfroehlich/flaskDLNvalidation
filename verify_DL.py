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
from states.Connecticut import Connecticut_is_valid
from states.Delaware import delaware_is_valid
from states.District_of_Columbia import district_of_columbia_is_valid
from states.Florida import florida_is_valid
from states.Georgia import Georgia_is_valid
from states.Hawaii import Hawaii_is_valid
from states.Idaho import Idaho_is_valid
from states.Illinois import Illinois_is_valid
from states.Indiana import Indiana_is_valid
from states.Iowa import Iowa_is_valid
from states.Kansas import Kansas_is_valid
from states.Kentucky import kentucky_is_valid
from states.Louisiana import Louisiana_is_valid
from states.Maine import Maine_is_valid
from states.Maryland import Maryland_is_valid
from states.Massachusetts import massachusetts_is_valid
from states.Michigan import Michigan_is_valid
from states.Minnesota import minnesota_is_valid
from states.Mississipi import mississipi_is_valid
from states.Missouri import missouri_is_valid
from states.montana import montana_is_valid
from states.Nebraska import nebraska_is_valid
from states.Nevada import nevada_is_valid
#New Jersey
from states.New_Mexico import new_mexico_is_valid
from states.New_York import new_york_is_valid
from states.North_Carolina import north_carolina_is_valid
from states.North_Dakota import north_dakota_is_valid
from states.Ohio import ohio_is_valid
from states.Oklahoma import oklahoma_is_valid
from states.Oregon import oregon_is_valid
from states.Pennsylvania import pennsylvania_is_valid
from states.Rhode_Island import rhode_island_is_valid
from states.South_Carolina import south_carolina_is_valid
from states.South_Dakota import south_dakota_is_valid
from states.Tennessee import tennessee_is_valid
from states.Texas import texas_is_valid
from states.Utah import utah_is_valid
from states.Vermont import vermont_is_valid
from states.Virginia import virginia_is_valid
from states.Washington import washington_is_valid
from states.West_Virginia import west_virginia_is_valid
from states.Wisconsin import wisconsin_is_valid
from states.Wyoming import wyoming_is_valid

#takes in all variables passed to main.py to call individual state DLN checkers
def DLHelper(state_abbr, dln, fName, lName, middle, month, day, year, sex, eyeColor, issueDay, issueMonth, issueYear ):

    #FLORIDA, WISCONSIN, ILLINOIS
    if state_abbr in [ 'FL', 'WI', 'IL' ]:

        #Florida
        if state_abbr == 'FL':
            #overflow num = 1 digit
            dln = dln[:-1]
            results = florida_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

        #Wisconsin
        elif state_abbr == 'WI':
            #overflow num = 2 digits
            dln = dln[:-2]
            results = wisconsin_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

        #Illinois
        else:
            results = Illinois_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
        if results != True:
            return results
        return generateDLNIllinoisFloridaWisconsin( state_abbr, month, day, year, sex, fName, lName, middle )

    #MICHIGAN, MARYLAND
    elif state_abbr == 'MI' or state_abbr == 'MD':
        #Michigan
        if state_abbr == 'MI':
            results = Michigan_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
        #Maryland
        else:
            results = Maryland_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

        if results != True:
            return results
        return generateDLNMarylandMichigan( state_abbr, month, day, year, sex, fName, lName, middle )

    #NEW HAMPSHIRE
    elif state_abbr == 'NH':
        #remove overflow nums
        dln = dln[:-1]
        return generateDLNNewHampshire( state_abbr, month, day, year, sex, fName, lName, middle )

    #UTAH, TENNESEE, VERMONT, NEW MEXICO, WASHINGTON, MANITOBA
    elif state_abbr in ['UT', 'TN', 'VT', 'NM']:
        #Utah
        if state_abbr == 'UT':
            results = utah_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
        #Tennessee
        elif state_abbr == 'TN':
            results = tennessee_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
        #Vermont
        elif state_abbr == 'VT':
            results = vermont_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
        #New Mexico
        else:
            results = new_mexico_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

        if results != True:
            return results
        return generateDLN_UT_TN_NM_VT_MB_WA( dln, state_abbr )

    #COLORADO
    #TO DO params
    elif state_abbr == 'CO':
        #remove overflow nums
        dln = dln[:-4]
        return generateDLNColorado(issueDay, issueMonth, issueYear)

    #Alabama
    elif state_abbr == "AL":
        return Alabama_is_valid(lName, dln, expiration_date)

    #Generic state algos
    #Alaska
    elif state_abbr == "AK":
        return Alaska_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)

    #Arizona
    elif state_abbr == "AZ":
        return Arizona_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)

    #Arkansas
    elif state_abbr == "AR":
        return Arkansas_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)

    #Califonia
    elif state_abbr == "CA":
        return Califonia_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Connecticut
    elif state_abbr == "CT":
        return Connecticut_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Delaware
    elif state_abbr == "DE":
        return delaware_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #District of Columbia
    elif state_abbr == "DC":
        return district_of_columbia_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Georgia
    elif state_abbr == "GA":
        return Georgia_is_valid(dln, DOB, expiration_date, eyes, height, sex, weight)

    #Hawaii
    elif state_abbr == "HI":
        return  Hawaii_is_valid(dln, DOB, expiration_date, eyes, height, sex, weight)

    #Idaho
    elif state_abbr == "ID":
        return Idaho_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Indiana
    elif state_abbr == "IN":
        return Indiana_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Iowa
    elif state_abbr == "IA":
        return Iowa_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)

    #Kansas
    elif state_abbr == "KS":
        return Kansas_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)
    
    #Kentucky
    elif state_abbr == "KY":
        return kentucky_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)

    #Louisiana
    elif state_abbr == "LA":
        return Louisiana_is_valid(dln, DOB, expiration_date, eyes, height, issue_date, sex, weight)
    
    #Maine
    elif state_abbr == "ME":
        return Maine_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
    
    #Mississipi
    elif state_abbr == "MS":
        return mississipi_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Massachusets
    elif state_abbr == "MA":
        return massachusetts_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Minnesota
    elif state_abbr == "MN":
        return minnesota_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
    
    #Missouri
    elif state_abbr == "MO":
        return missouri_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)
    
    #Montana
    #TO DO params
    elif state_abbr == "MT":
        return montana_is_valid(first, sex, month, year, day)

    #Nebraska
    elif state_abbr == "NE":
        return nebraska_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Nevada
    elif state_abbr == "NV":
        return nevada_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #New York
    elif state_abbr == "NY":
        return new_york_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #North Carolina
    elif state_abbr == "NC":
        return north_carolina_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #North Dakota
    elif state_abbr == "ND":
        return north_dakota_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Ohio
    elif state_abbr == "OH":
        return ohio_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Oklahoma
    elif state_abbr == "OK":
        return oklahoma_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Oregon
    elif state_abbr == "OR":
        return oregon_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Pennsylvania
    elif state_abbr == "PA":
        return pennsylvania_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Rhode Island
    elif state_abbr == "RI":
        return rhode_island_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #South Carolina
    elif state_abbr == "SC":
        return south_carolina_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #South Dakota
    elif state_abbr == "SD":
        return south_dakota_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Texas
    elif state_abbr == "TX":
        return texas_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Virginia
    elif state_abbr == "VA":
        return virginia_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Washington 
    elif state_abbr == "WA":
        return washington_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #West Virgina
    elif state_abbr == "WV":
        return west_virginia_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #Wyoming
    elif state_abbr == "WY":
        return wyoming_is_valid(dln, DOB, expiration_date, eyes, hair, height, issue_date, sex, weight)

    #if state abbrv does not match return false
    else:
        return False    