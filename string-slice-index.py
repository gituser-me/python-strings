# Let us create a variable named 
# message which holds the value
# "Hello, Ravi"

message = "Hello, Ravi"

# Now suppose we need to
# find the first character
# of the string for this we 
# do the following:

first_char = message[0]

# this is called indexing strings
# for finding specific characters
# in it
# so now let us print the value of first_char

print(first_char)

# but now we wish to find specific groups of letters in the string
# let us see how to do so
# the process we use for this is called slicing strings

# in this case we are going to find the group of letters "Hello" in the string
# firstly we notice the position of "H" in the string, that is 0
# next, we find the position of "o" in the string, that is 4
# so the code would be:

group_letters = message[0:4]

# so, that's it
# let us now print the value of group_letters

print(group_letters)

# so thats it for this tutorial
# hope you learnt how to index and slice strings
