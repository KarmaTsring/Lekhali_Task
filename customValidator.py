import re
from cerberus import Validator 

schl_dicts = { 
        
                #'name':'Exqwqwq', 'address':'Swayambhu','sch_type':'Higher Secondary School',
                'name':'Koteshwor', 'address':'Buddha Park','sch_type':'Higher Secondary School'
                
        }

hsp_dicts = {
                #'name':'Manmohan Hospital','hsp_id': 22, 'address':'Sitapaila',
                'name':'Norvic International','hsp_id': 1002,'address':'Thapathali'
                }


def schl_validators(schl_dict):
    schema = {
        'name':{'type':'string', 'minlength':5, 'maxlength':25},
        'sch_id':{'type':'integer', 'min':1, 'max':300},
        'address':{'type':'string', 'min':5, 'max':50},
        'sch_type':{'type':'string', 'min':5, 'max':90}
         }
        
    v = Validator(schema)
    if v.validate(schl_dict):
        return True
    else:
        return False


def hsp_validators(hsp_dict):
    schema = {
        'name':{'type':'string', 'minlength':7, 'maxlength':30},
        'hsp_id':{'type':'integer', 'min':1, 'max':400},
        'address':{'type':'string', 'min':5, 'max':50}
         }

    v = Validator(schema)
    if v.validate(hsp_dict):
        return True
    else:
        return False



#function as argument for school dict, validator 
def schl_check(schl_dict, func):
    return func(schl_dict)

#function as argument for hospital dict, validator
def hsp_check(hsp_dict, func):
    return func(hsp_dict)


print(f'School Dict valid: {schl_check(schl_dicts, schl_validators)}')
print(f'Hospital dict is Valid: {hsp_check(hsp_dicts, hsp_validators)}')   