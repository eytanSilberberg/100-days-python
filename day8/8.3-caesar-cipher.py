import math
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def get_correct_shift(shift):
    if shift > 26:
        multipy_by = shift / 26
        shift = shift - (26 * math.floor(multipy_by))
    return shift

# Encrypt and Decrypt on their own


def encrypt(text, shift):
    shift = get_correct_shift(shift)
    new_text = ''
    for i in text:
        index_of_char = alphabet.index(i)
        correct_idx = 0
        curr_idx = shift + index_of_char
        if curr_idx > 26:
            correct_idx = curr_idx - 26
        else:
            correct_idx = curr_idx
        new_text += alphabet[correct_idx]
    print(f'The encoded text is {new_text}')


def decrypt(text, shift):
    shift = get_correct_shift(shift)
    new_text = ''
    for i in text:
        index_of_char = alphabet.index(i)
        correct_idx = 0
        curr_idx = index_of_char - shift
        if curr_idx < 0:
            correct_idx = curr_idx + 26
        else:
            correct_idx = curr_idx
        new_text += alphabet[correct_idx]
    print(f'The decoded text is {new_text}')

# Encrypt and Decrypt together


def casear(text, shift, direction):
    shift = get_correct_shift(shift)
    new_text = ''

    for i in text:
        index_of_char = alphabet.index(i)
        correct_idx = 0
        if direction == 'encode':
            curr_idx = shift + index_of_char
            if curr_idx > 26:
                correct_idx = curr_idx - 26
            else:
                correct_idx = curr_idx
        elif direction == 'decode':
            curr_idx = index_of_char - shift
            if curr_idx < 0:
                correct_idx = curr_idx + 26
            else:
                correct_idx = curr_idx
        new_text += alphabet[correct_idx]
    print(new_text)


casear(text, shift, direction)
