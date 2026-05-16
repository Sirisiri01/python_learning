import re
# text="Hello,my name is Siri and my email is sirirksiri141@example.com"
# pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# match=re.search(pattern,text)
# if match:
#     print("Email found:",match.group())
# else:
#     print("Email not found")

text1="there are 26 students in class 10A and 25 in 10B"
pattern="[0-9]+"
matches=re.findall(pattern,text1)
print("Numbers found:",matches)
date_string="2026-05-16"
date_pattern=r"\d{4}-\d{2}-\d{2}"
if re.match(date_pattern,date_string):
    print("Valid Date")
else:
    print("Invalid Date")