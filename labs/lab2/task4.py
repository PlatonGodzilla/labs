def describe_person(name, age=30):
    if name.isalpha():
        return f'Это {name} и ему {age} лет'
    else:
        return('буквами пиши')
print(describe_person(input()))