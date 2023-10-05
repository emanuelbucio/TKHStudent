# Exercise 1.2. Write Python code to evaluate these expressions.
# The answers can be stored in a name, or evaluated in a print statement

# 1. How many seconds are there in 42 minutes 42 seconds?
print(42*60+42)


# 2. How many miles are there in 10 kilometers? Hint: there are 1.61
# kilometers in a mile.
kilometers = 10
miles = kilometers/1.61

print(miles)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?


miles = 6.21
seconds = 42*60+42
miles = 10/1.61
pace = seconds/miles
minutes = 60
print(pace/minutes)

pace_in_minutes = pace/minutes
print ("Our aveage pace is "+str(pace_in_minutes) + " or " + str(floor(pace_in_minutes)) + "." + str((pace_in_minutes - floor(pace_in_minutes))*60))



x = 3
x = x + 2
print(x==5)