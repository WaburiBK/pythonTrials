phone_balance = 4
bank_balance = 100

print phone_balance, bank_balance

if phone_balance < 5: #if statements controls when the code is executed
    phone_balance += 10
    bank_balance -= 10

print phone_balance, bank_balance

fuel = 900
bank_balance = 12000

print fuel, bank_balance

if fuel < 1000:
    fuel += 2500
    bank_balance -=2500

print fuel, bank_balance

n = 16

if n % 2 == 0:
    print "Number " + str(n) + " is even"

else:
    print "Number " + str(n) + " is odd" #else condition executed when the boolean expression returns false

season = "winter"

if season == "summer":
    print "plant the garden"

elif season == "spring":  #elif used when there are multiple conditions to be checked
    print "water the garden"
elif season == "autumn":
    print "harvest the garden"
elif season == "winter":
    print "stay indoors"

wake_up = 6

if wake_up > 5:
    print "Stay asleep"

else:
    print "Time to wake up"

steel_nails = 11

if steel_nails > 10:
    print "purchase mdf nails"

else:
    print "purchase steel nails"

#my customers are either business, corporate or personal
customer = "Corporate"

if customer == "Business":
    print "Increase rate by 10%"

elif customer == "Corporate":
    print "Increase rate by 15%"

elif customer == "Personal":
    print "Decrease rate by 15%"

