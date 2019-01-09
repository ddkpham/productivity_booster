#MODIFY THIS TO ADD WEBSITES VIA USER INPUT AS WELL AS USER START TIMES 

import time
from datetime import datetime as dt
#Path to hosts file on Mac
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com", "reddit.com", "www.reddit.com", "mangastream.com", "www.mangastream.com"] 

#Run Script Indefinitely
while True:
    #Set start and end time for website blocker
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)
    

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