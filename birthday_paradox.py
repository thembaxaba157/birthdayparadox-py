from statistics import multimode
import getpass
import datetime
import random


def num_bday_input():
    
    num_bday = input('How many birthdays shall I generate? (Max 100)\n > ')
    while not num_bday.isdigit() or int(num_bday)>100 or int(num_bday)<1:
        num_bday = input('How many birthdays shall I generate? (Max 100)\n > ')
    return int(num_bday)


def gen_rand_dates(num_bday):
    random_dates_list = []
    start_date ,end_date= datetime.date(2020, 1, 1),datetime.date(2020, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    for i in range(num_bday):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        random_dates_list.append(random_date.strftime("%b %d"))
    return random_dates_list


def intro_message():
    print('Birthday Paradox, by Al Sweigart al@inventwithpython.com and coded by thembaxaba157\n')


def print_birthdays(random_dates):
    print(f'\nHere are {len(random_dates)} birthdays:')
    print(*random_dates, sep=', ')


def first_sim_message(random_dates):
    x = list(set([i for i in random_dates if random_dates.count(i)>1]))
    message_conc = ''
    if len(x) == 0:
        message_conc = 'none of the dates'
    
    print(f'\nIn this simulation, multiple people have a birthday on {message_conc}',end='')
    print(*x, sep=', ')


def first_simulation(num_bday):
    random_dates = gen_rand_dates(num_bday)
    print_birthdays(random_dates)
    first_sim_message(random_dates)

def matching_birth_count(random_dates):
    if list(set([i for i in random_dates if random_dates.count(i)>1])):return 1
    else: return 0


def hun_thou_simulations(num_bdays):
    print(f'Generating {num_bdays} random birthdays 100,000 times...')
    getpass.getpass('Press Enter to begin...')
    match_birth = 0
    print('0 simulations run...')
    for i in range(0,100000):
        random_dates = gen_rand_dates(num_bdays)
        match_birth += matching_birth_count(random_dates)

        if (i+1)%10000 == 0:print(f'{i+1} simulations run...')

    return match_birth


def final_message(match_birth,num_bday):
    print(f'''Out of 100,000 simulations of {num_bday} people, there was a
matching birthday in that group {match_birth} times. This means
that {num_bday} people have a {100*(match_birth/100000)} % chance of
having a matching birthday in their group.
That's probably more than you would think!''')


def birth_para():
    intro_message()
    num_bday = num_bday_input()
    first_simulation(num_bday)    
    match_birth = hun_thou_simulations(num_bday)
    final_message(match_birth,num_bday)


if __name__ == '__main__':
    birth_para()
