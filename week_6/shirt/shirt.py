import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    checking_command_line_arg()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_file = Image.open("shirt.png")

    shirt_size = shirt_file.size

    muppet_resize = ImageOps.fit(image_file, shirt_size)

    muppet_resize.paste(shirt_file, shirt_file)

    muppet_resize.save(sys.argv[2])




def checking_command_line_arg():

    n = len(sys.argv)

    if n < 3:
        sys.exit("Too few command-line arguments")
    elif n > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if checking_ext_file(file1[1]) == False:
        sys.exit("Invalid input")

    if checking_ext_file(file2[1]) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")



def checking_ext_file(file):

    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()