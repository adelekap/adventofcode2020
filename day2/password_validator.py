from day2.input import read_password_input


def validate_passwords():
    passwords = read_password_input()
    valid_passwords = [p for p in passwords if p.is_valid_password()]
    return valid_passwords


if __name__ == '__main__':
    valid = validate_passwords()
    print(f'{len(valid)} valid passwords')
