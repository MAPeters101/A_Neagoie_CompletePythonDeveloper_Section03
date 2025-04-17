name = 'Johnny'
age = 55
print('hi ' + name)
#print('hi ' + name + '. You are ' + age + ' years old')
print('hi ' + name + '. You are ' + str(age) + ' years old')
print('hi {name}. You are {age} years old')
print(f'hi {name}. You are {age} years old')
print()
print('hi {}. You are {} years old'.format('Johnny', '55'))
print('hi {}. You are {} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
#print('hi {1}. You are {0} years old'.format(new_name='sally', age=100))
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))


