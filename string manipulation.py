# s = udacity
# t = bodacious
# Write python code that prints out "udacious" without using any quote characters

s = "udacity"
print s[:3]

t = "bodacious"
print t[4:]

print s[:3] + t[4:]

print s[:5] + t[6:]

print s[:5] + t[-3:]

# STRING SLICING

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

print sentence[:2]
print sentence[6:30]
print sentence[34:]

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "dog" # your noun here
verb_replacement = "move" # your verb here

new_sentence = "A dog went on a walk. It can move really fast"
# your code here
substring1 = new_sentence[:5]
substring2 = new_sentence[6:30]
substring3 = new_sentence[30:]

print new_sentence[:5] + new_sentence[6:30] + new_sentence[30:]