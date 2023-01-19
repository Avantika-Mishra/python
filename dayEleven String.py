name = "Avantika"
friend = "Aman"
AnotherFriend = 'Mayank'
print("Hello " + name)
print("Hello " + AnotherFriend)

Sentence = 'He said,"I want to eat an apple"'
print(Sentence)
#Multiline Strings
Sentence = '''He said, "I want to eat an apple and an orange
Can you please go to the market.'''
print(Sentence)
#indexing is like an array
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
#it throws an error bcoz there is nothing on eighth index
#print(name[8])
print("Lets use a for loop\n")
#Looping through the string
for character in name:
  print(character)

for character in Sentence:
  print(character)
  