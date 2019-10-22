from datetime import datetime

def vtime(t1,t2):
    formattime = '%I:%M%p'
    t3=datetime.strptime(t2,formattime)-datetime.strptime(t1,formattime)
    return(t3)

def isemp(regnum):
    f2=open("empdata.txt" , "r")
    for line in f2:
        y=line.split(" ")
        if(y[1]==regnum):
            f2.close()
            return(1)
    f2.close()
    return(0)

def filewriter(vtype,regno,duration,payment="0.00"):
    f3 = open("bill.txt", "at")
    f3.write(f"{i.vtype} {i.regno} Duration({duration}) Rs.{payment}\n")
    f3.close()

class vehicle:
    def  __init__(self,vtype,regno,timein=0,timeout=0): 
        self.vtype = vtype
        self.regno = regno
        self.timein = timein
        self.timeout = timeout

    def pay(self):
        duration=vtime(self.timein,self.timeout)
        dur=duration.seconds/3600

        if(self.vtype=="Bike"):
            payment=(int(dur-1)*10)+int(dur-int(dur)+0.999)*10+20

        elif(self.vtype=="Car5seater"):
            payment=(int(dur-1)*20)+int(dur-int(dur)+0.999)*20+30 

        elif(self.vtype=="Car7seater"):
            payment=(int(dur-.5)*25)+int(dur-int(dur)+0.999)*25+35

        elif(self.vtype=="Truck"):
            if((dur-2)>0):
                payment=(int(dur-2)*40)+int(dur-int(dur)+0.999)*40+100
            else:
                payment=100

        filewriter(i.vtype,i.regno,duration,payment)
  

f1=open("vehicledata.txt" , "r")
vehiclelist=[]
for i in f1:
    y=i.split(" ")
    y[-1] = y[-1].strip()
    vehiclelist.append(vehicle(y[0],y[1],y[2],y[3])) 
f1.close()
 
for i in vehiclelist:
    if(isemp(i.regno)==0):
        i.pay()       
    else:
        duration=vtime(i.timein,i.timeout)
        filewriter(i.vtype,i.regno,duration)