

def validators(dict):
    validations = {
    "name": lambda x: isinstance(x, str) and 5 <= len(x) <= 45,
    "lat": lambda x: isinstance(x, float) and -90 <= x <= 90,
    "lng": lambda x: isinstance(x, float) and -180 <= x <= 180,
    }
    for k,v in dict.items():
        # return validations.get(keys, lambda x: False)(values)
        return all(validations.get(k, lambda x: False)(v) for (k, v) in dict.items())
    

def check(dict, func):
    return func(dict)

dicts = {'name':'Seewew',
        'lat':43.222,
        'lng':-22.3331
        }

print(check(dicts, validators))
