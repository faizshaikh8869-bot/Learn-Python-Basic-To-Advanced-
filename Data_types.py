
import decimal 
from fractions import Fraction

### Numbers 

# ---------- Int ----------  
# number_int = int(22);
# number_ex_int = int(input("Enter int number"))


# # ---------- Float ---------- 
# number_flt = 3.142516
# number_ex_flt = float(input("Enter float number ")) 

# number_cast_flt = float("20")
# number_cast_flt0 = float(13)

# ---------- Decimal ---------- 
print(decimal.Decimal(1.1) + decimal.Decimal(1.2) + decimal.Decimal(1.3))

data = list(map(decimal.Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
print(max(data))

# ---------- Fractional ---------- 
print(Fraction(16, -10))

print(Fraction('3.1415926535897932'))
print(Fraction('3.1415926535897932').limit_denominator(1000))
print(Fraction(355, 113))


# ---------- Complex ----------
z = complex(3, 4)
## z = 3 + 4j
# cmath.sin(2 + 3j) 
print(z.real)
print(z.imag)
print(z * 2)
print(abs(z))


# ---------- List ----------        SQUARE BRACKET      Mutable 
lst_ex_str = ['Pathan', 'Pasha', 'Chand 😑', 'Dost Baap Sirname']
print(lst_ex_str[0])
print(lst_ex_str)

lst_ex_str[3] = 'Dost Ka BAap Ka naam'
print(lst_ex_str)

## ---------- tuple ----------     PARENTHESIS      IMUTABLE(unchangable like RCB - status not chaged onced declared )
tpl_ex_str = ('PAthan', 'Chand 😑', 'Pasha', 'Dost Ka name' )
# tpl_ex_str[2] = 'Xhutiya'     -- Will Fail



## ---------- Dict ------------
students = ['ramash', 'suresh', 'jignesh', 'sarvesh']
dct_ex_clss = {
    "teacher": "hutiya Sir",
    "students": students,
    "total Students": len(students),
    "Class": "3rd Class"
}

dct_ex_clss['Class'] = '1 st Class'
print(dct_ex_clss)

print(dct_ex_clss.get("teacher"))


## ----------- Set ------------     Unique         Mutable     
set_ex_fruts = {'apple', 'banana', 'fruit'}
print(set_ex_fruts)
print(type(set_ex_fruts))


## ---------- frozenset ----------- also Unique     Immutable (RCB)
frzen_st_ex = frozenset({'apple','banana', 'fruit'})


## ---------- String ------------   YA Ai Bharosa Rahega    String is only methods do ai  
A_Word = "Supermadarchoodcalifragilisticexpialodocious"

print(A_Word)
print(A_Word[5:15])

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

#--------------Range -----------
for _ in range(1, 10):
    print('\tTata By By\n \t  Khatam Gaya!!!')
