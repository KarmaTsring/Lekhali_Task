# from cerberus import Validator 
from schema import Schema, And, Use, Optional, SchemaError
from functools import singledispatch

@singledispatch
def check(schema, dataDict):
    try:
        schema.validate(dataDict)
        return True
    except SchemaError:
        return False

@check.register(dict)
def _(schema, dataDict):
    print("Hunxa")
        

schema = Schema({'toleName': And(str, lambda s: 5 <= len(s) <=45), #min_length=5, max_length=45
                   'lat':  And(Use(float), lambda n: -90 <= n <= 90),  #decimal format of latitude ranges from -180 to 180
                   'lng':  And(Use(float), lambda n: -180 <= n <= 180), #decimal format of longitude ranges from -180 to 180
                   'trueFalse': bool
                })

#User getting input of data dict
dataDict = {
    'toleName':'kathma',
    'lat':20.4343,
    'lng':-119.1213,
    'trueFalse': True
    

}

print(check(schema, dataDict))
print(check(schema, dataDict))