#MODIFY THIS TO ADD WEBSITES VIA USER INPUT AS WELL AS USER START TIMES 

import time
import math
from datetime import datetime as dt
#Path to hosts file on Mac
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com", "reddit.com", "www.reddit.com", "mangastream.com", "www.mangastream.com"] 

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
print('Hello! \n\nBoost your productivity by blocking distracting websites!')
print('Please enter the hour of when you would like to start being productive.')
print('\nExample: Enter "8" for 8:00 am || Enter "13" for 1:00pm')

#START TIME CONFIRMATION 
def get_start_time():
    start = int(raw_input('Please enter your start time now...\n'))
    while(start < 0 or start > 24):
        print('\nInvalid start time. Try to pick a time between 0 and 24')
        start = int(raw_input('Please enter your start time now...\n'))
        print(start)
    return start
 
def response_check(response):
    if response == 'y':
        return 1
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
    print(response)
    response_check(response)

# END TIME CONFIRMATION 
def get_end_time():
    print('Please follow the same format for entering when you would like your productivity to end!')
    end = int(raw_input('Please enter your end time now...\n'))
    while(end < 0 or end > 24):
        print('\nInvalid start time. Try to pick a time between 0 and 24')
        end = int(raw_input('Please enter your end time now...\n'))
        print(end)
    return end

def end_time_confirm(end):
    print("You have entered: " + str(end) + " which is " + timeConversion(end) + "...")
    print("Is this the correct end time?")
    response = raw_input('Enter "Y" for Yes and Enter "N" for No\n')
    response = str(response.lower())
    print(response)
    response_check(response)

#Get Start Time 
start = get_start_time()
start_time_confirm(start)

#Get End Time 
end = get_end_time()
end_time_confirm(end)

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