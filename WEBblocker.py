# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:27:49 2022

@author: Deesc
"""
from tkinter import *
from tkinter.messagebox import *
from datetime import datetime as dt
import time 

root = Tk()

root.geometry('400x300')
root.configure(bg="ghost white")
root.title("Deesc - Website Blocker")
root.resizable(True,True)

Label(root, text = 'Website Blocker', font = 'arial 20 bold', bg = 'white smoke').pack()
Label(root,text ="Deesc Gdams", font = 'arial 8 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Button(root, text= 'Block Site', font = 'helvetica 12 bold', bg = 'red', command=lambda: block(root)).place(x=150,y=100)
Button(root, text ='Unblock Site', font = 'helvetica 12 bold', command=lambda: unblock(root)).place(x=140, y=150)




host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = '127.0.0.1'

def block(win):
    blck_wn = Toplevel(win, background='LightBlue')
    blck_wn.title("Block a website")
    blck_wn.geometry('320x350')
    blck_wn.resizable(True, True)
    
    
    Label(blck_wn, text='Block websites', background='LightBlue', font=("Georgia", 12,'bold')).pack()
    #place(x=80, y=0)
    Label(blck_wn, text='Enter the websites separated by commas, ONLY', background='LightBlue', font=("Georgia", 10)).pack()
    #place(x=0, y=35)
    Label(blck_wn, text='Enter the URLs (www.<sitename>.com):', background='LightBlue', font=('Georgia', 10)).pack()
    #place(x=0, y=70)
    entry_sites = Text(blck_wn, width=35, height=3,pady=10)
    entry_sites.pack()
    #place(x=20, y=100)
    Label(blck_wn,text ="Deesc Gdams", font = 'arial 8 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
    
    submit_btn = Button(blck_wn, text='Block without time constraints', command=lambda: (block_websites(blck_wn, entry_sites.get('1.0',END))  if not (entry_sites.get('1.0',END)==0)  else (showinfo('Error!', message = 'The site list cannot be empty before submitting.'))))
    submit_btn.pack()
    #place(x=100, y=160)
    submit_btn2 = Button(blck_wn, text='Block with time constraints', command=lambda: timed_block_websites(blck_wn, entry_sites.get('1.0',END)))
    submit_btn2.pack()
    #place(x=100, y=190)

def block_websites(win, websites):
    if not websites==[]:
        website_lists = websites
        Website = list(website_lists.split(","))
        try:        
            with open (host_path , 'r+') as host_file:
                file_content = host_file.read()
                for website in Website:
                    if website in file_content:
                        showinfo('Website Already blocked!', 'A website you entered is already blocked')
                        win.destroy()
                    else:
                        host_file.write(ip_address + " " + website + '\n')
                        showinfo('Websites blocked!', message='We have blocked the websites you wanted blocked!')
                        win.destroy()
        except PermissionError:
            Eraar = 'To resolve this error, you need to provide required privileges to hosts file, navigate to:\nC:\\Windows\\System32\\drivers\\etc\\\nNow right click on hosts file >> Properties >> Security >> Edit >> Provide Full control to the user you are using.'
            showinfo('Error!', message= Eraar)
            win.destroy()
    else:
        showinfo('Error!', message = 'The site list cannot be empty before submitting.')
def timed_block_websites(blck_wn, websites):
    if not websites == []:
        
        hours = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13',
                 '14','15','16','17','18','19','20','21','22','23']
        time1 = StringVar()
        time1.set(hours[8])
        Label(blck_wn, text = 'Enter Block Times Start', font = 'arial 10 bold', bg = 'Aquamarine').pack()
        #place(x=21, y=60)
        entry_time_start = OptionMenu(blck_wn, time1, *hours)
        entry_time_start.pack()
        #place(x=20, y=150)
        time2 = StringVar()
        time2.set(hours[17])
        Label(blck_wn, text = 'Enter Block Times Stop', font = 'arial 10 bold', bg = 'Aquamarine').pack()
        #place(x=21, y=60)
        entry_time_stop = OptionMenu(blck_wn, time2, *hours)
        entry_time_stop.pack()
        #place(x=100, y=150)
        submit_btn3 = Button(blck_wn, text='Submit', command=lambda: t_block_websites(int(time1.get()),int(time2.get()),websites,blck_wn))
        submit_btn3.pack()
    else:
        showinfo('Error!', message = 'The site list cannot be empty before submitting.')
def t_block_websites(x,y, website_lists,win):    
    Start = (dt.now().year, dt.now().month, dt.now().day,x)
    Stop = (dt.now().year, dt.now().month, dt.now().day,y)
    while True:
      
        # time of your work
        if Start < Stop:
            
            with open(host_path, 'r+') as file:
                content = file.read()
                for website in website_lists:
                    if website in content:
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        file.write(ip_address + " " + website + "\n")
            showinfo("Work Hours", message = ("Websites blocked from!{}am to {}pm.".format(Start,Stop)))
            win.destroy()
            break
            
        else:
            with open(host_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_lists):
                        file.write(line)
      
                # removing hostnmes from host file
                file.truncate()
      
            showinfo("Happy Hours", message = "Websites Unblocked!")
            win.destroy()
            break
            
        time.sleep(5)
        
def unblock(win):
    unblck_wn = Toplevel(win, background='Aquamarine')
    unblck_wn.title("Unblock a website")
    unblck_wn.geometry('320x280')
    unblck_wn.resizable(False, False)
    
    infile = open(host_path)
    outfile = open('blocked_websites.txt','w')

    for line in infile:
        if not line.startswith('#'):
            outfile.write(line)
    
    infile.close()
    outfile.close()
    
    Label(unblck_wn, text='Unblock websites', background='Aquamarine', font=("Georgia", 14, "bold")).place(x=60, y=0)
    Label(unblck_wn, text='Select the URLs that you want to unblock:', background='Aquamarine', font=('Georgia', 10)).place(x=20, y=40)
    Label(unblck_wn, text='NOTE: All websites will be unblocked anyway.', background='Aquamarine', font=('Georgia', 10)).place(x=20, y=70)
    Label(unblck_wn, text ="Deesc Gdams", font = 'arial 8 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
    # Creating a dropdown menu from the textfile to get the sites that are blocked
    blck_sites_strvar = StringVar(unblck_wn)
    with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
        try:
            blck_sites = blocked_websites_txt.readlines()
            blck_sites_strvar.set(blck_sites[0])
        except IndexError:
            showinfo('No Blocked Websites', message = 'There are currently no blocked sites.')
            unblck_wn.destroy()
    dropdown = OptionMenu(unblck_wn, blck_sites_strvar, *blck_sites)
    dropdown.config(width=30)
    dropdown.place(x=40, y=100)
    submit_btn = Button(unblck_wn, text='Submit', command=lambda: unblock_websites(unblck_wn, blck_sites_strvar.get()))
    submit_btn.place(x=130, y=160)
    
def unblock_websites(win,websites_to_unblock):
    
    with open(host_path, 'r+') as hostfile:
        content_in_file = hostfile.readlines()
        hostfile.seek(0)
        for line in content_in_file:
            if not any(site in line for site in websites_to_unblock):
                hostfile.write(line)
            hostfile.truncate()
    with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
        file_content = blocked_websites_txt.readlines()
        blocked_websites_txt.seek(0)
        for line in file_content:
            if not any(site in line for site in websites_to_unblock):
                blocked_websites_txt.write(line)
            blocked_websites_txt.truncate()
    showinfo('Website Unblocked!', message = 'Website Unblocked!')
    win.destroy()
root.update()
root.mainloop()