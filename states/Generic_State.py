def generic_State_is_valid(dln, DOB, expiration_date, expiration_length, eyes, height, issue_date, sex, state, weight, sex_X = False, hair = False, extra=None):
    #DOB should be in format of "MM-DD-YYYY", height should be 'F-II', weight in '000'
    #state is abbreviation. Above parameters are declared alphabetically
    #If hair is given, then it must be the 3 letters denoting the color, not a boolean
    #When making a file for a new state, use these following links to determine expiration_length
    #and sex_X. expiration_length is a list containing all numbers that the state can use.
    #Because some states can use different lengths (i.e. the driver can choose 4 or 8 in some)
    #https://en.wikipedia.org/wiki/Driver%27s_licenses_in_the_United_States
    #https://en.wikipedia.org/wiki/Transgender_rights_in_the_United_States#Drivers'_licenses

    #We import time to find current date, and then set the month, day, and year
    #variables to the current month, day, and year
    import time
    month = time.strftime("%m")
    day = time.strftime("%d")
    year = time.strftime("%Y")


    #Setting the DOB dates to appropriate variables to compare later on
    DOB_list = DOB.split('-')
    DOB_month = DOB_list[0]
    DOB_day = DOB_list[1]
    DOB_year = DOB_list[2]

    #The difference is found by simple math (in overall years)
    #If the user is over 80, the user can still be validated, but
    #the team is notified for further confirmation
    diff_year = int(year) - int(DOB_year)
    diff_month = int(month) - int(DOB_month)
    diff_day = int(day) - int(DOB_day)
    date_difference = diff_year + diff_month/12 + diff_day/365
    if (date_difference > 65):
        #exception()
        pass

    #Finding the height in overall inches
    #First we clean the data to numbers and add the
    #feet to inches. Finally, if the height is abnormal
    #(outside of the normal distribution of height, very low
    #percentage of occurance), then exception() is called,
    #although the user can still be validated
    height_list = height.split('-')
    feet = height_list[0]
    inches = height_list[1]
    overall_inches = int(feet)*12 + int(inches)
    if ( (overall_inches < 50) or (overall_inches > 90) ):
        #exception()
        pass


    #Finding the weight, and from there, the BMI
    #The BMI will be used to find extreme cases and invalidate the user
    #In cases when the BMI is unusual, but not fringe cases, the user
    #Can still be validated, but the team will be informed
    weight = int(weight)
    BMI = ( weight / (overall_inches ** 2) ) * 703
    if ( (BMI < 15) or (BMI > 40) ):
        #exception()
        pass


    #This is a list of abbreviations used by the government. In case this is updated or
    #differs between states, when this is checked, exception() is called for investigation,
    #just in case
    eye_color_list = ["BLK", "BLU", "BRO", "GRY", "GRN", "HAZ", "MAR", "MUL", "PNK", "XXX", None]
    hair_color_list = ["BAL", "BLK", "BLN", "BLU", "BRO", "GRY", "GRN", "ONG", "PLE", "PNK",
                        "RED", "SDY", "WHI", "XXX"]


    #Below we compare the issue and expiration dates. They should be
    #exactly 5 years apart. In the off chance this state changes the
    #length, when this invalidates a user, exception() is called
    expiration_list = expiration_date.split('-')
    if ( int(expiration_list[2]) < int(year) ):
        return False
        #License is EXPIRED


    if (issue_date != False):
        issue_list = issue_date.split('-')
        if (expiration_list[0] != issue_list[0]):
            return False
        elif (expiration_list[1] != issue_list[1]):
            return False
        #Below we check the issue date is not past the current date
        elif (int(issue_list[2]) == int(year)):
            if (int(issue_list[0]) == int(month)):
                if (int(issue_list[1]) > int(day)):
                    return False
            if (int(issue_list[0]) > int(month)):
                return False
        elif (int(issue_list[2]) > int(year)):
            return False

        #Below it loops through all expiration lengths, and if none of the
        #dates are any appropriate year from the issued date, then it returns
        #False, otherwise, it keeps progressing through the code
        bool_list = []
        for year_num in expiration_length:
            if ( int(expiration_list[2]) != (int(issue_list[2]) + year_num) ):
                #exception()
                bool_list.append(False)
        if (True in bool_list):
            return False

    #Imports function from dlnvalidation
    from dlnvalidation import is_valid
    #Control structure to check that everything is valid. If everything
    #is normal, nothing will be flagged. Certain cases may call exception()
    #for further investigation
    if ( is_valid(dl_number = dln, dl_state = state) == False ):
        return False
    if ( (date_difference < 18) or (date_difference > 100) ):
        return False
    elif ( (int(DOB_month) > 12) or (int(DOB_day) > 31) ):
        return False
    elif ( (sex != 'M') and (sex !='F') ):
        if (sex_X and sex == 'X'):
            pass
        else:
            return False
    elif ( (overall_inches < 20) or (overall_inches > 95) ):
        #Checks to make sure height is not above and below the
        #tallest and shortest heights of people
        #exception()
        return False
    elif ( (weight < 20) or (weight > 600) ):
        #exception()
        return False
    elif ( (BMI < 8) or (BMI > 100) ):
        #Checks for very unrealistic BMIs,
        #This is extremely wide, so most likely
        #not effective but its another step
        #exception()
        return False
    elif ( eyes not in eye_color_list ):
        #exception()
        return False
    elif ( (hair != False) and (hair not in hair_color_list) ):
        #exception()
        return False
    else:
        return True


if ( __name__ == "__main__" ):
    print(generic_State_is_valid("9999999", "01-01-2000", "02-04-2022", 5, "BRO", '5-11', "02-04-2017", 'F', "AL", '300'))


"""
60f
Summary Comment of generic State validator:
    Parameters are given in alphabetical order, and contain the following:
        Driver License Number, Date of Birth, Expiration Date, Eye Color,
        Height, Issue Date, Sex, State, and Weight. It can also take in
        sex_X, which is a bool if the state uses 'X' for other than male and female,
        and hair, which is originally False, but when provided, should be the hair
        color. issue_date can also be False
    Age of the individual is calculated and verified it is older than the limit,
    and within a reasonable range. License expiration is also checked. BMI is found
    and checked that it is within normal human ranges. Height and weight are also
    found to be within normal human ranges.
    When an abnormal piece of data is given, if it is still within a small percentage
    of likeliness to occur, then the user can still be validated, but exception()
    is called, which is a custom function that emails the dev team and cobalt to alert
    them to the file it's being called from, the error that occured, and the user it
    orginated from. This function is also called whenever a validation error in a part
    of code that is based on rules that may have changed (i.e. eye color list is updated
    in a certain state, which makes our code invalidate an actually validate hair color)
    The file goes off of the current date for anything relating to time (import time).
    dlnvalidation DOES need to be imported beforehand.

    Originally did not realize some states did not include issue date, so had to go back
    and add the if statement. Solution was to take the statement checking the license
    is not expired outside of the rest of the statements checking the issue date relations.
    Then I simply put all of the if and elif statements inside a single if statement
    checking if the issue_date is NOT false

    Links provided for sex_X and expiration_length are:
        https://en.wikipedia.org/wiki/Driver%27s_licenses_in_the_United_States
        https://en.wikipedia.org/wiki/Transgender_rights_in_the_United_States#Drivers'_licenses
    expiration_length is a list because some states have multiple lengths the license can last.
    Therefore, if a state has only one year, have a single item list.
    For future development, time can be put into further logic to follow up with those special
    case states, because there *IS* deeper logic, like some states have a 5 year length, but
    ONLY after 65. To implement this would require more reworking of this inner logic, additional
    parameters, and maybe more.
        Note: I added a section to loop through this and add to a list of bools to keep track
        of if any dates did or did not pass the loop, as you can't automatically return True
        or False in a single loop, you need to test all of them and see if they are all False

    dlnvalidation may be incorrect for Maine, as it says it takes only 7 digits, but it seems
    Maine can take 7-8. If this is the case, we might need to make our own version of
    dlnvalidation that we own and use, and can update directly. I updated the repo with a
    pull request on May 8, 2021, currently waiting for approval

    I added the 'extra' parameter for future development, as updating 50 files, the
    generic_State_is_valid, and testing all of them can take many hours, I started to create
    each state with this extra parameter that is Nonetype right now, but later on will be easy
    enough to set equal to a list of different information which this program can go to each index
    and find the information. It would also be easy enough to simply pass over it if it's Nonetype
f06
"""
