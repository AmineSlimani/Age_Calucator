# debut de  programme
#Debut de declaration des variables
birthday=input("please write your birthday : ")
birthday=int(birthday)

birthmonth=input("please write your birth month : ")
birthmonth=int(birthmonth)

birthyear=input("please write your birth year : ")
birthyear=int(birthyear)

from datetime import date

now = date.today()
# Fin de declaration des variables
# How Equation of day is gonna be in different situation as example : 31 ,30 , 29 or 28
if  birthday <= now.day:
     days=now.day-birthday

elif birthday > now.day and (birthmonth == 4 or birthmonth == 6 or birthmonth == 9 or birthmonth == 11 ):
     days =(30 + now.day)- birthday

elif birthday > now.day and birthmonth == 2 :
     days =(29+now.day) - birthday

elif birthday > now.day and birthmonth == 2 :
     days =(28+now.day) - birthday

elif birthday > now.day and birthday >=1 or birthday <= 31:
     days =(31+ now.day)- birthday

# How Equation of month is gonna be in different situation
if  birthmonth <=now.month:
    months = now.month-birthmonth
elif birthmonth > now.month:
    months = (12+now.month)-birthmonth

# How Equation of year is gonna be in different situation
if  birthmonth <= now.month:
    years = now.year - birthyear

elif birthmonth > now.month:
    years = now.year - birthyear - 1

# while user write wrong information

if birthday < 1 or birthday > 31 :
    print(" your birthday isn't correct.")

elif birthday == 31 and (birthmonth == 4 or birthmonth == 6 or birthmonth == 9 or birthmonth == 11 ):
    print(" you write 31 days at month number {}.Please ! check your information .".format(birthmonth))

elif birthyear%4 != 0 and birthmonth == 2 and birthday == 29 :
    print("you write 29 , february , in this year !february over in 28 ")

elif birthday >29 and birthday<=31 and birthmonth == 2 :
    print(" you write {} at february , that's fault !".format(birthday))

elif birthmonth < 1 or birthmonth > 12 :
    print(" you said  that  your birth month is {} ! your birth month  isn't correct !".format(birthmonth))

elif  birthyear  > birthyear :
    print(" you said  that  your birth month is {} ! your birth month  isn't correct !".format(birthmonth))

else :

    print("Your age is :")
    print(" {} years and {} months and {} days".format(years,months,days))
# Fin de programme
# by Amine Slimani
