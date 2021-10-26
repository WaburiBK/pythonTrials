#Lists
kenyan_towns = ['Nairobi', 'Thika', 'Eldoret', 'Nyeri', 'Kisumu', 'Watamu'] #lists enclosed in square brackets

#Lists can hold/contain a mix of data types
random_list = [156, 4.5, 'I am a string', True] #contains int, float, string and bool values

#List Indexing
print (kenyan_towns[2]) #application of zero based indexing

#List Slicing
print (kenyan_towns[1:4]) #lower bound inclusive, upper bound exclusive

#Mutability and Order
#Lists are mutable and can be changed at any moment
kenyan_towns[2] = 'Lamu'
print (kenyan_towns)

random_list[0] = random_list[0] // 15
print (random_list)

#using 'in' or 'not in'
nse_top = ['SCOM', 'BAT', 'KAKZ', 'ABSA', 'EQTY', 'KCB']

print (nse_top[2])
print (nse_top[0:4])

#LIST METHODS
first_list = [15, 100, 256, 8520, 3, 95]
print (max(first_list)) #returns largest value
print (len(first_list)) #returns no. of objects in list
print (sorted(first_list)) #returns copy of list in ascending order
print (sorted(first_list, reverse=True)) #returns copy in descending order
print (min(first_list)) #returns opposite of max()

second_list = ['Kaka Travellers', 'Bahima Shuttle', 'Tripple 8 Services', 'Sony Classic']  #list of strings
print (max(second_list)) #returns largest in terms of alphabetic placement
print (len(second_list))
print (sorted(second_list))
print (sorted(second_list, reverse=True))
print (min(second_list)) #returns smallest in terms of alphabetic placement


