is_loop_exit = False
is_c = False
is_o = False
is_n = False

cuttent_string = ""
result_string = ""

while (not is_loop_exit):
    input_string = input()

    if input_string.lower() == "end":  # "END".lower() => 'end'
        is_loop_exit = True
    else:
        if input_string == "c" and not is_c:
            is_c = True
        elif input_string == "o" and not is_o:
            is_o = True
        elif input_string == "n" and not is_n:
            is_n = True
        else:
            if input_string.isalpha():
                cuttent_string = f"{cuttent_string}{input_string}"

        is_code_complete = (is_n and is_o and is_c)
        if (is_code_complete):
            result_string = f"{result_string}{cuttent_string} "
            cuttent_string = ""
            is_c = False
            is_o = False
            is_n = False

print(result_string)
