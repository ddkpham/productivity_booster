#MODIFY THIS TO ADD WEBSITES VIA USER INPUT AS WELL AS USER START TIMES 

import time
import math
from datetime import datetime as dt
#Path to hosts file on Mac
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = [] 

#Converts 24 hour time to 12 hour time 
def timeConversion(int):
    if int > 12:
        int = int-12
        return str(int) +":00 pm"
    else:
        if int == 12:
            return str(int) +":00 pm"
        else:
            return str(int) +":00 am"

#Grab start time and end time for when websites should be restricted
def hello_statement():
    print('Hello! \n\nBoost your productivity by blocking distracting websites!')
    print('Please enter the hour of when you would like to start being productive.')
    print('\nExample: Enter "8" for 8:00 am || Enter "13" for 1:00pm')


#Choose websites to block 
def website_statements():
    print("Please enter the websites you wish to block one at a time:")
    print("Example: www.cuddlycats.com OR cuddlycats.com will work")

#START TIME CONFIRMATION 
def get_start_time():
    start = int(raw_input('Please enter your start time now...\n'))
    while(start < 0 or start > 24):
        print('\nInvalid start time. Try to pick a time between 0 and 24')
        start = int(raw_input('Please enter your start time now...\n'))
        #print(start)
    return start

#Function returns 1 on success asks for a new start time on fail 
def response_check(response):
    if response == 'y':
        #Response confirmed
        pass
    elif response =='n':
        print("Oops... Try entering your time again")
        start = get_start_time()
        start_time_confirm(start)
    else:
        print('Please enter either "Y" or "N" only please')
        response = raw_input('Enter "Y" for Yes and Enter "N" for No\n')
        response = str(response.lower())
        response_check(response)


def start_time_confirm(start):
    print("You have entered: " + str(start) + " which is " + timeConversion(start) + "...")
    print("Is this the correct start time?")
    response = raw_input('Enter "Y" for Yes and Enter "N" for No\n')
    response = str(response.lower())
    #print(response)
    response_check(response)

# END TIME CONFIRMATION 
def get_end_time():
    print('Please follow the same format for entering when you would like your productivity to end!')
    end = int(raw_input('Please enter your end time now...\n'))
    while(end < 0 or end > 24):
        print('\nInvalid start time. Try to pick a time between 0 and 24')
        end = int(raw_input('Please enter your end time now...\n'))
        #print(end)
    return end

def end_time_confirm(end):
    print("You have entered: " + str(end) + " which is " + timeConversion(end) + "...")
    print("Is this the correct end time?")
    response = raw_input('Enter "Y" for Yes and Enter "N" for No\n')
    response = str(response.lower())
    #print(response)
    response_check(response)

def user_website_input():
    website = raw_input('Enter "X" to exit\n')
    website = website.lower()
    while (website != 'x'):
        #Website not in website list
        if website not in website_lists:
            prefix_check = 'www.'
            if prefix_check not in website:
                website_lists.append(website)
                website = 'www.'+ website
                website_lists.append(website)
            else:
                website_lists.append(website[4:])
                website_lists.append(website)
        else:
            print("Website already in block list")

        website = raw_input('Enter another website or hit "X" to exit\n')
        website = website.lower()

#-----------------------------------MAIN PROGRAM------------------------------------#
hello_statement()

#Get Start Time of webblocker
start = get_start_time()
start_time_confirm(start)

#Get End Time of weblocker
end = get_end_time()
end_time_confirm(end)

#Check to see if start time and end time is valid 
while(start > end):
    print("\nERROR! Make sure your end time is after your start time")    
    #Get Start Time 
    print('Please enter the hour of when you would like to start being productive.')
    print('\nExample: Enter "8" for 8:00 am || Enter "13" for 1:00pm')
    start = get_start_time()
    start_time_confirm(start)

    #Get End Time 
    end = get_end_time()
    end_time_confirm(end)

#Obtain list of distracting websites user wishes to block
website_statements()    
user_website_input()

#Run Script Indefinitely
while True:
    #Set start and end time for website blocker
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, start)
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, end)
    

    if start_time < dt.now() < end_time:
        print("Working Hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            #print(content)
            for website in website_lists:
                if website in content:
                    print("website already blocked")
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    print(website + " has been blocked " + "\n")
    else:
        print("Put on your party pants work is over!")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            #Place read pointer at first char
            file.seek(0)
            #print(content)
            for line in content:
                #print(line)
                #time.sleep(1)
                if not any(website in line for website in website_lists):
                    file.write(line)
            #Delete the rest of the old content
            file.truncate()
    print(start_time)
    print(end_time)
    time.sleep(300)