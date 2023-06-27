# Main function
def main():
    #str to face
    a = input("How are you: " )
    print(convert(a))




# Creating the "convert" function
def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")

main(