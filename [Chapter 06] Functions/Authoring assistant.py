# Type all other functions here
def get_num_of_non_WS_characters(user_str):
    count = 0
    for c in user_str:
        if c != ' ':
            count += 1
    return count

def get_num_of_words(user_str):
    user_list = user_str.split(' ')
    for word in user_list:
        if word == '':
            user_list.remove('')
          
    for word in user_list:
        if word == '':
            user_list.remove('')
                    
    print(user_list)
    return len(user_list)
    
def fix_capitalization(user_str):
    count = 0
    is_new_sentence = True
    string = ''

    if len(user_str) > 0:
        for c in user_str:
            if is_new_sentence and c.islower():
                is_new_sentence = False
                count += 1
                string += c.upper()
            elif is_new_sentence and c.isupper():
                is_new_sentence = False
                string += c
            elif c == '.':
                is_new_sentence = True
                string += c
            else:
                string += c
    return string, count        
    
def replace_punctuation(user_str, exclamation_count = 0, semicolon_count = 0):
    ex = exclamation_count
    semi = semicolon_count
    text = ''
    if len(user_str) > 0:
        for c in user_str:
            if c == '!':
                ex += 1
                text += '.'
            elif c == ';':
                semi += 1
                text += ','
            else:
                text += c
    print('Punctuation replaced')
    print('exclamation_count:', ex)
    print('semicolon_count:', semi)
    return text
    
def shorten_space(user_str):
    text = ''
    if len(user_str) > 0:
        for i in range(0,len(user_str)-1):
            if not(user_str[i] == ' ' and user_str[i+1] == ' '):
                text += user_str[i]
        text += user_str[-1]
    return text

def print_menu(user_str):
    menu = '\nMENU\n'\
    'c - Number of non-whitespace characters\n'\
    'w - Number of words\n'\
    'f - Fix capitalization\n'\
    'r - Replace punctuation\n'\
    's - Shorten spaces\n'\
    'q - Quit\n'
    print(menu)
    
    menu_op = input('Choose an option:\n')
    while menu_op != 'q':
        if menu_op == 'c':
            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(user_str))
        elif menu_op == 'w':
            print('Number of words:',get_num_of_words(user_str))
        elif menu_op == 'f':
            text, num = fix_capitalization(user_str)
            print('Number of letters capitalized:', num)
            print('Edited text:', text)
        elif menu_op == 'r':
            text = replace_punctuation(user_str)
            print('Edited text:', text)
        elif menu_op == 's':
            text = shorten_space(user_str)
            print('Edited text:', text)
        
        print(menu)
        menu_op = input('Choose an option:\n')

    return menu_op, user_str


if __name__ == '__main__':
    sample_text = input('Enter a sample text:\n\n')
    print('You entered:', sample_text)
    print_menu(sample_text)
