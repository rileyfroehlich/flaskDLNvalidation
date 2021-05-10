def Alabama_is_valid(last_name, license_number, expiration_date):
    #Imports to use a browser to go to the website and input/read data
    from selenium import webdriver
    from selenium.webdriver.common.touch_actions import TouchActions

    #THIS MUST BE CHANGED TO WHERE YOU DOWNLOAD CHROMDRIVER
    #https://chromedriver.chromium.org/downloads
    path = '/home/julian/Documents/BlockChain Stuff/Python/chromedriver'

    #Riley's Code, sets up the browser page with proper parameters
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(path, options=options)
    #^^^Must have Chrome installed

    #Navigates browser to the below link
    driver.get('https://alverify.mvtrip.alabama.gov/')

    #Sets all the input boxes (last name, license number, expiration date, and submit button)
    #to variables
    last_name_box = driver.find_element_by_id('ContentPlaceHolder1_txtLastName')
    license_number_box = driver.find_element_by_id('ContentPlaceHolder1_txtDLNumber')
    expiration_data_box = driver.find_element_by_id('ContentPlaceHolder1_txtDLExpirationDate')
    submit_button = driver.find_element_by_id('ContentPlaceHolder1_btnSubmit')

    #Inputs the data from the arguments of the function to the inputs
    last_name_box.send_keys(last_name)
    license_number_box.send_keys(license_number)

    #Expiration date was difficult, it only accepts numbers, and was not
    #reading input as the desired datatype, regardless of what I did.
    #Riley ultimately found this solution. He sets up the box and how we
    #send the data
    action=TouchActions(driver)
    action.tap(expiration_data_box)
    action.perform()

    #Below the data is sent, and the submit button clicked
    expiration_data_box.send_keys(expiration_date)
    submit_button.click()

    #From here, the output of the website is text on the screen
    #We take the label returned and find the properties (I tried a
    #few other methods and this was the first was to work, so I went
    #with it), which returns a string of attribute and value. I split
    #the string into a list, take the 2nd item, which is the value of color,
    #As failed yields red text and passed provides green text, although
    #It needs to be tested to find the exact green color. From there, we
    #clean the data and pass it through a control structure to verify
    #the value
    response = driver.find_element_by_id('ContentPlaceHolder1_lblResponse')
    response = response.get_attribute('style')
    response_list = response.split()
    response = response_list[1].rstrip(';')
    if (response == 'darkred'):
        return False
    else:#if (response == ''):
        return True
    driver.close() ##Move outside control structure once valid is verified
    # ^^^ Closes the window
    #I left part of the elif for future development when we get a valid
    #Alabama license

#Below is used to test that the code can reach out to the appropriate website
if (__name__ == '__main__'):
    print(Alabama_is_valid("Oldironsides", "B4332134", "112022"))


"""
60f
Summary comment of Alabama:
    Uses Selenium to navigate to the official Alabama gov website to verify
    the license exists within their database. Main developers were Riley and
    Julian. It verifies the license by checking the color of the
    validated/notvalidated text on the page. At the end, the page is closed.
    The execution time of the code should be no more than 5 seconds, most of that
    time is reaching out to the website

    Expiration date was a different input type than license number and last name,
    and required a different solutions, which Riley was able to solve.
f06
"""
