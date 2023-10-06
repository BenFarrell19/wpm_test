import json
'''
lst = json.load(open('log', 'r'))

del_count = 0
for i, index in enumerate(lst):
    if index == 'space':
        lst[i] = ' '
    elif index == 'Key.shift':
        lst[i] = ''
    elif index == 'del':
        lst[i] = ''
        del_count += 1
    elif index == 'shift':
        lst[i] = ''
        # count the number of times del pressed to determine how far back in text person went
        # then take from where they deleted back to to where the deletes stars in file and check that section for errors
        # to see if they were just rewording or if there was an error
a = ''.join(lst)
print(a)
json.dump(a, open("uncorrected", 'w'))
'''

corrected = json.load(open('corrected', 'r'))
uncor = json.load(open('uncorrected', 'r'))

print(uncor)
print(corrected)


