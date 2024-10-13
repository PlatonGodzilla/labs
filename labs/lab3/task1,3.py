def read_file(filename: str, read_all: bool):
    try:
       with open(filename, 'r') as file:
          if read_all: 
            return file.read()
          else:
             filecontent = ""
             for line in file:
                filecontent += line
       return filecontent
    except FileNotFoundError:
        print("К сожалению искомый файл не существует")
print(read_file(input(), True))