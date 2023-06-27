# CASE HANDLER UNIT

Video Demo: [video](https://youtu.be/kjRtUrrH-1E)

    This repository contains the final project for Harvard's CS50's Introduction to Programming with Python course. The project is a Case Handler Unit, which allows you to transform text from the clipboard and paste the result instantly.

## Author

- Gilberto Granados Zapatero

## Description

The Case Handler Unit is a graphical user interface (GUI) application built using the tkinter library in Python. It provides several operations to modify text, such as converting to uppercase, lowercase, title case, and sentence case. Additionally, it allows you to add a prefix or suffix to the text.

## Folder Contents

- project.py: This is the file which contains my main function and the other functions necessary to implement the application.
- test_project.py This is the file with the functions for testing the project.py
- requirements.txt: All pip-installable libraries that I used for this project are listed here.

## How to Use

1. Copy the text you want to modify to the clipboard.
2. Run the Case Handler Unit application.
3. Click on the corresponding button to perform the desired text transformation.
4. The modified text will be copied back to the clipboard automatically.
5. You can paste the modified text wherever you want.

## Requirements

- Python 3.x
- tkinter library
- pyperclip library
- idlelib.tooltip module

## Usage

To start the Case Handler Unit, use python and run the following command:

    $ python project.py

To test the application use pytest and run the following command:

    $ pytest test_project.py

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.