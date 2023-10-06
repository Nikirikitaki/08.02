from datetime import date, datetime, timedelta

start_date = date.today()
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

def get_period(start_date, num_days):
    result = {}
    for i in range(num_days):
        result[(start_date.day, start_date.month)] = start_date.year
        start_date += timedelta(1)
    return result

def get_birthdays_per_week(users):
    start_date = date.today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # users_dict = {day: [] for day in days}
    empty_dict = {}
    start_date = date.today()
    period = get_period(start_date, 7)
    if not users:
        return empty_dict
    for user in users:
        user_name = user["name"]
        birthday = user["birthday"]
        
        date_birthday = (birthday.day, birthday.month)
        if date_birthday in period:
            birthday = birthday.replace(year=period[date_birthday])
            day_of_week = birthday.weekday()
            if day_of_week == 5 or day_of_week == 6:
                day_of_week = 0
            day_name = days[day_of_week]
            if empty_dict.get(day_name):
                empty_dict[day_name].append(user_name)
            else:
                empty_dict[day_name] = [user_name] 
    print(empty_dict)
    return empty_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum1", "birthday": datetime(2023, 9, 30).date()},
        {"name": "Jan Koum2", "birthday": datetime(2023, 9, 27).date()},
        {"name": "Jan Koum3", "birthday": datetime(2023, 9, 30).date()},
        {"name": "Jan Koum4", "birthday": datetime(2023, 10,3 ).date()},
    ]

    result = get_birthdays_per_week(users)
    
    # Выводим результат1
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
