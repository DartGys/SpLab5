from yacc_grammar import parser


def main():
    while True:
        try:
            userInput = input('Enter a statement or expression: ')
        except EOFError:
            break
        result = parser.parse(userInput)
        print(result)


if __name__ == '__main__':
    main()
