import csv
import pandas as pd
import numpy as np

data = pd.read_csv("insurance.csv")

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def load_list_to_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst


load_list_to_data(ages, "insurance.csv", 'age')
load_list_to_data(sexes , "insurance.csv", 'sex')
load_list_to_data(bmis , "insurance.csv", 'bmi')
load_list_to_data(num_children , "insurance.csv", 'children')
load_list_to_data(smoker_statuses , "insurance.csv", 'smoker')
load_list_to_data(regions , "insurance.csv", 'region')
load_list_to_data(insurance_charges , "insurance.csv", 'charges')


class PatientInfo:
    
    def __init__(self, patient_age, patient_sex, patient_bmi,
                 patient_children, patient_smoke, patient_region, patient_charge):
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_bmi = patient_bmi
        self.patient_children = patient_children
        self.patient_smoke = patient_smoke
        self.patient_region = patient_region
        self.patient_charge = patient_charge

    def average_smoker(self):

    	total_smokers = []
    	total_na_smoker = []

    	for element in self.patient_smoke:
    		if element == 'yes':
    			total_smokers.append(element)
    		elif element == 'no':
    			total_na_smoker.append(element)

    	total_smoker_mean = round(len(total_smokers) / len(self.patient_smoke), 3)
    	total_na_smoker_mean = round(len(total_na_smoker) / len(self.patient_smoke), 3)

    	print("Average patients that smokes:", total_smoker_mean)
    	print("Average patients that do not smoke:", total_na_smoker_mean)

    	if total_smoker_mean > total_na_smoker_mean:
    		print("According currenlty our database indicates average person that smokes greater than people does not smoke.")
    	elif total_na_smoker_mean > total_smoker_mean:
    		print('According currently our database indicates average person does not smoke greater than people who actually smoke.')    

    def update_age(self, new_age):
    	""" Updates Patient's age """ 
    	self.patient_ages = new_age
    	new_age = int(new_age)
    	print("Patient's new age is {}".format(self.patient_age))

    def update_children(self, num_of_child):
    	self.patient_children = num_of_child
    	
    	
    	if num_of_child <= 0:
    		print(f'You have no child.')
    		
    	elif num_of_child == 1:
    		print(f"You have got a single child.")
    	else:
    		print(f"You have {self.patient_children} children's.")

    def update_smoke(self, update_smoke=None):

    	if update_smoke == 0:
      		print("Well done, smoking it is not good for you plus makes your insurance cheaper.")

    	elif update_smoke >= 1:
      		print("Consider quit smoking to have a healty life and make your insurance cheaper.")

    def change_of_sex(self, gender=None):

    	if type(gender) is int:
    		print('Number is invalid entry. Enter a your gender')
    	else:
    		print(f"Succed. Information has been changed to {gender}.")


    def analyze_ages(self): # Copied.
        # initialize total age at zero
        total_age = 0
        # iterate through all ages in the ages list
        for age in self.patient_age:
            # sum of the total age
            total_age += int(age)
        # return total age divided by the length of the patient list
        return ("Average Patient Age: " + str(round(total_age/len(self.patient_age), 2)) + " years")

    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["Age"] = [int(age) for age in self.patient_age]
        self.patients_dictionary["Sex"] = self.patient_sex
        self.patients_dictionary["BMI"] = self.patient_bmi
        self.patients_dictionary["Num Of Child"] = self.patient_children
        self.patients_dictionary["Smoke Status"] = self.patient_smoke
        self.patients_dictionary["Regions"] = self.patient_region
        self.patients_dictionary["charges"] = self.patient_charge
        return self.patients_dictionary

    def gender_count(self):
    	male_count = 0
    	female_count = 0

    	for gender in self.patient_sex:

    		if gender == 'male':
    			male_count += 1

    		elif gender == 'female':
    			female_count += 1
    	print("Male Count:", str(male_count))
    	print("Female Count:", str(female_count))

    def unique_region(self):
    	unique = []

    	for element in self.patient_region:
    		if element not in unique:
    			unique.append(element)
    	return unique

    def average_charges(self):

    	total_charges = 0 

    	for element in self.patient_charge:

    		total_charges += float(element)
    	return ("Average Yearly Medical Insurance Charges: " +  
                str(round(total_charges/len(self.patient_charge), 2)) + " dollars.")

    def average_gender(self):

    	total_male = []
    	total_female = []

    	for element in self.patient_sex:

    		if element == 'male':
    			total_male.append(element)
    	
    		elif element == 'female':
    			total_female.append(element)

    	print("According in our data set we have got total of males", len(total_male),
    	 "average Male", round(len(total_male) / len(self.patient_sex), 2))

    	print("According in our data set we have got total of Females", len(total_female),
    	 "average Female", round(len(total_female) / len(self.patient_sex), 2))

			




patients = PatientInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patients.update_children(1)
patients.update_smoke(1)
patients.change_of_sex('Male')
patients.analyze_ages()
patients.gender_count()
print(patients.unique_region())
print(patients.average_charges())
patients.average_gender()
patients.average_smoker()
patients.create_dictionary()
