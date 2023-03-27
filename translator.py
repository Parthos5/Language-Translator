from tkinter import *
from googletrans import Translator

# Create a function to translate the input text
def translate_text():
    # Get the text from the input box
    input_text = input_box.get("1.0", END).strip()

    # Create a translator object
    translator = Translator()

    # Get the selected language from the dropdown menu
    selected_language = language_dropdown.get()

    # Translate the text to the selected language
    translated_text = translator.translate(input_text, dest=selected_language).text

    # Insert the translated text into the output box
    output_box.delete("1.0", END)
    output_box.insert(END, translated_text)

# Create a GUI window
window = Tk()

# Add a label for the input box
input_label = Label(window, text="Enter text to translate:")
input_label.pack()

# Add an input box
input_box = Text(window, height=5)
input_box.pack()

# Add a label for the language dropdown menu
language_label = Label(window, text="Select language to translate to:")
language_label.pack()

# Add a dropdown menu for selecting the language
# language_options = ["en", "es", "fr", "de", "it", "ja", "ko", "pt", "ru", "zh-cn"]
language_options = ["en", "es", "fr", "hi", "mr", "pt", "ta", "tl", "pa", "kn", "ml"]
language_names = ["English", "Spanish", "French", "Hindi", "Marathi", "Portuguese", "Tamil", "Tulu", "Punjabi", "Kannada", "Malayalam"]
language_dropdown = StringVar(window)
language_dropdown.set("en")
language_menu = OptionMenu(window, language_dropdown, *language_names)
language_menu.pack()

# Add a button to translate the text
translate_button = Button(window, text="Translate", command=translate_text)
translate_button.pack()

# Add a label for the output box
output_label = Label(window, text="Translated text:")
output_label.pack()

# Add an output box for displaying the translated text
output_box = Text(window, height=5)
output_box.pack()

# Start the GUI event loop
window.mainloop()