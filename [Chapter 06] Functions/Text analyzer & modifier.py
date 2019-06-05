def get_num_of_characters(input_str):
    # Type your code here
    return  len(input_str)
def output_without_whitespace(input_str):
    string = ''
    for c in input_str:
        if c != ' ':
            string += c
    return string


if __name__ == '__main__':
    phrase = input('Enter a sentence or phrase:\n\n')
    print('You entered:', phrase)
    print('\nNumber of characters:', get_num_of_characters(phrase))
    print('String with no whitespace:',output_without_whitespace(phrase))
    
