age=input("what is your age")                             #  {}

total_days=365*90
total_weeks=52*90
total_months=12*90

yearsleft=90-int(age)
daysleft=total_days-(365*int(age))
weeksleft=total_weeks-(52*int(age))
monthsleft=total_months-(12*int(age))

print(f"you have {daysleft} days,{weeksleft} weeks,{monthsleft} months left")