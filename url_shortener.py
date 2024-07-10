from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyshorteners
import webbrowser
import validators

# Function to shorten URL
def shorten_url(url):
    if not validators.url(url):
        output_url.set("Invalid URL")
        messagebox.showerror("Error", "The URL you entered is invalid.")
        url_entry.delete(0,END)
        output_url.set("")
        return
    
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        output_url.set(short_url)
    except Exception as e:
        output_url.set("Error: " + str(e))
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to copy the shortened URL to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_url.get())
    root.update()

# Function to open the shortened URL
def open_url():
    url_to_open = output_url.get()
    if validators.url(url_to_open):
        webbrowser.open(url_to_open)
    else:
        messagebox.showerror("Error", "The URL you are trying to open is invalid.")
        output_url.set("Invalid URL")

# Main Window
root = Tk()
root.title("URL Shortener")
root.geometry("550x250")

# Label
label = ttk.Label(root, text="URL Shortener", font=("Poppins", 25))
label.grid(row=0, padx=(85, 0))

# Label for URL Input
url_input = ttk.Label(root, text="Enter URL: ")
url_input.grid(row=1, column=0, pady=10)

# Input field for URL
url = StringVar()
url_entry = ttk.Entry(root, textvariable=url, width=30)
url_entry.grid(row=1, column=1, pady=10)

# Button for Short URL
shorten_button = ttk.Button(root, text="Shorten", command=lambda: shorten_url(url.get()))
shorten_button.grid(row=2, column=0, pady=10)

# Label for Shortened URL
shortened_url_label = ttk.Label(root, text="Shortened URL: ")
shortened_url_label.grid(row=4, column=0, pady=10)

# Output field for shortened URL
output_url = StringVar()
output_url_entry = ttk.Entry(root, textvariable=output_url, width=30)
output_url_entry.grid(row=4, column=1, pady=10)

# Button for Copy URL
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, pady=10)

# Button to Open URL
open_button = ttk.Button(root, text="OPEN", command=open_url)
open_button.grid(row=5, column=1, pady=10)

root.mainloop()


