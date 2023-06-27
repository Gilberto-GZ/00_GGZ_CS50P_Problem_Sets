import sys
import requests

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif float(sys.argv[1]) == False:
            sys.exit("Command-line argument is not a number")
        else:
            print("$", f"{get_price():,.4f}", sep = "")
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_price():

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r_content = r.json()
    r_dict = r_content["bpi"]
    r_usd = r_dict["USD"]
    r_rate = r_usd["rate_float"]* float(sys.argv[1])
    return r_rate

if __name__ == "__main__":
    main()