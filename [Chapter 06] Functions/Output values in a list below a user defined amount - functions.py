''' Define your function here '''
def get_user_values():
    user_values = []
    num = int(input())
    for i in range(0,num):
        user_values.append(int(input()))
    upper_threshold = int(input())
    return user_values, upper_threshold

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for i in user_values:
        if i <= upper_threshold:
            print(i)


if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

