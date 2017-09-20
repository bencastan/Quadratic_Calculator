import quadratics

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------')
    print('     CALCULATOR APP')
    print('-------------------------------')
    print()


def run_event_loop():
    print('What do you want to Calculate ?')
    cmd = 'EMPTY'

    while cmd.lower().strip() != 'x' and cmd:
        cmd = input('[Q]uadratics, [O]ther, or E[x]it ?')
        cmd = cmd.lower().strip()
        if cmd == "q":
            quadratics.header()
            num_a, num_b, num_c = quadratics.get_values()
            d = quadratics.get_discriminant(num_a, num_b, num_c)
            if d < 0:
                print('This equation has no real solution!')
            elif d == 0:
                print('This equation has one solution: {}'.format(quadratics.one_solution(num_a, num_b, d)))
            else:
                x, y = quadratics.two_solution(num_a, num_b, num_c, d)
                print('This equation has two solutions: {} or {}'.format(x, y))

        elif cmd == 'o':
            print("Not working yet")
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}.".format(cmd))
            print('Goodbye!')


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('Item {} is {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text,data)

if __name__ == '__main__':
    main()
