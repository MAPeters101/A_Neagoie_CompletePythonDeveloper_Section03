

# username = input("Please enter your username: ")
# password = input("Please enter your password: ")
# password_len = len(password)
# print(f'{username}, your password {'*'*password_len} is {password_len} letters long.')
# print('-'*80)

username = input("What is your username: ")
password = input("What is your password: ")
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password, {hidden_password}, is {password_length} letters long.')


