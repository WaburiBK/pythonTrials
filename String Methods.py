name = "June"
location = "Nyeri"

print ("My girlfriend {} lives and works in {}".format(name, location))

statement = "Today was a brilliant day. We managed to finish all the work and enjoy a few drinks"

word_count = len(statement)
first_idx = statement.index("the")
second_idx = statement.rindex("the")


new_message = "The total word count for the above statement is {}. Additionally, the first and last occurrence of 'the' is at index {} and {} respectively."

print (new_message.format(word_count, first_idx, second_idx))

fuel = "25"
added_fuel = "10"
new_fuel = int(fuel) + int (added_fuel)

customer_messsage = "Your fuel tank capacity after top up stands at {} litres"

print (customer_messsage.format(new_fuel))

print (type(fuel))
print (type(new_fuel))
print (type(customer_messsage))

value = input("Please enter the re-fill amount (Kshs): ")
price = 106.5

fuel_added = int(value) // price

print ("You have received {} litres.".format(fuel_added))
