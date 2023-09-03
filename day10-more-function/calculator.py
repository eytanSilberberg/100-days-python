from logo import logo


def add(prev_num, user_input):
    answer = prev_num+user_input
    print(f'{prev_num}+{user_input}={answer}')
    return answer


def sub(prev_num, user_input):
    answer = prev_num-user_input
    print(f'{prev_num}-{user_input}={answer}')
    return answer


def mult(prev_num, user_input):
    answer = prev_num*user_input
    print(f'{prev_num}*{user_input}={answer}')
    return answer


def divide(prev_num, user_input):
    answer = prev_num/user_input
    print(f'{prev_num}/{user_input}={answer}')
    return answer


def calculate():
    print(logo)
    is_calculating = True
    total = int(input('Select a number '))
    while is_calculating:
        operation = input('Select the Operation you\'d like to do +,-,* or / ')
        user_input = int(input('Select a number '))
        if (operation == '+'):
            total = add(total, user_input)
        elif (operation == '-'):
            total = sub(total, user_input)
        elif (operation == '*'):
            total = mult(total, user_input)
        elif (operation == '/'):
            total = divide(total, user_input)
        else:
            print('Please choose one of the operations ')
        to_continue = ''
        while to_continue != 'y' and to_continue != 'n':
            to_continue = input("Do you wish to continue? Y or N ")
            to_continue = to_continue.lower()
            print(to_continue)
            if to_continue == 'y':
                is_calculating = True
            elif to_continue == 'n':
                is_calculating = False
            else:
                print('Pick a valid option')

    return total


print(calculate())
