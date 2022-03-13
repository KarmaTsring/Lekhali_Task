

def validators(dict):
    
    #define num to compare it to the len of dict
    num = 0 
    for value in dict.values():
        if type(value) == str:
            if len(value)>5 and len(value)<45:
                num +=1
        elif type(value)== float and (value>-180 and value<180):
            num+=1
        elif type(value) == bool:
            num+=1  
   #if the num value is equal to the length of dict-items, for all the dict-values validation then it returns, True
    if num == len(dicts):
        return True
    else:
        return False

def check(dict, func):
    return func(dict)

dicts = {'name':'Santosh',
        'lat':10.00,
        'lng':22.00,
        'bool':True,
        'apple':'a'
        }
# print(len(dicts))

print(check(dicts, validators))
