def is_very_long(a):
    return len(a) > 12
        
    
def has_digit(a):
    return any(b.isdigit() for b in a)


def has_upper_letters(a):
    return any(b.isupper() for b in a)


def has_lower_letters(a):
    return any(b.islower() for b in a)


def has_symbols(a):
    return not all(b.isalpha() or b.isdigit() for b in a)


def main():
    a = input('Введите пароль: ')
    check = (
        is_very_long(a), 
        has_digit(a), 
        has_symbols(a), 
        has_upper_letters(a), 
        has_lower_letters(a),
    )    
    score = 0
    b = len
    for scoring_points in check:
        a = str(scoring_points)
        comparison_variable = b(a)
        if comparison_variable < 5:
            score += 2   
    print('Рейтинг пароля:',score)


if __name__ == '__main__':
    main()
 