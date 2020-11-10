#!/usr/bin/env python
# coding: utf-8

# In[22]:


### Please fill in the blank with the local address of your class schedule:
## The data should be inputted as a string. For example: class_schedule.csv
schedule = 'class_schedule.csv'
preferences = []


### Please fill in the blank with the name of your first choice class
## The data should be inputted as a string, and should appear as a class in the supplied schedule
first_choice = 'Computer Science'
preferences.append(first_choice)


### Please fill in the blank with the name of your second choice class
## The data should be inputted as a string, and should appear as a class in the supplied schedule
second_choice = 'Math'
preferences.append(second_choice)


### Please fill in the blank with the name of your third choice class
## The data should be inputted as a string, and should appear as a class in the supplied schedule
third_choice = 'Chemistry'
preferences.append(third_choice)


### Please fill in the blank with the name of your fourth choice class
## The data should be inputted as a string, and should appear as a class in the supplied schedule
fourth_choice = 'Biology'
preferences.append(fourth_choice)


### Please fill in the blank with the name of your fifth choice class
## The data should be inputted as a string, and should appear as a class in the supplied schedule
fifth_choice = 'French'
preferences.append(fifth_choice)


### What is the maximum number of STEM classes you want to take?
## The data should be inputted as a integer value in the range 1 to 3.
max_stem = 3


### What is the maximum number of Arts classes you want to take?
## The data should be inputted as a integer value in the range 1 to 3.
max_art = 1


### What is the maximum number of Foreign Language classes you want to take?
## The data should be inputted as a integer value in the range 1 to 3.
max_lang = 1

### List the professors you would like to avoid in order starting with least preferred:
## The data should be inputted as comma separated strings,
## and the strings should appear as professors in the supplied schedule
bad_prof = ['Cleveland','Ike']

### List the professors you would like to have in order starting with most preferred:
## The data should be inputted as comma separated strings,
## and the strings should appear as professors in the supplied schedule
good_prof = ['Adams','Buchanan']


# In[26]:


import pandas as pd
def class_optimizer():
    
### procceses imported schedule
    df = pd.read_csv(schedule)
    time_slot = 1;
    max_weight = 30
    
### calculates the number of CNF clauses that will exist in the file
    def findCount():
        slot_value = 1;
        count = 0;
        while slot_value < 5:
            n = df[df["Time Slot"] == slot_value]["Class ID"].size
            count = count + ((n * (n-1) / 2) + 1)
            slot_value += 1;
        for x in preferences:
            n = df[df["Subject"] == x]["Class ID"].size
            count = count + ((n * (n-1) / 2) + 1)
        for x in good_prof:
            n = df[df["Professor"] == x]["Class ID"].size
            count = count + n
        for x in bad_prof:
            n = df[df["Professor"] == x]["Class ID"].size
            count = count + n
      #  m = df[df["Class Type"] == "STEM"]["Class ID"].size
      #  count = count + (m * (m-1) / 2)
        return int(count);
    
### prints the header information needed for the SAT4j MAX-SAT Solver
    print("p wcnf", end=' ')
    print(df.index.size, end=' ')
    print(findCount(), end=' ')
    print(max_weight)

### prints the clauses for time slot constraints
    while time_slot < 5:
        ts = df[df["Time Slot"] == time_slot]["Class ID"].values.tolist()
        
## picks one class from time slot
        print(max_weight, end=" ")
        for x in ts:
            print(x, end=' ')
        print("0")
        
## at most one class from each time slot
        for i in range(0,len(ts)):
            for j in range(i+1,len(ts)):
                print(max_weight, end=" ")
                print(-ts[i], end=' ')
                print(-ts[j], end=' ')
                print("0")
                j += 1;
            i += 1;
        time_slot += 1;

### prints the clauses for the subject preference constraints
    pweight = 10;
    for x in preferences:
        pl = df[df["Subject"] == x]["Class ID"].values.tolist()
        
## picks one class per subject with corresponding weight
        print(pweight, end=" ")
        for x in pl:
            print(x, end=" ")
        print("0")
        
## at most one class per subject
        for i in range(0,len(pl)):
            for j in range(i+1,len(pl)):
                print(max_weight, end=" ")
                print(-pl[i], end=' ')
                print(-pl[j], end=' ')
                print("0")
                j += 1;
            i += 1;
        pweight -= 1;
    tweight = 30;
    if max_stem == 2:
        sl = df[df["Class Type"] == "STEM"]["Class ID"].values.tolist()
        print(tweight, end=" ")
        for x in sl:
            print(x, end=" ")
        print("0")
    
        for i in range(0,len(sl)):
            print(tweight, end=" ")
            for x in sl:
                if x == sl[i]:
                    print(-x, end=" ")
                else:
                    print(x, end=" ")
            print("0")    
            i += 1;
    elif max_stem == 1:
        sl = df[df["Class Type"] == "STEM"]["Class ID"].values.tolist()
        for i in range(0,len(sl)):
            for j in range(i+1,len(sl)):
                print(max_weight, end=" ")
                print(-sl[i], end=' ')
                print(-sl[j], end=' ')
                print("0")
                j += 1;
            i += 1;
    prof_weight = 5;
    for x in good_prof:
        profl = df[df["Professor"] == x]["Class ID"].values.tolist()
        for y in profl:
            print(prof_weight, end=" ")
            print(y, end=" ")
            print("0")
        prof_weight -= 1;
    prof_weight = 5;
    for x in bad_prof:
        profl = df[df["Professor"] == x]["Class ID"].values.tolist()
        for y in profl:
            print(prof_weight, end=" ")
            print(-y, end=" ")
            print("0")
        prof_weight -= 1;


# In[27]:


### creates wcnf file with information printed in DIMACS notation
import sys
orig_stdout = sys.stdout
f = open('classes.wcnf', 'w')
sys.stdout = f
class_optimizer()
sys.stdout = orig_stdout
f.close()

### runs the SAT4j MAX-SAT solver in a command shell
import subprocess
out = subprocess.check_output(['java', '-jar', 'sat4j-maxsat.jar', 'classes.wcnf']).decode('utf-8').split('\n')

### processes the output and shows the corresponding rows of class information from the dataframe
answer = []
for i in range(1, len(out[len(out) - 4].split()) - 1):
    x = int(out[len(out) - 4].split()[i])
    if x > 0:
        answer.append(x)
df = pd.read_csv(schedule)
df[df["Class ID"].isin(answer)].sort_values(by=["Time Slot"])


# In[7]:


out[len(out) - 2][1:43]


# In[ ]:




