read=open('set2.log','r')  #read the file
data = read.read()             #convert it into a readable  

print data
master_list=data.split()       #this list consists of all the elements separated and used to access each element separately



def conv_sec(x,dt):    #function to convert time into seconds including milliseconds and date consideration
    x=x[0:13]
    x=x.replace(":"," ")
    x=x.replace("."," ")
    x=x.split()
    
    
    y=( float(x[0])*3600 + float(x[1])*60 + float(x[2])+ float(int(x[3])/1000.0)+ dt*3600*24)
    return y

def conv_time(y):       #function to convert time from seconds format to h:m:s.ms format
    
    z=int((y-int(y))*1000)
    
    if(z/100==0):
        z=str(z)
        z="0"+z
    else:
        z=z+1
        z=str(z)
    m,s=divmod(y,60)
    h,m=divmod(m,60)
    t=str("%d:%02d:%02d" % (h, m, s))
    total=t+"."+z
    return total

def get_date(x):    #this function is used to get the date for the time mentioned
    for n in range(len(master_list)):
        if master_list[n]==x:
            return master_list[n-6]    

def conv_date_to_numbers(x):   #used to convert date of the format "14-Nov-2015" to [14,11,2015]
    y=x.replace("-"," ")
    y=y.split()
    if(y[1]=="Jan"):
        y[1]=1
    elif(y[1]=="Feb"):
        y[1]=2
    elif(y[1]=="Mar"):
        y[1]=3
    elif(y[1]=="Apr"):
        y[1]=4
    elif(y[1]=="May"):
        y[1]=5
    elif(y[1]=="Jun"):
        y[1]=6
    elif(y[1]=="Jul"):
        y[1]=7
    elif(y[1]=="Aug"):
        y[1]=8
    elif(y[1]=="Sep"):
        y[1]=9
    elif(y[1]=="Oct"):
        y[1]=10
    elif(y[1]=="Nov"):
        y[1]=11
    elif(y[1]=="Dec"):
        y[1]=12
    y[0]=int(y[0])
    y[2]=int(y[2])
    return y

def conv_date_to_counter(x):  #this calculates the difference between the initial date and rest in the input and forms a counter which can be used to see if date has changed
    counter=[]
    temp=x[0]
    counter.append(0)
    for n in range(1,len(x)):
        if(n+1<len(x)):
            
            counter.append(x[n]-x[0])
    return counter
        
def unique_elements(x): #this function is used to remove duplicate items from the list in a ordered way
    checked = []
    for e in x:
        if e not in checked:
            checked.append(e)
    return checked

def average(x):
    sum=0.0
    for n in x:
        sum=sum+n
    average=sum/len(x)
    return average

   
date_counter=[] #this is to get the date of all requests from the master_list
for n in range(len(master_list)):
    if(n%11==0):
        date_counter.append(master_list[n])
date_in_num=[] #initialized to store the date in number format
for n in range(len(date_counter)):
    date_in_num.append(conv_date_to_numbers(date_counter[n]))

only_date=[]    #separate only date from the given date_in_num
for n in range(len(date_in_num)):
    only_date.append(date_in_num[n][0])

diff_in_date=conv_date_to_counter(only_date)  #this generates the difference in date


dictionary={}       #create an empty dictionary
k=0
temp=0
for n in range(0,len(master_list)):     #creating a dictionary with time as keys and domains as values 
    if(k+11 < len(master_list)):
        dictionary[conv_sec(master_list[1+k],diff_in_date[temp])]=master_list[6+k]
        temp=temp+1
    k=k+11

time=sorted(dictionary.keys())  #to take time from the dictionary created



break_time=[]       #this list is created to collect the position where the time differenceis high
for sec in range(0,len(time)):
    if(sec+1<len(time)):
        if((time[sec+1]-time[sec])>20):     #a threshold of 20 is used 
            break_time.append(sec+1)



g=0     
time_length=len(break_time) #number of elements in the list containing the position

list_of_time=[] #contains the time list separated accordingly

for p in range(0,time_length+1):    
    if(p<time_length):
        h=break_time[p]
    else:
        h=len(time)-1
    list_of_time.append(time[g:h:])
    g=h

#print list_of_time            

domain=[]
for n in time:
    domain.append(dictionary[n])

list_of_domain=[]
g=0
for p in range(0,time_length+1):    #this creates the domain list which fall in one category as a single list
    if(p<time_length):
        h=break_time[p]
    else:
        h=len(time)-1
    list_of_domain.append(domain[g:h:])
    g=h

list_of_unique_domain=[]    #removing the duplicates in the list
for n in range(len(list_of_domain)):
    list_of_unique_domain.append(unique_elements(list_of_domain[n]))

#print list_of_unique_domain
report=open('report.txt','w')   
z=len(list_of_unique_domain)
for d in range(z):  #to generate the dns log in a huma readable format
    dom_name=list_of_unique_domain[d][0]+":"+str(len(list_of_unique_domain[d]))  #for the format which gives amazom.com:(number)
    timing=conv_time(list_of_time[d][0])    #get the time at which the domain was accessed
    final_date=get_date(list_of_unique_domain[d][0])             #get the respective date
    report.write(dom_name+" "+str(final_date)+" "+timing)
    report.write("\n")
    for n in range(len(list_of_unique_domain[d])):
        report.write(str(n+1)+" "+list_of_unique_domain[d][n])
        report.write("\n")
    report.write("\n")

report.close()




