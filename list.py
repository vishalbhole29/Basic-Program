# list

x=[23,45,67,89]
print(x)

# list comprehension
# print even number upto 50 using list compresion

y=[num for num in range(1,51) if num%3==0]
print(y)

# Temperature conversion celcius to fahr
cel=[0,10,15,30]
far=[9/5*temp+32 for temp in cel]
print(far)

# print every word in this statement taht has even number of letters

string="print every word in this statement taht has even number of letters"
for word in string.split():
   if len(word)%2==0:
       print(word)

# sam print only the words that start with s in this statement
s="sam print only the words that start with s in this statement"
list=s.split()
for s in list:
    if s.startswith("s"):
        print(s)




