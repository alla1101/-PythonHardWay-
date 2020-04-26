types_of_people=10
x=f"there're {types_of_people} in this world"
binary="binary"
do_not="don't"
y=f"those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious=False
joke_evaluation="Isn't that joke so funny?! {} is the result\n and this was the catch fraze\n {}"

print(joke_evaluation.format(hilarious,y) )

w="this is the left side of ..."
e="a string with a right side"

print(w+e)