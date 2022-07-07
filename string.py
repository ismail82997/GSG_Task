a = "Hello World!"
#print(a[-7:-1])
# len() to know how many charc. in the string.
print(len(a))

# To check if the word you are looking for in the string or not the result will be true or false 
text = " Work hard rest less"
# print("hard" in text)
# you can usr not in to lokk for if the word in string or not 
print("hello" not in text) 

txt = "you are great but you must relase it"
# .upper() to make all string capital 
# .lower() to make all string small
print(txt.upper())

op = "YOU ARE THE BEST MAN NOW"
print(op.lower())

u = "hello"
print(a*3) 

def my_function():
    print("Hello from the other side!!")
    print("World War 3")
my_function()

def Adding():
    a = 20 
    b = 30 
    Sum = a + b 
    print("After calling", Sum)

Adding()

def multiplication(w, z): 
    mu = w * z 
    print(mu)
multiplication(80, 20)

def my_function( country = "Palestine"):
    print("I'm from"+" "+ country)

my_function()
my_function("Egypt")

def my_sons(child3, child2, child1):
    print("The youngest child is" +" "+ child3)

my_sons(child1= "Ismail", child2= "Noor", child3="Hamza")

def plus(*args):
    return sum(args)

print(plus(1,3,6,8,9,80)) 



