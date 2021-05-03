import numpy as np

def dln_UT_TN_NM_VT(dln, whichState):
    whichState=whichState.upper()
    if whichState not in ['UT', 'TN', 'NM', 'VT']:
        return "Not in function states."
    if whichState == 'UT':
        weight_vector = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])
        dln_vector = np.array([int(i) for i in str(dln)])
        truth_value = np.dot(weight_vector, dln_vector) % 10
        if truth_value != 0:
            return False
        else:
            return True
    elif whichState == 'TN' or whichState == 'NM' or whichState == 'VT':
        weight_vector = -np.array([2, 7, 6, 5, 4, 3, 2])
        dln_vector = np.array([int(i) for i in str(dln)[:-1]])
        val = np.dot(weight_vector, dln_vector) % 11
        if val == 0:
            if whichState == 'VT' and str(dln)[-1] == 'A':
                return True
            if str(dln)[-1] == 1 and whichState != 'VT':
                return True
        elif val == 10:
            if str(dln)[-1] == 0:
                return True
        elif val == str(dln)[-1]:
            return True
        else:
            return False
    
    else:
        return False

def dln_WA(dln):
    #should be a string already, but just to be sure
    dln = str(dln)

    #the mappings that Washington uses for characters to numbers
    char_dict = {'AJ' : 1,
        'BKS' : 2,
        'CLT' : 3,
        'DMU' : 4,
        'ENV' : 5,
        'FOW' : 6,
        'GPX' : 7,
        'HQY' : 8,
        'IRZ' : 9}

    dln_char_to_key = ''
    for char in dln:
        for key in char_dict.keys():
            if char in key:
                dln_char_to_key += str(char_dict[key])

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    converted_dln = ''
    for char in dln:
        if char in alphabet:
            char = dln_char_to_key[count]
            count += 1
            converted_dln += char
        else:
            converted_dln += char
    
    assert len(converted_dln) == len(dln) == 12

    dln_list = [int(i) for i in converted_dln]

    dln_list[0] -= sum(dln_list[1 : 4])
    dln_list[0] += sum(dln_list[4 : 9])
    dln_list[0] -= dln_list[10]
    dln_list[0] += dln_list[11]

    dln_list[0] = abs(dln_list[0]) % 10
    if converted_dln[9] == dln_list[0]:
        return True
    else:
        return False

def generateDLN_UT_TN_NM_VT_MB_WA(dln, state):
    if state in ['UT', 'TN', 'NM', 'VT']:
        return dln_UT_TN_NM_VT(dln, state)
    elif state in ['MB', 'WA']:
        return dln_WA(dln)

#print(get_is_valid_with_date("8205059A", "VM", '2021-05-02'))

"""
count = 0
start = time.time()
dln_NM = ''
nums = "0123456789"
for i in range(8):
    dln_NM += nums[np.random.randint(0, len(nums))]

while dln_UT_TN_NM_VM(dln_NM, 'NM') != True:
    count += 1
    if count % 100000 == 0:
        print(count)
    if dln_UT_TN_NM_VM(dln_NM, 'NM') == True:
        print(dln_NM)
    dln_NM = ''
    for i in range(8):
        dln_NM += nums[np.random.randint(0, len(nums))]

print(time.time() - start)
"""