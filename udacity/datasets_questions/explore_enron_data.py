#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("Data: %d" %len(enron_data["GLISAN JR BEN F"].keys()))
count = 0
for k,v in enron_data.iteritems():
	if enron_data[k]["poi"]==1:
		count = count + 1

print("POI Count:  %d" %count)
num_lines = sum(1 for line in open('../final_project/poi_names.txt'))
print(enron_data)
print(enron_data["SKILLING JEFFREY K"])
print(enron_data["LAY KENNETH"])
print(enron_data["FASTOW ANDREW"])
print("Line Count : %d" %num_lines )
#print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Value of Stocks for James Prentice : %d" %enron_data["PRENTICE JAMES"]["total_stock_value"])
