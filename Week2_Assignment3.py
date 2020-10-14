
# let the user know what's going on
print ("Oh hello there!")
print ("Let's go")
print ("-----------------------------------")

# variables containing all of your story info
adjective1 = raw_input("Enter a negative adjective: ")
adjective2 = raw_input("Enter another negative adjective: ")
activity = raw_input("Name an activity: ")
location1 = raw_input("A place you don't like: ")
noun1 = raw_input("Name a thing you don't like: ")
noun2 = raw_input("Another thing you don't like: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "A mile and a half on a " + adjective1 + " bus takes a long time. " \
+ " The odor of " + adjective2 + " prison food takes a long time to pass you by. "\
+ "Day upon day of this " + activity + " gets you down." \
+ " Nobody gives you a chance or a dollar in this old " + location1 + "." \
" Hovering silence from you is a giveaway. " \
+ noun1 + " and " + noun2 + "  bads not your style. "

# finally we print the story
print (story)