import validators

def main():
    e_mail = ""
    print(validator(e_mail))

def validator(e_mail):

    e_mail = input("What's your email address?: ")
    if validators.email(e_mail):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()

