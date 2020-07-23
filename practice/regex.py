import re

pattern = "term1"

string = "string of term1"

if re.search(pattern, string):
    print("Match")
else:
    print('No Match')
