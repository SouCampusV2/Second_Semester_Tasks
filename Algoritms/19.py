def replace_exclamation_with_index(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if char == '!':
            result += str(i)
        else:
            result += char
    return result

# Пример использования:
input_str = "Hello! World!!____abcd!"
output_str = replace_exclamation_with_index(input_str)
print(output_str)
