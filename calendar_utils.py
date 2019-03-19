# Mphephu Faresa
# CSC1010H

def is_leap_year(year) :
    #code for leap year 
    a =year%4
    b =year%100
    c = year%400
    if  a==0 :
        if b == 0 :
            if c==0 : return True
            else : return False             
        if b!=0 : return True 
        
    else: return False 
    
def month_name(number) :
    month = {1:"January",2:"February",3 :'March' , 4:"April" , 5:"May" , 6:"June" , 7:"July",8:"August",9:"September",10:"October",11:'November',12:"December"}
    return month[number]
    #Given the number of a month, returns the corresponding name. 1 is January, ..., 12 is December.
    
def days_in_month(month_number,year) :
    month = month_name(month_number)
    #print(month)
    if month in {"January" , "March" , "May" ,'July' ,'August' , 'October' , "December" }:
        return 31 
    elif month in {"April", "June" ,"September" ,"November" }:  return 30
    elif is_leap_year(year) == True and month_number == 2 : return 29
    elif month_number == 2 :  return 28
        
    #Given month (in the form of a number) and (4 digit) year, return the number of days in the month (accounting, in the case of February, for whether or not it is a leap year).
def first_day_of_year(year) :
    z =(year-1)%4 
    x= (year-1)%100
    v = (year-1)%400
    calc =  5*z + 1 + 4*x + 6*v 
    return calc%7
    
def first_day_of_month(month_number, year) :
    count = 0
    days = {"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
    z =(year-1)%4 
    x= (year-1)%100
    v = (year-1)%400
    calc =  5*z + 1 + 4*x + 6*v 
    day = calc%7    
#print(day)
    sto = 1
    for month in range(month_number) :
        #print(month)
        if month == 0 :
            if is_leap_year(year) == True :
                sto+=5
                sto+= days_in_month(month+1,year)
                #print(sto)
        if month == 1 :
            if is_leap_year(year) == False : 
                sto+=-1
                day-=3
                sto+= days_in_month(month+1,year)
                #print("Month",month)
            if is_leap_year(year) == True :     
                sto+=2
                day+=2
                sto+= days_in_month(month+1,year)
                #print("Month Leap",month)      
        else :
            sto+= days_in_month(month+1,year)
        #print("Sto",sto)
        
    for i in range(sto):
        day +=1   
        if day >=7 : day = 0
   # print("day",day)    
    return day 
    
    # Given a month (in the form of a number) and (4 digit) year, return the number of the day on which the first of that month falls. 0 is Sunday, …, 6 is Saturday.    

#def main():
 #   days_in_month(2,2016)
    
#main()