# def multi(a, b):
#     try:
#         return a * b
#     except TypeError:
#         #return 0
#         print('To nie jest liczba!')
#
# multi('a', 'b')
import logging


# def multi(a, b):
#     return a*b

# try:
#     print(multi('a','b'))
# except TypeError:
#     logging.warning('Podane złe dane wejściowe')


# dla leniwych
# try:
#     print(multi('a','b'))
# except Exception as e: # jak nie znamy typu bledu, wtedy w opisie bledu sie dokladnie pojawi
#     logging.warning(e)

# def multi(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         return 0
#
#
# print(multi('3', '5'))  # ok
# print(multi('a', 'b'))  # value error
# print(multi(None, 5))  # type error

def multi(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return 0


# def check_age(users, age):
#     count = 0
#     for user in users:
#         try:
#             if int(user['age']) < age:
#                 count += 1
#         except KeyError:
#             print('Niepoprawne dane: {}'.format(user))
#         except ValueError:
#             print('Niepoprawny wiek: {}'.format(user)) # mozna wiele wyjatkow dodawac albo w () - jak maja miec ten sam efekt dzialania, albo pod soba z roznymi efektami
#     return count


# def check_age(users, age):
#     count = 0
#     for i, user in enumerate(users):  # iteruje z automatu np po slownikach
#         try:
#             user_age = int(user['age'])
#         except KeyError:
#             print('Niepoprawne dane: {}'.format(user))
#         except ValueError:
#             print('Niepoprawny wiek: {}'.format(
#                 user))  # mozna wiele wyjatkow dodawac albo w () - jak maja miec ten sam efekt dzialania, albo pod soba z roznymi efektami
#         else:
#             count += 1 if user_age < age else 0
#         finally:
#             print('{}.{}'.format(i, user))
#     return count

#zmniejszenie def przez rozbicie na 2 siostrzane

def _check_age (users, age):
    count = 0
    for i, user in enumerate(users):
        if int(user['age']) < age:
            count += 1
    return count


def check_age(users, age):
    try:
        return _check_age(users, age)
    except (KeyError, ValueError):
        print('Niepoprawne dane:')
    return 0




invalid_date = [{'name': 'Jan', 'age': 'sto'},
                {'name': 'Ewa', 'age': '10'},
                {'name': 'ola', 'age': '23'}]

valid_date = [{'name': 'Jan', 'age': '10'},
              {'name': 'Ewa', 'age': '25'},
              {'name': 'Ola', 'age': '23'}]

print(check_age(invalid_date, 11))
