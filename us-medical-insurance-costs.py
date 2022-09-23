#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[1]:


import csv


# In[2]:


insurance_list = []
columns = []
ages = []
regions_unique = []
regions = []
bmis = []
costs = []
genders = []
smoker = []
children = []
with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    for row in insurance_dict:
        insurance_list.append(row)
        if columns == []:
            columns = list(row.keys())
        ages.append(row['age'])
        regions.append(row['region'])
        if not row['region'] in regions_unique:
            regions_unique.append(row['region'])
        bmis.append(row['bmi'])
        costs.append(row['charges'])
        genders.append(row['sex'])
        smoker.append(row['smoker'])
        children.append(row['children'])


# In[3]:


# I want to know if the dataset has roughly the same number of males and females
def get_gender_ratio(gender_list):
    male = 0
    female = 0
    for sex in gender_list:
        if(sex =='male'):
            male += 1
        elif(sex == 'female'):
            female += 1
    return {'male': male/len(gender_list), 'female': female/len(gender_list)}
print(get_gender_ratio(genders))


# In[10]:


# I want to know if there are more male smokers than female
def calc_gender_smoker_ratio(gen_list, smok_list):
    male_smokers = 0
    female_smokers = 0
    for index in range(len(gen_list)):
        if gen_list[index] == 'male':
            if smok_list[index] == 'yes':
                male_smokers += 1
        elif gen_list[index] == 'female':
            if smok_list[index] == 'yes':
                female_smokers += 1
    return {'male-smokers': male_smokers, 'female-smokers': female_smokers}
gen_smokers = calc_gender_smoker_ratio(genders, smoker)
print("There are {} male smokers and {} female smokers".format(gen_smokers['male-smokers'], gen_smokers['female-smokers']))


# In[18]:


# I want to know if the average bmi for people with children is higher than those without children
def avg_bmi_children(bmi_list, child_list):
    children_bmis = []
    no_children_bmis = []
    child_total = 0
    no_child_total = 0
    for index in range(len(bmi_list)):
        if int(child_list[index]) > 0:
            children_bmis.append(bmi_list[index])
            child_total += float(bmi_list[index])
        elif int(child_list[index]) == 0:
            no_children_bmis.append(bmi_list[index])
            no_child_total += float(bmi_list[index])
    return {'children': round(child_total/len(children_bmis), 2), 'no_children': round(no_child_total/len(no_children_bmis),2)}
bmi_children_avgs = avg_bmi_children(bmis, children)
print("The average bmi for someone with children is {} while the average for someone with no children is {}.".format(bmi_children_avgs['children'],bmi_children_avgs['no_children']))


# In[42]:


# I want to know the average insurance cost for each region
def avg_cost_per_region(cost_list, region_list):
    totals = {'southwest': 0, 'southeast': 0, 'northwest':0, 'northeast':0}
    entries = {'southwest': 0, 'southeast': 0, 'northwest':0, 'northeast':0}
    for index in range(len(region_list)):
        totals[region_list[index]] += float(cost_list[index])
        entries[region_list[index]] += 1
    
    avgs = {'southwest': totals['southwest']/entries['southwest'], 'southeast': totals['southeast']/entries['southeast'], 'northwest':totals['northwest']/entries['northwest'], 'northeast':totals['northeast']/entries['northeast']}
    return avgs
average_costs_per_region = avg_cost_per_region(costs, regions)
for region in regions_unique:
    print("Average cost for the {} region is ${}".format(region,round(average_costs_per_region[region],2)))


# In[37]:


# I want to know if the average and the IQR average of the costs list are similar
def get_iqr_avg(cost_list):
    length = len(cost_list)
    iqr_values = cost_list[int(length/4)-1:int(length-length/4)-1]
    iqr_total = 0
    for value in iqr_values:
        iqr_total += float(value)
    return iqr_total/len(iqr_values)
iqr_avg = get_iqr_avg(costs)
def get_avg(values):
    total = 0
    for value in values:
        total += float(value)
    return total/len(values)
avg = get_avg(costs)
print("The average cost of insurance is ${} while the IQR average is ${}.".format(round(avg, 2), round(iqr_avg, 2)))


# In[41]:


# I want to know if the median and the median of the IQR are similar
def iqr_med(cost_list):
    length = len(cost_list)
    iqr_values = cost_list[int(length/4)-1:int(length-length/4)-1]
    return iqr_values[int(len(iqr_values)/2) -1]
iqr_median = iqr_med(costs)
def med(values):
    return values[int(len(values)/2)]
median = med(costs)
print("The median insurance cost is ${} while the median of the IQR is ${}".format(round(float(median),2), round(float(iqr_median),2)))

