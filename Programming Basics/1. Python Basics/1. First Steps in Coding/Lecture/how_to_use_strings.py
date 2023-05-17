first_name='Maria'
last_name='Ivanova'
age=19
sentence=first_name+' '+last_name+'@'+str(age)
print(sentence)

a=1.5
b=2.5
sum='The sum is: '+str(a)+str(b)
print(sum)

first_name=input()
last_name=input()
age=int(input())
# print(first_name+' '+last_name+' '+str(age))
print(f"{first_name} {last_name} {age}")