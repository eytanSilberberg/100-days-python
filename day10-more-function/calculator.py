from logo import logo


def add(prev_num, user_input):
    answer = prev_num+user_input
    return answer


def sub(prev_num, user_input):
    answer = prev_num-user_input
    return answer


def mult(prev_num, user_input):
    answer = prev_num*user_input
    return answer


def divide(prev_num, user_input):
    answer = prev_num/user_input
    return answer


operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': divide
}


def calculate():
    print(logo)
    is_calculating = True
    total = float(input('Select a number '))
    while is_calculating:
        operation = input('Select the Operation you\'d like to do +,-,* or / ')
        user_input = float(input('Select a number '))
        is_valid_operation = False
        while not is_valid_operation:
            if operation != '+' and operation != '-' and operation != '*' and operation != '/':
                print('Please choose one of the operations ')
            else:
                answer = operations[operation](total, user_input)
                print(f'{total} {operation} {user_input} = {answer}')
                total = answer
                is_valid_operation = True
        wish_to_continue = input(
            'Wish to continue? Please choose Y or N').lower()
        if wish_to_continue == 'y':
            is_calculating = True
        elif wish_to_continue == 'n':
            is_calculating = False

    return total


print(calculate())
