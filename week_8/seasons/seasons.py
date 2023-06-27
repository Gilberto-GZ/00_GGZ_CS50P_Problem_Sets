import sys
import inflect
from datetime import date
from datetime import timedelta

def main():

    p = inflect.engine()



    age_words = p.number_to_words(age()).replace(" and", "").capitalize()
    print(age_words + " minutes")

def age():
    try:
        year, month, day = input("Date of Birth: ").split("-")
        delta_date = current_date() - birthday(year, month, day)
        age = round(delta_date.total_seconds()/60)
        return age

    except (ValueError, TypeError):

        print("Invalid Date")
        sys.exit(1)



def birthday(year, month, day):
    try:
        birth_date = date(int(year), int(month), int(day))
        return birth_date
    except (ValueError, TypeError):
        return "Invalid Date"

def current_date():

    try:
        current_date = date.today()
        return current_date
    except (ValueError, TypeError):
        return "Invalid Date"

if __name__ == "__main__":
    main()