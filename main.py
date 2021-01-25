# it is simple program for calculate daily calorie

from colored import fg, bg, attr

print(fg('yellow') + '\tHi there! I will help you calculate your daily calories\n')


def calc():
    color1 = bg('blue') + fg('black')
    color2 = bg('yellow') + fg('black')
    reset = attr('reset')

    try:
        gender = input(color1 + 'Please print your gender : Male or Female :' + reset)

        if gender == 'male' or gender == 'Male':
            gender = 'Man'
        elif gender == 'female' or gender == 'Female':
            gender = 'Woman'
        else:
            print('something is wrong try')
            return calc()

        name = input(color1 + 'Please print your name :' + reset)
        if not name.isalpha():
            print('Only letters! ')
            return calc()

        age = int(input(color1 + 'Please print your age :' + reset))
    except ValueError:
        print('You not write a number!')
        return calc()

    try:
        weight = float(input(color1 + 'Please print your weight (kg) :' + reset))
    except ValueError:
        print('Wrong you not write number')
        return calc()

    try:
        choose = input(color2 + 'Please choose one answer: \nA) {}\nB) {}\nC) {}\nD) {}'.format
        ('I wdddill be less active.☠️',
         'active 1 or 2 times a week.🥺',
         'active 3 or 4 times a week😎',
         'Always👍🏻\n',
         'Answer: ' + reset))

        if choose == 'A' or choose == 'a':
            point = 1.2
        elif choose == 'B' or choose == 'b':
            point = 1.4
        elif choose == 'C' or choose == 'c':
            point = 1.5
        elif choose == 'D' or choose == 'd':
            point = 1.7
        else:
            print(fg('white'), 'Something is wrong', reset)
            return calc()

    except NameError:
        print('')
        return calc()

    c = weight * 24 * point * age / age

    print(fg('white') + '\tHi', name.capitalize(), 'it is your daily calorie', int(c), 'kcal', reset)

    again = input(fg('red') + '\tDo u want again (y/n) :\n')

    if again == 'y' or again == 'Y':
        print(fg('white') + 'Good job', name.capitalize())
        return calc()
    elif again == 'N' or again == 'n':
        print(fg('blue') + 'Thanks for using', name.capitalize(), 'you are best', gender)
        quit()
    else:
        print('Please write y or n', name.capitalize())


calc()
