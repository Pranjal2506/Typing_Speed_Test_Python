from time import *
import random as r

def mistake(para,user):
    error=0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error += 1
        except:
            error += 1
    print("Accuracy: ",((len(para)-error)/len(para))*100)
    return error

def speed_time(init,end,word):
    net_time=round((end-init),2)
    speed=len(word.split(" "))/(net_time/60)
    return round(speed,2)
    
text=["Hello! I am a person and I am here to test my typing speed. I can type punctuations like <*>$ etc.",
      "Here I can test speed of my typing",
      "If anyone wants to test open this program and run",
      "Thank you, goodnight takecare sweet dreams tata bye bye"]
test1=r.choice(text)
print("       *****Typing Speed Calculator*****")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter : ")
time_2=time()

print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
print("Error",mistake(test1,testinput))