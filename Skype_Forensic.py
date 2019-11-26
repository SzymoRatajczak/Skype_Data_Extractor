import sqlite3,os,optparse

def printProfile(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("Select fullname,city,country,datetime(profile_timestamp,'unixepoch')from Accounts;")

    for row in c:
        print('[*]----Found Account----')
        print('[+]User:'+str(row[0]))
        print('[+]Username:'+str(row[1]))
        print('[+]Location:'+str(row[2])+str(row[3]))
        print('[+]Profile Date:'+str(row[4]))



def printContacts(skyeDB):
    conn=sqlite3.connect(skyeDB)
    c=conn.cursor()
    c.execute("Select displayname,skypename,city,country,phone_mobile,birthday from Contacts;")
    for row in c:
        print('\n[*]----Found contact----')
        print('[+]User:'+str(row[0]))
        print('[+]Skype username:'+str(row[1]))
        if str(row[2])!='' and str(row[2])!='None':
            print('[*]Location'+ str(row[2]+','+str(row[3])))
        if str(row[4])!='None':
            print('[*]Mobile number'+ str(row[4]))
        if str(row[5])!='None':
            print('[*]Birthday'+str(row[5]))



def printCallLog(skyeDB):
    conn=sqlite3.connect(skyeDB)
    c=conn.cursor()
    c.execute("select datetime(begin_timestamp,'unixepoch',identity from calls,conversations where calls.conv_dbid=conversations.id)")
    print('\n[*]-----Found Calls------')
    for row in c:
         print('[+]Tie:'+str(row[0])+ '| Partner'+str(row[1]))



def printMessage(skypeDB):
    conn=sqlite3.connect(skypeDB)
    c=conn.cursor()
    c.execute("Select datetime(timestamp,'unixepoch'),dialog_partner,author,body_xml from messages;")
    print('\n[*]------Found MEssages------')
    for row in c:
        try:
            if 'partlist' not in str(row[3]):
                if str(row[1])!=str(row[2]):
                    msgDirection='To'+str(row[1])+':'
                else:
                    msgDirection='From'+str(row[2])+' '
                print('Time'+str(row[0])+ ' '+ msgDirection+str(row[3]))

        except:
            pass



 
    







