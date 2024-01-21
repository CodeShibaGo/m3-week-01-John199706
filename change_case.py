def change_case(input_str, case):
    if case == "upper":
        input_str = input_str.upper()
    elif case == "lower":
        input_str = input_str.lower()
    return input_str
result = change_case("Hello","upper")
print(result)

