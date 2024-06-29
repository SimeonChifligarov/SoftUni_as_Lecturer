username = input('insert your username: ')
password = input('insert password: ')

attempt = input('please login with correct password: ')
while attempt != password:
    # print('wrong password')
    attempt = input('please login with correct password: ')

print(f'Welcome {username}!')
