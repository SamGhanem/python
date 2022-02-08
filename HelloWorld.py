# # 1. TASK: print "Hello World"
print( "Hello world" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Sam Ghanem"
print( "Sam", "Ghanem" )	# with a comma
print( "Sam" + " " + "Ghanem" )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
my_name = "Sam Ghanem"
print(f"Hello", my_name +"!" )	# with a comma
number = "78"
print(f"Hello", number + "!")	# with a +	-- this one should give us an error!
number = "78"
print(f"Hello" , number + "!")
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"i love to eat", fave_food1, "and",fave_food2  ) # with an f string
print(fave_food1.upper())

