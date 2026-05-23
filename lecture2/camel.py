def main():
    variable = input("Variable name: ")
    print(camel_to_snake(variable))

def camel_to_snake(text):
    upper_case_str = "QWERTYUIOPASDFGHJKLZXCVBNM"
    snake_str = ""
    for letter in text:
        if letter in upper_case_str:
            snake_str += "_" + letter.lower()
        else:
            snake_str += letter
    return snake_str

main()