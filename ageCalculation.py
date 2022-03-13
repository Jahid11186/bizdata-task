date_of_birth = input("Enter your date of birth (dd-mm-yyyy): ")
date_of_today = input("Enter current date (dd-mm-yyyy): ")


def input_collector(date):
    data = []
    flag = []
    shift = 0
    for i in range(len(date)):
        if date[i] == '-':
            flag.append(i)

    flag.append(-1)

    for item in flag:
        if item == -1:
            data.append(date[shift:])
        else:
            data.append(date[shift:item])
            shift = item + 1
    return data


birth = input_collector(date_of_birth)
current = input_collector(date_of_today)


def age_calculator(date_birth, date_today):
    birth_day, birth_month, birth_year = int(date_birth[0]), int(date_birth[1]), int(date_birth[2])
    current_day, current_month, current_year = int(date_today[0]), int(date_today[1]), int(date_today[2])

    if birth_day > current_day:
        current_day += 30
        current_month -= 1
    else:
        current_day = current_day

    age_in_days = current_day - birth_day  # age in days

    if birth_month > current_month:
        current_month += 12
        current_year -= 1
    else:
        current_month = current_month

    age_in_months = current_month - birth_month  # age in month
    age_in_years = current_year - birth_year  # age in year

    age_str = "Your age: {0} years {1} months {2} days".format(age_in_years, age_in_months, age_in_days)
    return age_str


print(age_calculator(birth, current))