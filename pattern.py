import re
s1="Sunday, Monday,Tuesday,Wednesday, Sunday, Saturday"
pat=r"S[a-z]+"
replacement="Friday"
result=re.sub(pat,replacement,s1, count=1)
print(result)

message="We are learning re.Using re we can replace a pattern in a string"
pat=r'\bre\b'
replacement="Regular Expression"
result=re.sub(pat, replacement, message)
print(result)