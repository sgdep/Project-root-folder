import re                       #Used for Regular Expression.
import json                     #Used at the end for dumping output to result.json file
from functools import reduce    #Used later to convert nested list to list.


counts = dict()                 #Created a main dicionary
emails_tentative = list()       #Created a list 

# The code below opens the files, search for email adds email found to a list called emails_tentative. 
fhand1 = open('websiteData.txt','r', encoding = 'utf-8') 
for line in fhand1:
    if not "@" in line:
        continue
    email_found = re.findall(r"[A-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line) #This code filters the valid email from any word that has "@"
    emails_tentative.append(email_found)

emails_nestedlist = [x for x in emails_tentative if x != []] #This line removes any empty list from emails_tentative and assigns the remaining list to emails_nestedlist.
final_emails = reduce(lambda x,y: x+y, emails_nestedlist) #This line converts the nested list into list.

#The code below goes through the final_emails list and create nested dictionary with email, Occourance and EmailType.
for email in final_emails:
    username = email[:email.index("@")]     # THis line seperates username from email so that conditions can be checked later.    
    if email in counts:
        counts[email]["Occurance"] = counts[email]["Occurance"] + 1         
    else:
        dict1 = dict()                 #This line creates a sub dictionary, which is later assigned key and values.  
        dict1["Occurance"] = 1
        counts[email] = dict1          #Entire dictionary is assigned as value to the "email" key of main dictionary counts.
        if len(username) >= 8 and '.' in username:
            counts[email]["EmailType"] = "Human"
        else:
            counts[email]["EmailType"] = "Non-Human"
        

#The code below creates result.json file and writes the data of counts dictionary.
fhand2 = open("result.json", "w")
json.dump(counts, fhand2, indent = 4) 
fhand2.close()

