number=[""," One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
power = [" Lakh", " Thousand"," Hundred", " Crore"]
stack = [0,0,0,0,0,0,0,0]
adm =[ ]
a = ""
b = ""
c = "" 
d =""  
e =""  
f =""  
g =""  
h = ""
i = 0
j = ""
z = ""
print("NOTE :-Please don't forget to put decimal")
num = str(input("Enter your number :- "))
split = num.split(".")
digit = int(split[0])
decimal = int(split[1])
decimal1 = split[1]

while decimal != 0:
    adm.append(decimal%10)
    decimal = decimal // 10

while digit !=0:
    stack[i]=digit%10
    i = i + 1
    digit = digit //10


    # For Crore's place
for num1 in range(len(number)):
       if stack[7] > 0:
           if stack[len(stack)-1] == num1:           
             a = number[num1] 
             a= a + power[3] +" "
             
    # For Lakh's place
for num1 in range(len(nty)):     #first for loop
       if stack[6] >1 :
           if stack[len(stack)-2] == num1:
                 b = nty[num1]
                 if stack[5] == 0:
                    b = b + power[0] +" "
                    
for num1 in range(len(number)):   # second for loop 
        
        if stack[6]==0:
            if stack[len(stack)-3] ==num1:
                c = number[num1]     
                if stack[6] == 0:
                    if stack[5] !=0:
                        c = c + power[0] +" "
                
        elif stack[6] !=1:    
            if stack[5] != 0:
                if stack[len(stack)-3]==num1:
                   c = number[num1]
                   if stack[6] > 1:
                    c = c + power[0] +" "
    
for num1 in range(len(tens)):   #Third for loop
        if stack[6]==1:
            if stack [len(stack)-3] == num1:
                b = tens[num1]+ power[0] + " "
             
                
    # For Thousand's place 
for num1 in range(len(nty)):    
       if stack[4] >1 :
           if stack[len(stack)-4] == num1:
                 d = nty[num1]
                 if stack[3] == 0:
                    d = d + power[1] +" "
                    
for num1 in range(len(number)):
        
        if stack[4]==0:
            if stack[len(stack)-5] ==num1:
                e = number[num1]      
                if stack[4] == 0:
                    if stack[3] !=0:
                        e = e + power[1] +" "
                
        elif stack[4] !=1:  #edit 1
            if stack[3] != 0:
                if stack[len(stack)-5]==num1:
                   e = number[num1]
                   if stack[4] > 1:
                    e = e + power[1] +" "
    
for num1 in range(len(tens)):
        if stack[4]==1:
            if stack [len(stack)-5] == num1:
                d = tens[num1]+ power[1] +" "
         
    
    # For hundred's place
for num1 in range(len(number)):  
        if stack[2] > 0:
            if stack[len(stack)-6] == num1:
                f =number[num1] + power[2] +" and "
for num1 in range(len(number)):    
    if stack[2]== 0:
        if stack[1] !=0:
            z = " and "
        if stack[0] !=0:
            z= " and "  
        
            
    # For Ten's place
for num1 in range(len(nty)):    
       if stack[1] >1 :
           if stack[len(stack)-7] == num1:
                 g = nty[num1]
                 
                    
for num1 in range(len(number)):
        
        if stack[0]== 0:
            if stack[len(stack)-8] ==num1:
                h = number[num1]      
                    
        elif stack[1] !=1:  
            if stack[0] != 0:
                if stack[len(stack)-8]==num1:
                   h = number[num1]
                  
    
for num1 in range(len(tens)):
        if stack[1]==1:
            if stack [len(stack)-8] == num1:
                g = tens[num1]
                
            if stack[1] >1:
                for num1 in range(len(number)):
                    if stack[0] > 0:  
                        if stack[len(stack)-8]==num1:
                            h = number[num1]

    

if  len(adm) == 1:
    j = "  "+ decimal1 + "/10"
elif len(adm) ==2:
    j = "  "+ decimal1 + "/100"
elif len(adm) ==3:
    j = "  "+ decimal1 + "/1000"
elif len (adm) ==4:
    j = "  "+ decimal1 + "/10000"
    
print(" Rs "+a+b+c+d+e+f+z+g+h+j+" Only ")
