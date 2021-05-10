''' congradulate function prints the lines with a day of week and user who has a birth day on this day 
    in the following format --- Monday: Name, Name2
                                Tuesday: Name3, Name4 etc 
    users are presented as a list of dictionaries with name and timedate birthday data
    the starting week is the week starting from Monday which is next after current date (e.g. today is May 12th, 2021 (Wednesday)
     - conradilating week starts from May 17th, 2021 (Monday)
    if a user`s birthday is on weekend the celebrating day will be Monday
    a week starts from Monday
'''


def congradulate(users):

    if __name__ == '__main__':
        from collections import defaultdict
        from datetime import datetime, timedelta
        current_date = datetime.now().date()
        current_day = current_date.weekday() # find current day of week to define the week of congratulations
        starting_date = current_date + timedelta(days=7 - current_day) # define Monday of congratulations week
        congrats_dict = defaultdict(list) # use the default dict to print the result in above-mentioned format
        for user in users:
            for key, val in user.items():
                user_birthday = datetime.date(val)
                user_birthday_new = datetime(year=current_date.year, month=user_birthday.month, day=user_birthday.day).date() # amend user`s birthday
                                                                                                                              # year for the correct calculation
                time_delta = user_birthday_new - starting_date
                if -2<=time_delta.days<=0: # check Saturday - Monday birthdays
                    congrats_dict[user_birthday_new.strftime('%A')].append(key) # {Day of week: [Name, Name2 ...]}
                elif 0<time_delta.days<=4: # check weekday birthdays (excluding Monday)
                    congrats_dict[user_birthday_new.strftime('%A')].append(key)
                
        for key, val in congrats_dict.items():
            congrats_string = ', '.join(val) # Name, Name2 ...
            print(f'{key}: {congrats_string}\n') # Day of week: Name, Name2 ...

from datetime import datetime, timedelta
users = [{'Bob': datetime(year=2012, month=5, day=17)}, {'Lili': datetime(year=2012, month=5, day=18)},\
 {'Jake': datetime(year=2012, month=5, day=19)}, {'Margo': datetime(year=2012, month=5, day=20)},\
 {'Gary': datetime(year=2012, month=5, day=23)},{'Vanda': datetime(year=2012, month=5, day=20)}]

congradulate(users)

