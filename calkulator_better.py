def main():
    next_operation = True
    while next_operation:
        print('Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:')

        print('')
        input_1 = input('liczba > ')
        while not isfloat(input_1):
            print('To nie jest liczba!')
            input_1 = input('> ')

        number_1 = float(input_1)


        print('')
        operation = input("operacja > ")
        while operation not in ['+', '-', '*', '/', '%']:
            print('Niepoprawna operacja!')
            operation = input("operacja > ")

        print('')
        input_2 = input('liczba > ')
        correct_input_2 = False
        while not correct_input_2:
            if not isfloat(input_2):
                print('')
                print('To nie jest liczba!')
                input_2 = input('> ')
            else:
                number_2 = float(input_2)
                if number_2 == 0.0 and (operation == '/' or operation == '%'):
                    print('')
                    print('Dzielenie przez zero!')
                    input_2 = input('liczba > ')
                else:
                    correct_input_2 = True

        result = False
        if operation == '+':
            result = number_1 + number_2
        elif operation == '-':
            result = number_1 - number_2
        elif operation == '*':
            result = number_1 * number_2
        elif operation == '/':
            result = number_1 / number_2
        elif operation == '%':
            result = number_1 % number_2
        result = round(result, 2)
        print('kalkuluję %s %s %s = %s' % (input_1, operation, input_2, result))
        print('')

        answer = ''
        while answer != 'n' and answer != 't':
            answer = input('Chcesz wykonać kolejne działanie? Wpisz literę t lub n. ')

        if answer == 'n':
            next_operation = False

    print('The End')


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


if __name__ == "__main__":
    main()
