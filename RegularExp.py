# RegEx can be used to check if a string contains the specified search pattern.
import re

text = "Hello bangladesh"
mes = re.findall("He.*l",text) #here * state the limitation of characters
print(mes)

txt1 = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt1)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# A special sequence is a \ followed by one of the characters in the list below,
print("\n")
text2 = "This is the first time Im doing 4099 codes in 1 day."
text3 = "Can you solve this equation:2+5*10?"
find_char = re.findall("\AThis",text2)
print("Finding first characters in the line:",find_char)
find_dig = re.findall("\d",text3)
print("Finding digits in the string line:",find_dig)
find_last = re.findall("day.\Z",text2)
print("Finding the last char of the line:",find_last)
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
print("\n")
import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

text5 = "The numbers 0, 1, 2, and 3 are present in this text."

matches = re.findall(r'[0123]', text)

print(matches)

txt6 = "The rain in Spain"
x = re.search("Portugal", txt6)
print(x)
