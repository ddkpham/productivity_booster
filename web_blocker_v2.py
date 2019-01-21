import time
from Tkinter import *
import time
import math
import os
import platform
from datetime import datetime as dt


#Path to hosts file on Mac
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_lists = [] 
hour_check= []
min_check = []

#Obtains host path based on OS system of Device
def host_path():
    os = platform.system()
    os = os.lower()
    if 'darwin' in os:
        hosts_path = "/etc/hosts"
        print("MacOS...host file set")
    elif 'linux' in os:
        hosts_path = "/etc/hosts"
        print("Linux...host file set")
    else: 
        hosts_path = "c:\Windows\System32\Drivers\etc\hosts"
        print("Windows...host file set") 

    return hosts_path



# this must return soon after starting this
def change_text():
    label['text'] = time.asctime() 

    # now we need to run this again after one second, there's no better
    # way to do this than timeout here
    root.after(1000, change_text)


#Continually checks time to see if it is time to unblock website

#Set Hosts path for website Domain name redirection 
hosts_path = host_path()
valid_time = False
#Declare Tkinter Object
root = Tk()
root.title('Productivity Booster')

#Declare a Frame to place objects in 
big_frame = Frame(root)
big_frame.pack(fill='both', expand=True)

welcome_label = Label(big_frame, text='Welcome to the Productivity Booster App')
welcome_label.grid(row=0,column=0, sticky=W)

label = Label(big_frame, text='Current Time', fg="black", bg="white")
label.grid(row=1, column=0, sticky= W)

label = Label(big_frame, text='0', fg="black", bg="white")
label.grid(row=1, column=1, sticky= W)

intro_label = Label(big_frame, text='Entering Start/End times. Ex 8:15 am = 8:15 || 5:35 pm = 17:35 ', fg="black", bg="white")
intro_label.grid(row=2, column=1, sticky= W)

#Checks if start and end times are valid. Provides feedback according. 
#FIX Valid/Invalid time label text. Text needs to be checked then deleted before relabel
#Refactor
def time_check():
    start = start_time.get()
    end = end_time.get()
    start = start.split(':')
    end = end.split(':')
    global hour_check
    global min_check
    hour_check = [int(start[0]), int(end[0])]
    min_check = [int(start[1]), int(end[1])]
    for time in hour_check:
        print(time)
        if(0<= time <=24):
            print("valid hour")
        else:
            print("invalid hour")
            global valid_time
            valid_time = False
            valid_time_label = Label(big_frame, text="Invalid")
            valid_time_label.grid(row=3, column=1, sticky=E)
            return
    for time in min_check:
        print(time)
        if(0<= time <=60):
            print("valid minutes")
        else:
            print("invalid minutes")
            global valid_time
            valid_time = False
            valid_time_label = Label(big_frame, text="Invalid oop")
            valid_time_label.grid(row=3, column=1, sticky=E)
            return
    if(hour_check[0] > hour_check[1]):
        print("invalid start and end times")
        global valid_time
        valid_time = False
        valid_time_label = Label(big_frame, text="Invalid oop")
        valid_time_label.grid(row=3, column=1, sticky=E)
        return
    elif (hour_check[0]== hour_check[1]):
        if min_check[0] > min_check[1]:
            print("invalid start and end times")
            global valid_time
            valid_time = False
            valid_time_label = Label(big_frame, text="Invalid oop")
            valid_time_label.grid(row=3, column=1, sticky=E)
            return
        else:
            print("valid start and end times ::A")
            global valid_time
            valid_time = True
            print(valid_time)
            start_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[0], min_check[0])
            end_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[1], min_check[1])
            print(start_block_time)
            print(end_block_time)
            valid_time_label = Label(big_frame, text="Valid Times")
            valid_time_label.grid(row=3, column=1, sticky=E)
    else:
        print("valid start and end times ::B")
        global valid_time
        valid_time = True
        print(valid_time)
        start_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[0], min_check[0])
        end_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[1], min_check[1])
        print(start_block_time)
        print(end_block_time)
        valid_time_label = Label(big_frame, text="Valid Times")
        valid_time_label.grid(row=3, column=1, sticky=E)



#Set up Time Entry boxes
start_label = Label(big_frame, text='Start Time', fg="black", bg="white")
start_label.grid(row=3, column=0, sticky= W)

start_time = Entry(big_frame)
start_time.grid(row=3, column=1, sticky=W)

end_label = Label(big_frame, text='End Time', fg="black", bg="white")
end_label.grid(row=4, column=0, sticky= W)

end_time = Entry(big_frame)
end_time.grid(row=4, column=1, sticky=W)

time_confirm_btn = Button(big_frame, text="Time Check", command=time_check)
time_confirm_btn.grid(row=5, sticky=W)

#Set up Website Lists
website_label = Label(big_frame, text="Enter Websites to be blocked followed by newline")
website_label.grid(row=6, sticky=W)

website_list = Text(big_frame, height=20, width=30)
website_list.grid(row=7, sticky=W)

def website_check():
    websites = website_list.get("1.0", "end-1c")
    websites = websites.split('\n')
    print(websites)
    for element in websites:
        if ".com" in element:
            if element not in website_lists:
                print('website confirmed')
                website_lists.append(element)
        elif ".ca" in element:
            if element not in website_lists:
                print('website confirmed')
                website_lists.append(element)
        elif ".org" in element:
            if element not in website_lists:
                print('website confirmed')
                website_lists.append(element)
        else:
            print("not a website")
    print(website_lists)
    print(valid_time)
    
    #valid_time stays FALSE! 
    if valid_time==True:
        print(hour_check)
        print(min_check)
        start_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[0], min_check[0])
        end_block_time = dt(dt.now().year, dt.now().month, dt.now().day, hour_check[1], min_check[1])
        if start_block_time < dt.now() < end_block_time:
            print("Working Hours...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                #print(content)
                for website in website_lists:
                    if website in content:
                        print("website already blocked")
                        pass
                    else:
                        if 'www' in website:
                            file.write(redirect + " " + website + "\n")
                            file.write(redirect + " "  + website[4:] + "\n")
                            print(website + " has been blocked " + "\n")
                        else:
                            file.write(redirect + " " + website + "\n")
                            file.write(redirect + " " + "www." + website + "\n")
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

    else:
        print("Set start and end times improperly")
    
    root.after(300000, website_check)


#Set up Confirm Button 
website_confirm_btn = Button(big_frame, text="BLOCK WEBSITES", command=website_check)
website_confirm_btn.grid(row=8, sticky=W)




change_text()      # don't forget to actually start it :)

root.geometry('700x600')
root.mainloop()