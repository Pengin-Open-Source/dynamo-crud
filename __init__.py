'''
Writen by: Stuart Anderson
Copyright: Tobu Pengin, LLC. 2022
'''
from decouple import config
from connector import DynDBC as DBC
from crud import Operation as execute


#Declare AWS credential variables using .env keys -> see .env file for key values
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME = config("REGION_NAME")

dbc = DBC(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=REGION_NAME)


#running a blank session as main.  modify as needed for personal use case
if __name__ == "__main__":
    with execute(dbc,'posusers') as ex:
        response = ex.read({'data':{'email':'stuart@tobupengin.com'},'get':['email','firstname']}).get('Item')
        print(str(response))
        