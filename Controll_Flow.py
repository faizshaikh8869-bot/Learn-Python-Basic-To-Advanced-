

# ---------------- Controll flow With For ----------------
 
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Stratagy 1:- Iterate Over a Copy 
# for user,status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# Stratagy 2:- Create a new Collection
active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
print(users)

# ---------------- With Range ----------------

sample = list(range(5, 105, 5))
print(sample)



a = ['Mary', 'had', 'a', 'little','lamb']

for i in range(len(a)):
    print(i, a[i])

#---------------- Brake and Continue ---------------- 

for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} equals {i} * {n//i}")
            break
print('\n')

for n in range(2, 10):
    if n % 2 == 0:
        print(f"FOUND EVEN NUM {n}")
        continue
    print(f"Oh!!! Shit, ODD NUM {n}")

#---------------- Exception Handling ----------------

for num in range(1,5):
    try:
        x = int(input("Enter a num:- "))
        break
    except ValueError:
        print("Fuck You 🤟")

from enum import Enum
#---------------- match and enum----------------
"""
Its look's like switch in Other Language 
    But 
it's more similar to pattern matching in languages like Rust or Haskell.
"""

class Color(Enum):
    RED = 'r'
    GREEN = 'g'
    BLUE = 'b'

color = Color(input("Enter Your Color 'r,g or b': "))

match color:
    case Color.RED:
        print("you like RED")
    case Color.BLUE:
        print("you like BLUE")
    case Color.GREEN:
        print("you like GREEN")
    case _:
        print("Not a Valid Color")
        # raise ValueError("Not a Color")

#---------------- Function ----------------
"""
 you might object that fib is not a function but a procedure since it doesn’t return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it’s a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using print()
"""

def fib(n):
    global c 
    a,b = 0,1   #Local Variable 

    c = 23      #Global Variable 
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print() # Return null 


fib(1000)
print(c)
fib(0)


"""
A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type.
"""
def fib2(n):

    a,b = 0,1
    results = []

    while a < n:
        results.append(a)
        a,b = b, a+b

    return results

lists = fib2(100)
print(lists)

#---------------- Default Arguments ----------------

# Prompt:str    -> Function Anotion --- It's Optional 
def ask_ok(prompt:str, retries = 4, reminder='Plese Try again!') -> bool:
    while True:
        reply = input(prompt)

        if reply in { 'y', 'yes', 'ye'}:
            print('Doing the Task')
            return True
        if reply in { 'n', 'no', 'nop', 'nope'}:
            print('Not doing the Task')
            return False

        retries = retries - 1
        # Base Case 
        if retries < 0:
            raise ValueError('invalid user response')
        
        print(reminder)

ask_ok('OK to overwrite the file? :- ', 2, '------- Come on, only yes or no! ------')


#---------------- *args and **Kwargs and Markers ----------------

# Markers:- /, * 
def standard_arg(arg):
    print(arg)
# standard_arg(2)
# 2
# standard_arg(arg=2)
# 2

def pos_only_arg(arg, /):
    print(arg)
# pos_only_arg(1)
# 1
# pos_only_arg(arg=1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>

def kwd_only_arg(*, arg):
    print(arg)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

# kwd_only_arg(arg=3)
# 3


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# ---------------------------------
#           *args & **kwargs
"""
*args (Positional Arguments): Collects any extra positional arguments into a tuple. The single asterisk * packs the values together, and args is just the standard variable name.

**kwargs (Keyword Arguments): Collects any extra named (key=value) arguments into a dictionary. The double asterisk ** packs the key-value pairs together, and kwargs is the standard variable name.
"""
def create_profile(username, *hobbies, **details):
    print(f"User: {username}")

    if hobbies:
        print(f"Hobbies: {', '.join(hobbies)}")

    for key,value in details.items():
        print(f"{key}: {value} ")

create_profile(
    "Faiz Shaikh",
    "Coding", "Cycling", "Chess",
    city="Pune", role="Developer", active=True
)


#------------------- Lambda Functions and Closure ------------------

# Lambda -> Comonly used in Sorting 

add_func = lambda x,y : x +y
print(add_func(2,5))

# Closure

def make_multiply(factor):

    def multiply(number):
        return number * factor
    return multiply

double = make_multiply(2)
triple = make_multiply(3)

print(double(10))
print(triple(5))

# Mixed
def make_inc(n):
    return lambda x: x + n

f = make_inc(12)
print(f(0))
print(f(1))