#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pymongo
client = pymongo.MongoClient('mongodb://embifiAdmin:embifi_1659709763@db.embifi.in:22058/lms?authMechanism=DEFAULT&authSource=admin')
db = client['lms']
loan_application = db['loanapplications']

def customer_tenure(customer_id):
    tenure_value = int(loan_application.find_one({'customer_id':customer_id})['tenure_value'])

    if tenure_value in (1,2,3,4,5,6):
        model_number = tenure_value
    
    elif tenure_value > 6:
        model_number = 6
        
    return model_number

