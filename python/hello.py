#create variable:
name = input()
#name = 'masu'
n = None;


#print value:
# print(f'hello world {name}')
# print('hello world ' + name)

#Conditional
if name == 'masu':
    name = name + ' The Great'
    print(f'yess, na him {name}')
elif name == 'brymo':
    print('inaa, dan iskan ne')
else:
    print('bamu san shi ba')

#dataSets
    #tuple
friends = ['Abba', 'Amina', 'Zahra']
    #list
coordinates = (10.0, 71.03)
    #set, only accepts a value once, no duplicate values
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.remove(3)
print(s)
    #Dictionaries(objects)
ages = {
    'Amrah': 21,
    'Zahra': 18,
    'Moriki': 17
}
ages('Zahra') += 2
ages('Hammam') = 25

#Loops
for i in range(5):
    print(i)

for i in friends:
     print(i)
