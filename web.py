import webbrowser
import sys
import time;
import datetime;
import os;

vid = "idyZRfRScbk" #Video ID for youtube video
dhour = input("Enter hour:")
dmin = input("Enter minute:")
pword = raw_input("Enter your password:")
if(not(dhour < 24 and dhour >= 0 and dmin < 60 and dmin >= 0)):
    print("INVALID TIME")
    sys.exit()

ltime = time.localtime(time.time())
strt = time.strftime('%Y-%m-%dT%H:%M:%S', ltime)
slist = list(strt)
slist[11] = str(dhour/10)
slist[12] = str(dhour%10)
slist[14] = str(dmin/10)
slist[15] = str(dmin%10)
strt = "".join(slist)
alrmtimeStruct = time.strptime(strt, '%Y-%m-%dT%H:%M:%S')

# alrmtimeStruct.tm_hour = dhour
# alrmtimeStruct.tm_min = dmin

# alrmtimeStruct.tm_mday = ltime.tm_mday
# alrmtimeStruct.tm_year = ltime.tm_year
# alrmtimeStruct.tm_mon = ltime.tm_mon
# alrmtimeStruct.tm_sec = ltime.tm_sec
# alrmtimeStruct.tm_wday = ltime.tm_wday
# alrmtimeStruct.tm_yday = ltime.tm_yday
# alrmtimeStruct.tm_isdst = ltime.tm_isdst


alrmtime = time.mktime(alrmtimeStruct)

    
if(dhour < ltime.tm_hour):
    alrmtime += 86400

if(alrmtime < time.time()):
    print("INVALID TIME")
    sys.exit()


timeStruct = time.localtime(alrmtime)
m = str(timeStruct.tm_mon)
d = str(timeStruct.tm_mday)
y = str(timeStruct.tm_year)
hh = str(timeStruct.tm_hour)
mm = str(timeStruct.tm_min)
ss = str(timeStruct.tm_sec)



print("Alarm set for \""+m+"/"+d+"/"+y+" " + hh+":"+mm+":"+ss+"\"")

os.system("echo "+pword+" | sudo -S pmset schedule wake \""+m+"/"+d+"/"+y+" " + hh+":"+mm+":"+ss+"\"");
os.system("open /System/Library/PreferencePanes/Security.prefPane/")
print("\n")
time.sleep(45)
os.system("pmset displaysleepnow");
n = alrmtime - time.time()
print n
if(n > 32):
    
    print("Sleeping for", n)
    time.sleep(n - 31)
    print("Woken up")

while(1):
    if(time.time() == alrmtime): #https://www.youtube.com/watch?v=ijLZ9-rlEhg
        print("Wake up!")
        os.system("osascript -e \"set Volume 10\"");
        os.system("open /System/Library/PreferencePanes/Security.prefPane/")
        webbrowser.open("https://www.youtube.com/tv#/watch?v="+vid);
        sys.exit()

    

    