import re
def text_match(s):
        matching = '^[a-z]+_[a-z]+$'
        if re.search(matching,  s):
                return 'Yes'
        else:
                return 'No'

s = input()
print(text_match(s))