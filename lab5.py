# letter М
X1 = (
     1, -1, -1, -1, -1, -1,  1,
     1,  1, -1, -1, -1,  1,  1,
     1, -1,  1, -1,  1, -1,  1,
     1, -1, -1,  1, -1, -1,  1,
     1, -1, -1, -1, -1, -1,  1,
     1, -1, -1, -1, -1, -1,  1,
     1, -1, -1, -1, -1, -1,  1,
)

# letter К
X2 = (
    1, -1, -1, -1, -1,  1,  -1,
    1, -1, -1, -1,  1, -1,  -1,
    1, -1, -1,  1, -1, -1,  -1,
    1,  1,  1, -1, -1, -1,  -1,
    1, -1, -1,  1, -1, -1,  -1,
    1, -1, -1, -1,  1, -1,  -1,
    1, -1, -1, -1, -1,  1,  -1,
)


def show_letter(letter):
    curr_index = 0
    for x in letter:
        curr_index += 1
        print('#' if x == 1 else ' ', end=('\n' if curr_index % 7 == 0 else ' '))


def decode_letter(letter):
    result = []
    for line in letter.split('\n'):
        result += [int(x) for x in line.split()]
    return result


def analyze_letter(letter, n_uw, n_ub):
    res_value = 0
    for i in range(len(letter)):
        res_value += n_uw[i] * letter[i] + n_ub[i]
    return res_value


def train_model():
    letter_m_y, letter_k_y = 1, -1
    bias, weight = 0, 0
    u_weight, u_bias = [], []
    n_uw, n_ub = [], []

    for x in X1:
        u_weight.append(weight + x * letter_m_y)
        u_bias.append(bias + letter_m_y)

    for i in range(len(X2)):
        n_uw.append(u_weight[i] + X2[i] * letter_k_y)
        n_ub.append(u_bias[i] + letter_k_y)

    return n_uw, n_ub


with open('letters_data.txt') as file:
    result = file.read()
    letters = result.split('END\n')

    show_letter(X1)
    print('Letter for learning M\n')

    show_letter(X2)
    print('Letter for learning K\n')

    print('\n\n-_-_-_-_-_-_-_-_-_- Letters recognition -_-_-_-_-_-_-_-_-_-\n')

    n_uw, n_ub = train_model()

    for letter in letters:
        res_letter = decode_letter(letter)
        res_value = analyze_letter(res_letter, n_uw, n_ub)
        show_letter(res_letter)

        if res_value > 0:
            print('Recognized letter M\n')
        elif res_value < 0:
            print('Recognized letter K\n')
        else:
            print('Can not recognize letter\n')

