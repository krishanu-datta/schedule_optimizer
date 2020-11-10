#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Please fill in the blank with the address of your class schedule:
### for example: class_schedule.csv
schedule = 'class_schedule.csv'
preferences = []


# In[2]:


### Please fill in the blank with the name of your first choice class
first_choice = 'Computer Science'
preferences.append(first_choice)


# In[3]:


### Please fill in the blank with the name of your second choice class
second_choice = 'Computer Science'
preferences.append(second_choice)


# In[4]:


### Please fill in the blank with the name of your third choice class
third_choice = 'Chemistry'
preferences.append(third_choice)


# In[5]:


### Please fill in the blank with the name of your fourth choice class
fourth_choice = 'History'
preferences.append(fourth_choice)


# In[6]:


### Please fill in the blank with the name of your fifth choice class
fifth_choice = 'French'
preferences.append(fifth_choice)


# In[7]:


### What is the maximum number of STEM classes you want to take?
max_stem = 2


# In[8]:


### What is the maximum number of Arts classes you want to take?
max_art = 1


# In[9]:


### What is the maximum number of Foreign Language classes you want to take?
max_lang = 1


# In[10]:


### List the professors you would like to avoid in order starting with least preferred:
bad_prof = ['Cleveland','Ike']


# In[11]:


### List the professors you would like to have in order starting with most preferred:
good_prof = ['Adams','Buchanan']


# In[12]:


import pandas as pd
df = pd.read_csv(schedule)


# In[13]:


### calculates the number of CNF clauses that will exist in the file
time_slot = 1;
max_weight = 30
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
    return int(count);
findCount()


# In[14]:


### prints the header information needed for the SAT4j MAX-SAT Solver
print("p wcnf", end=' ')
print(df.index.size, end=' ')
print(findCount(), end=' ')
print(max_weight)


# In[15]:


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


# In[16]:


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


# In[21]:


tweight = 20;
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


# In[23]:


if max_art == 2:
    al = df[df["Class Type"] == "Liberal Arts"]["Class ID"].values.tolist()
    print(tweight, end=" ")
    for x in al:
        print(x, end=" ")
    print("0")
    
    for i in range(0,len(sl)):
        print(tweight, end=" ")
        for x in al:
            if x == al[i]:
                print(-x, end=" ")
            else:
                print(x, end=" ")
        print("0")    
        i += 1;
elif max_art == 1:
    al = df[df["Class Type"] == "Liberal Arts"]["Class ID"].values.tolist()
    for i in range(0,len(al)):
        for j in range(i+1,len(al)):
            print(max_weight, end=" ")
            print(-al[i], end=' ')
            print(-al[j], end=' ')
            print("0")
            j += 1;
        i += 1;


# In[25]:


if max_lang == 2:
    ll = df[df["Class Type"] == "Foreign Language"]["Class ID"].values.tolist()
    print(tweight, end=" ")
    for x in ll:
        print(x, end=" ")
    print("0")
    
    for i in range(0,len(ll)):
        print(tweight, end=" ")
        for x in ll:
            if x == ll[i]:
                print(-x, end=" ")
            else:
                print(x, end=" ")
        print("0")    
        i += 1;
elif max_lang == 1:
    ll = df[df["Class Type"] == "Foreign Language"]["Class ID"].values.tolist()
    for i in range(0,len(ll)):
        for j in range(i+1,len(ll)):
            print(max_weight, end=" ")
            print(-ll[i], end=' ')
            print(-ll[j], end=' ')
            print("0")
            j += 1;
        i += 1;


# In[27]:


prof_weight = 5;
for x in good_prof:
    profl = df[df["Professor"] == x]["Class ID"].values.tolist()
    for y in profl:
        print(prof_weight, end=" ")
        print(y, end=" ")
        print("0")
    prof_weight -= 1;


# In[28]:


prof_weight = 5;
for x in bad_prof:
    profl = df[df["Professor"] == x]["Class ID"].values.tolist()
    for y in profl:
        print(prof_weight, end=" ")
        print(-y, end=" ")
        print("0")
    prof_weight -= 1;


# In[ ]:


### creates wcnf file with information printed in DIMACS notation
import sys
orig_stdout = sys.stdout
f = open('sample.wcnf', 'w')
sys.stdout = f
print("Hello World")
sys.stdout = orig_stdout
f.close()


# In[ ]:


### runs the SAT4j MAX-SAT solver in a command shell
import subprocess
out = subprocess.check_output(['java', '-jar', 'sat4j-maxsat.jar', 'classes.wcnf']).decode('utf-8').split('\n')
out


# In[ ]:


### processes the output and shows the corresponding rows of class information from the dataframe
answer = []
for i in range(1, len(out[len(out) - 4].split()) - 1):
    x = int(out[len(out) - 4].split()[i])
    if x > 0:
        answer.append(x)
answer


# In[ ]:


df = pd.read_csv(schedule)
df[df["Class ID"].isin(answer)].sort_values(by=["Time Slot"])


# In[ ]:


out[len(out) - 2][1:43]


# In[ ]:




