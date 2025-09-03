




def leapyearfinder():

        year=int(input("which YEAR you want me to check:"))

        if  year % 400==0  or (year % 4==0 and year % 100 !=0):
           print(year,": IS A LEAP YEAR ")

        else:
             print(year,": is NOT leap year")
        return 0


leapyearfinder()
    