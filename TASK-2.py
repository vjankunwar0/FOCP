from statistics import mean
km,miles=[],[]

print("Swallow Speed Analysis: Version 1.0")
while True:
    get=input("Enter the Next Reading:")
    if get=="":#check if the input is emputy 
        break
  
    if get[0].lower()=="u" and get[1:].isalpha()==False: #validating the speed 
        speed = float(get.lower().replace("u",""))   
        miles.append(speed)
        km.append(speed*0.621371)
        print("Reading saved.")

    elif get[0].lower()=="e" and get[1:].isalpha()==False: #validating the speed 
        speed =float( get.lower().replace("e",""))
        km.append(speed)
        miles.append(speed*1.60934)
        print("Reading saved.")

    else:
       print( "invalidinput")
if len(km)!=0: #check if there is not empty   
    if len(km)==1:
        print("{} Reading Analysed.".format(len(km)))

    else:
        print("{} Readings Analysed.".format(len(km))) 
    print("max speed:{:.2f} KPH,{:.2f} MPH".format(max(km),max(miles)))
    print("min speed:{:.2f} KPH,{:.2f} MPH".format(min(km),min(miles)))
    print("average speed:{:.2f} KPH,{:.2f} MPH".format(mean(km),mean(miles)))
else:
    print("no values entered")