import re
def text_match(s):
        matching = 'ab{2,3}'
        if re.search(matching,  s):
                return 'Yes'
        else:
                return'No'
s = input()
print(text_match(s))
