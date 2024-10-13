def write_inp(input_str: str):
   with open('user_input.txt', 'a') as file:
      file.write(input_str)
inp = input('Введите желаемый текст>>> ')
write_inp(inp)
print('“Успешно записано»')