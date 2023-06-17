DEFAULT_MESSAGE = "It's cold outside!"

output_dict = {
    "sunny": "It's warm outside!",
}

input_message = input()

# if input_message in output_dict:
#     print(output_dict[input_message])
# else:
#     print(DEFAULT_MESSAGE)

print(output_dict[input_message]) if input_message in output_dict else print(DEFAULT_MESSAGE)
