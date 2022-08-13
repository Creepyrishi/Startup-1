import os
from pyairtable import Api, Base, Table


MESSAGE_BASEID ="appDOHob0s9g3sw8d"
AIRTABLE_API = 'keyIgDCfhEZJMHEVf'

messageTable = Table(AIRTABLE_API, MESSAGE_BASEID, 'message')
serviceTable = Table(AIRTABLE_API, MESSAGE_BASEID, 'service')


# for storing message from website 
def addMessage(name:str, phone:int, mail:str, message:str):
    data = {
        "Name": name,
        "Phone": phone,
        "Mail": mail,
        "Message": message,
    }
    try:
        messageTable.create(data)  
        return True  
    except Exception as e:
        print(e)
        return False

# for retriving all services 
def getServices():
    for records in serviceTable.iterate(page_size=100, max_records=1000):
        return records