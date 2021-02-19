current_year=int(input("Enter the Current Year: "))
final_year=int(input("Enter the final year until which you wanna find the leap years: "))
no_of_years=int((final_year-current_year)/4)
leap_years=[]
count=0
i=0
while(count<no_of_years):
    if(current_year%400==0 or current_year%4==0 and current_year%100!=0):
        leap_years.append(current_year)
        count=count+1
    current_year=current_year+1
print("The Leap Years until ",final_year,"are")
print(leap_years)
