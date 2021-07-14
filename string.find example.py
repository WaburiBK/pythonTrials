definition = "Goodness! I have not coded in over a week! Let me change that."
first = definition.find("!")
second = definition.find("!", first+1)
new_definition = definition[:first] + definition[first+1:second] + definition[second+1:]
print new_definition
new_definition = definition[:first] + "." + definition[first+1:second] + "." + definition[second+1:]
print new_definition