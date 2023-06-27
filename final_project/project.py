"""
Final project for Harvard's CS50's Introduction to Programming with Python

Case Handler Unit: Transform the text from the clipboard and paste the result instantly.

Author: Gilberto Granados Zapatero

"""

import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
import pyperclip


def main():

    gui()

# Update clipboard content
def refresh_clipboard():

    # Define text and text_in_preview as global variables
    global text, text_in_preview

    # Getting clipboard text
    text = pyperclip.paste()

    # If multiple lines get only first for the preview
    first_row = text.splitlines()[0] if text else ""

    # If first line is very long, take only first 26 characters to preview
    if len(first_row) > 26:
        text_in_preview = first_row[0:26] + "..."
    else:
        text_in_preview = first_row

    return text, text_in_preview

def gui():

    # GUI part

    # Create the main window
    window = tk.Tk()
    window.title("Case Handler Unit")

    # Set the window decorations and dimensions
    window.geometry("270x700")

    # Create a label for previewing the clipboard content
    preview_in_label = tk.Label(window, text="Case IN: ", wraplength=260, height=1, fg="#666666")
    preview_in_label.pack(pady=5)

    # Create labels for text length and word count
    length_label = tk.Label(window, text="Text Length:")
    length_label.pack(pady=5)

    word_count_label = tk.Label(window, text="Word Count:")
    word_count_label.pack(pady=5)

    # Create button widget for uppercase text
    uppercase_button = tk.Button(window, text="| CONVERT TO UPPERCASE |", font=("Sans", 12), bg="white", height=(1), width=(25), command=lambda: convert_to_uppercase(refresh_clipboard(), text_in_preview, preview_out_label))
    uppercase_button.pack(pady=10)
    my_tip = Hovertip(uppercase_button, "Convert copied text to Upper Case", hover_delay=300)

    # Create button widget for lowercase text
    lowercase_button = tk.Button(window, text="| convert to lowercase |", font=("Sans", 12), bg="white", height=(1), width=(25), command=lambda: convert_to_lowercase(refresh_clipboard(), text_in_preview, preview_out_label))
    lowercase_button.pack(pady=10)
    my_tip = Hovertip(lowercase_button, "Convert copied text to Lower Case", hover_delay=300)

    # Create button widget for title case text
    titlecase_button = tk.Button(window, text="| Convert To Title Case |", font=("Sans", 12), bg="white", height=(1), width=(25), command=lambda: convert_to_titlecase(refresh_clipboard(), text_in_preview, preview_out_label))
    titlecase_button.pack(pady=10)
    my_tip = Hovertip(titlecase_button, "Convert copied text to Title Case", hover_delay=300)

    # Create button widget for sentence case text
    sentencecase_button = tk.Button(window, text="| Convert to sentence case |", font=("Sans", 12), bg="white", height=(1), width=(25), command=lambda: convert_to_sentencecase(refresh_clipboard(), text_in_preview, preview_out_label))
    sentencecase_button.pack(pady=10)
    my_tip = Hovertip(sentencecase_button, "Convert copied text to Sentence case", hover_delay=300)

    # Create label for prefixer
    prefix_entry = tk.Entry(window)
    prefix_entry.pack(pady=5)

    # Create button widget for prefixer
    button_prefix = tk.Button(window, text="Prefix",font=("Sans", 10), bg="white", command=lambda: prefix_text(refresh_clipboard(), prefix_entry, preview_out_label))
    button_prefix.pack(pady=5)

    # Create label for suffixer
    suffix_entry = tk.Entry(window)
    suffix_entry.pack(pady=5)

    # Create button widget for suffixer
    button_suffix = tk.Button(window, text="Suffix",font=("Sans", 10), bg="white", command=lambda: suffix_text(refresh_clipboard(), suffix_entry, preview_out_label))
    button_suffix.pack(pady=5)

    # Update text length and word count information on button click
    update_button = tk.Button(window, text="Text Info",font=("Sans", 10), bg="#c9daf8", command=lambda: text_info(refresh_clipboard(), text_in_preview, preview_in_label, length_label, word_count_label))
    update_button.pack(pady=10)
    my_tip = Hovertip(update_button, "Show info about copied text", hover_delay=300)

    # Create a label for previewing the text converted
    preview_out_label = tk.Label(window, text="Case OUT: ", wraplength=260, height=1, fg="#666666")
    preview_out_label.pack(pady=10)

    # Create the "Help" button
    help_button = tk.Button(window, text="About", font=("Sans", 10), bg="white", command=lambda: toggle_instructions(instructions_frame))
    help_button.pack(side=tk.TOP)

    # Create a frame for the instructions panel
    instructions_frame = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=12, width=35)

    # Create a label with the instructions
    instructions_label = tk.Label(instructions_frame,
    text="Welcome to Case Handler Unit, use it is very \n\
    easy. \n1.- You just need to Copy to clipboard any \n\
    text string you want to convert.\n\
    2.- Then click on a button to transform\n\
    yor text as you need. \n\
    3.- And finally paste your converted text string \n\
    where you want.", height=(12), width=(35), justify="center", bg="lightgray")

    instructions_label.pack(padx=10, pady=10)

    # Start with the instructions panel hidden
    instructions_frame.pack_forget()

    window.mainloop()

# CASE HANDLER UNIT FUNCTIONS

# Toggle instructions pane
def toggle_instructions(instructions_frame):

    if instructions_frame.winfo_ismapped():
        instructions_frame.pack_forget()
    else:
        instructions_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Show data about text in the clipboard
def text_info(text, text_in_preview, preview_in_label, length_label, word_count_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        # Calculate the length of the text
        text_length = len(text)

        # Count the occurrences of each word
        word_count = len(text.split())

        # Update the preview, length and word count labels
        preview_in_label.config(text=f"Case IN: {text_in_preview}")
        length_label.config(text=f"Text Length: {text_length}")
        word_count_label.config(text=f"Word Count: {word_count}")

        return text, text_in_preview

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to uppercase
def convert_to_uppercase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_upper = text.upper()
        text_out_preview = text_in_preview.upper()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_upper)
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_upper

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to lowercase
def convert_to_lowercase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_lower = text.lower()
        text_out_preview = text_in_preview.lower()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_lower)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_lower

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to title case
def convert_to_titlecase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_title = text.title()
        text_out_preview = text_in_preview.title()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_title)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_title

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to sentence case
def convert_to_sentencecase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_sentence = text.capitalize()
        text_out_preview = text_in_preview.capitalize()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_sentence)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_sentence
    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Set a prefix to the clipboard text
def prefix_text(text, prefix_entry, preview_out_label):

    text = refresh_clipboard()[0]

    if text:
        # Get the prefix from the entry box
        prefix = prefix_entry.get()

        # Prefix each line of the text
        prefixed_lines = [prefix + line for line in text.splitlines()]

        # Join the lines back together
        text_prefixed = '\n'.join(prefixed_lines)

        # Set the modified text back to the clipboard
        pyperclip.copy(text_prefixed)

         # Split the text by newlines and take the first element
        first_row = text_prefixed.splitlines()[0]

        if len(first_row) > 26:
            text_out_preview = first_row[0:26] + "..."
        else:
            text_out_preview = first_row

        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return prefix_text

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Set a suffix to the clipboard text
def suffix_text(text, suffix_entry, preview_out_label):

    text = refresh_clipboard()[0]

    if text:
        # Get the suffix from the entry box
        suffix = suffix_entry.get()

        # Suffix each line of the text
        suffixed_lines = [line + suffix for line in text.splitlines()]

        # Join the lines back together
        text_suffixed = '\n'.join(suffixed_lines)

        # Set the modified text back to the clipboard
        pyperclip.copy(text_suffixed)

         # Split the text by newlines and take the first element
        first_row = text_suffixed.splitlines()[0]

        if len(first_row) > 26:
            text_out_preview = first_row[0:26] + "..."
        else:
            text_out_preview = first_row

        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return suffix_text

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")



if __name__ == "__main__":
     main()