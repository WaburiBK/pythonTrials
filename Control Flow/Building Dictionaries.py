book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin' ]

word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
    
print (word_counter)

car_dealership = ['volkswagen', 'toyota', 'mercedes', 'subaru', 'mercedes', 'honda', 'subaru', 'toyota', 'mazda', 'mitsubishi']

car_counter = {}

for car in car_dealership:
    if car not in car_counter:
        car_counter[car] = 1
    else:
        car_counter[car] += 1
    
print (car_counter)

popular_destinations = ['watamu', 'kilifi', 'diani', 'malindi', 'watamu', 'mombasa', 'kilifi', 'nanyuki', 'watamu', 'diani', 'watamu', 'wasini']

destination_counter = {}

for destination in popular_destinations:
    if destination not in destination_counter:
        destination_counter[destination] = 1
    else:
        destination_counter[destination] =+ 1

print (destination_counter)






















