def greet(name):
    if name.isalpha():
        return(f'привет, {name}!')
    else:
        return('буквами пиши')
print(greet(input()))