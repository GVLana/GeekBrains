
while True:
    try:
        seconds = int(input("Please, enter time in seconds: "))

        seconds_in_minute = 60
        seconds_in_hour = 60 * 60
        seconds_in_day = 24 * 60 * 60

        days = seconds // seconds_in_day
        seconds = seconds - (days * seconds_in_day)
        hours = seconds // seconds_in_hour
        seconds = seconds - (hours * seconds_in_hour)
        minutes = seconds // seconds_in_minute
        seconds = seconds - (minutes * seconds_in_minute)

    except ValueError:
        print("You entered not a number.")
        continue
    else:
        print(f"{days}:{hours}:{minutes}:{seconds}")
        break
