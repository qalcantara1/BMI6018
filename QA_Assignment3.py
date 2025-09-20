#!/usr/bin/env python
# coding: utf-8

# # BMI 6018 - Fall 2025

# ##### Queren Alcantara

# In[1]:


#Start your assignment here
print("Assignment 3")


# In[2]:


#Problem 1
print("1.a") #Create a list of integers
my_integers = list(range(10))
print(my_integers)


# In[3]:


print("1.b") #Add 3 to the 5th indexed element (index number 5).
my_integers.insert(5,3)
print(my_integers)


# In[4]:


print("1.c") #Coerce all elements in the list to floats using list comprehension
coerced_floats = [float(elements) for elements in my_integers]
print(coerced_floats)


# In[5]:


print("1.d") #Coerce the list to a set. So I will use the initial list.
coerced_sets = {elements for elements in my_integers}
print(coerced_sets)


# In[6]:


print("1.e") #Using a method, append int 10 to the set
coerced_sets.add(10)
print(coerced_sets)


# In[7]:


print("1.f") #Using a method, pop an item from the set
coerced_sets.pop()
print(coerced_sets)


# In[8]:


print("1.g") #Using a length counting function, count the number of items in the set
print(len(coerced_sets))


# In[9]:


print("1.h") #Check if the number of items in the set is the same as the number of items in the list
len(coerced_sets) == len(my_integers) #Do they have the same number of elements?


# In[10]:


print("1.i") #Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
set_list = [elements for elements in coerced_sets] #set to list
print (set_list)
combined_list = set_list + my_integers #joining list
print(combined_list)


# In[11]:


print("1.j") #Coerce 1.i to a set
combined_set = {elements for elements in combined_list}
print(combined_set)


# In[12]:


print("1.k") #Count the number of elements in the 1.j
print(len(combined_set))


# In[13]:


#Problem 2


# In[14]:


print("2.a") #Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named two_a, ensure the key names are the same as the dictionary names.
two_a = {"two_patient_dictionary_kinoko": {
              "name" : "Kinoko",
              "year" : 2021
        },
        "two_patient_dictionary_dango": {
              "name" : "Dango",
              "year" : 2019
        },
        "two_patient_dictionary_mochi": {
              "name" : "Mochi",
              "year" : 2020
        }
    }
print(two_a)


# In[15]:


print("2.b") #Using keys, retrieve the Dango's name from 2.a
print(two_a["two_patient_dictionary_dango"]["name"])


# In[16]:


print("2.c") #Using keys, update the value of Mochi's year to 2018. This should not be a variable and should simply update 2.a.
two_a["two_patient_dictionary_mochi"]["year"] = 2018
print(two_a) #checking the change


# In[17]:


print("2.d") #Manually create a dictionary that has a single level and contains each patient as the key and the year as the value. Set Mochi's year to 2019.'

patients_dict = {"Kinoko": 2021,
                "Dango": 2019,
                "Mochi": 2019}
print(patients_dict)


# In[18]:


print("2.e") #Coerce the keys of 2.d into a list
patients_list = [elements for elements in patients_dict.keys()]
print(patients_list)


# In[19]:


print("2.f") #Coerce the values of 2.d into a list
patients_values_list = [elements for elements in patients_dict.values()]
print(patients_values_list)


# In[20]:


print("2.g") #Use the zip function to combine 2.e and 2.f into a dictionary again
second_dict = dict(zip(patients_list,patients_values_list))
print(second_dict)


# In[21]:


#Problem 3
 
#Set objects
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}


# In[22]:


print("3.a") #Is set E a subset of set A
three_setE <= three_setA


# In[23]:


print("3.b") #Is set E a strict subset of set A
three_setE < three_setA


# In[24]:


print("3.c") #Create a set that is the intersection of set A and set B
intersectionAB = three_setB.intersection(three_setA)
print(intersectionAB)


# In[25]:


print("3.d") #Create a set that is the union of sets C, D and E
unionCDE = three_setC.union(three_setD, three_setE)
print(unionCDE)


# In[26]:


print("3.e") #add 9 to the set
unionCDE.add(9)
print(unionCDE)


# In[27]:


print("3.f") #Using == compare this set to the list in one_a
one_a = list(range(10))
unionCDE == one_a


# In[28]:


print("3.g") #Explain why they are not the same. What would you need to change if you wanted this to be True?

print("The objects are different because the object from 3.e does not have the value 0")
print(one_a)
print(unionCDE)

print("To change that, I would need to change the set to a list, add a 0 in the first index position, and then compare them")


# In[29]:


#Problem 4


# In[30]:


print("4.a") #Create a variable of type int with the value of 8
variable = 8
print(variable)


# In[31]:


print("4.b") #Create an empty list 
four_b = []
print(four_b)


# In[32]:


print("4.c") #Using type(), add the type of 4.a to this list
first_type = type(variable)
four_b.append(first_type)
print(four_b)


# In[33]:


print("4.d") #Add 0.39 to 4.c
four_b.append(0.39)
print(four_b)


# In[34]:


print("4.e") #append the type of 0.39 to the list
second_type = type(0.39)
four_b.append(second_type)
print(four_b)


# In[35]:


print("4.f") #exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no decimal places, and append to list.
exponential = 4**-10
rounded_expo = round(exponential)
four_b.append(rounded_expo)
print(four_b)


# In[36]:


print("4.g") #append the type to the list
third_type = type(rounded_expo)
four_b.append(third_type)
print(four_b)


# In[37]:


#Problem 5


# In[38]:


print("5.a") #Manually create a dictionary where the values are items in the list from where we left in problem 4, and the keys should be their index in the list. Print the dictionary.
five_a_list = len(four_b)
five_a_dict = dict(zip(range(five_a_list),four_b))
print(five_a_dict)


# In[39]:


print("5.b") #Add 300 and coerce it into a string
four_b.append(str(300))
print(four_b)


# In[40]:


print("5.c") #append the type to the list
four_b.append(type(four_b[-1]))
print(four_b)


# In[41]:


print("5.d") #slice the string up to the 2nd element
sliced_string = four_b[-2][:2] 
print(sliced_string)


# In[42]:


print("5.e") #append the type to the list
fourth_type = type(sliced_string)
four_b.append(fourth_type)
print(four_b)


# In[43]:


print("5.f") #use list comprehension to convert this into a new list of integers
original_items = [0.39, 0, '300']
new_integers = [int(element) for element in original_items]

print(new_integers)


# In[44]:


print("5.g") #append the type to the list
four_b.append(type(new_integers))
print(four_b)


# In[45]:


print("5.h") #append the type of three_setA to the list
four_b.append(type(three_setA))
print(four_b)


# In[ ]:




