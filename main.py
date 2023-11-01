import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

# Define color constants
LIGHT_BLUE = "#6BCBFF"
DARK_BLUE = "#0A57A4"
FONT_NAME = "Arial"


# Function to extract data using CSS selector
def extract_data_with_css_selector(html_content, css_selector):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    try:
        # Select elements based on the provided CSS selector
        selected_elements = soup.select(css_selector)

        # Extract text from the selected elements
        data = [element.text for element in selected_elements]
        return data

    except Exception as e:
        raise ValueError(f"Data extraction error: {str(e)}")


# Function to extract data from HTML content
def extract_data_from_html(html_content, tag_input, class_input, id_input):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data using the provided tag, class, and ID inputs
    data = [element.text for element in soup.find_all(tag_input, id=id_input, class_=class_input)]
    return data


# Function to get the website name from the URL
def get_website_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


# Function to show or hide Tag, Class, and ID labels and entry widgets
def show_hide_data_extraction_widgets():
    data_extraction_method = data_extraction_method_var.get()
    if data_extraction_method == "CSS Selector":
        # Hide Tag, Class, and ID widgets
        tag_label.grid_remove()
        tag_entry.grid_remove()
        class_label.grid_remove()
        class_entry.grid_remove()
        id_label.grid_remove()
        id_entry.grid_remove()
        css_selector_label.grid()
        css_selector_entry.grid()
    else:
        # Show Tag, Class, and ID widgets
        tag_label.grid()
        tag_entry.grid()
        class_label.grid()
        class_entry.grid()
        id_label.grid()
        id_entry.grid()
        css_selector_label.grid_remove()
        css_selector_entry.grid_remove()


# Function to handle the "Scrape Data" button click
def scrape_data():
    url = url_entry.get()
    data_extraction_method = data_extraction_method_var.get()

    try:
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text

            if data_extraction_method == "CSS Selector":
                css_selector = css_selector_entry.get()
                data = extract_data_with_css_selector(html_content, css_selector)
            else:
                tag_input = tag_entry.get()
                class_input = class_entry.get()
                id_input = id_entry.get()
                data = extract_data_from_html(html_content, tag_input, class_input, id_input)

            website_name = get_website_name(url)
            save_option = save_option_var.get()

            # Get the user-specified file path for saving
            file_path = filedialog.asksaveasfilename(defaultextension=f".{save_option.lower()}",
                                                     initialfile=f"{website_name}_data")

            if file_path:
                save_option = save_option_var.get()

                if save_option == "JSON":
                    # Save data as JSON
                    with open(file_path, "w") as json_file:
                        json_file.write(str(data))
                    messagebox.showinfo("Success", f"Data saved as JSON to {file_path}")

                elif save_option == "CSV":
                    # Save data as CSV
                    df = pd.DataFrame(data, columns=["Data"])
                    df.to_csv(file_path, index=False)
                    messagebox.showinfo("Success", f"Data saved as CSV to {file_path}")

                else:
                    raise ValueError("Invalid save option")
        else:
            messagebox.showerror("Error", f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main application window
app = tk.Tk()
app.title("Web Scraper")
app.configure(bg=LIGHT_BLUE)

# URL entry
url_label = tk.Label(app, text="Enter URL:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
url_label.grid(row=0, column=0, pady=5)
url_entry = tk.Entry(app, width=50, highlightthickness=0)
url_entry.grid(row=0, column=1, columnspan=2)

# Data extraction method selection (Radio buttons)
data_extraction_method_label = tk.Label(app, text="Select data extraction method:", font=(FONT_NAME, 15),
                                        background=LIGHT_BLUE)
data_extraction_method_label.grid(row=1, column=0, pady=5, padx=30)
data_extraction_method_var = tk.StringVar()
data_extraction_html_content = tk.Radiobutton(app, text="HTML Content", variable=data_extraction_method_var,
                                              value="HTML Content", command=show_hide_data_extraction_widgets,
                                              background=LIGHT_BLUE)
data_extraction_html_content.grid(row=1, column=1, pady=5)
data_extraction_css_selector = tk.Radiobutton(app, text="CSS Selector", variable=data_extraction_method_var,
                                              value="CSS Selector", command=show_hide_data_extraction_widgets,
                                              background=LIGHT_BLUE)
data_extraction_css_selector.grid(row=1, column=2, pady=5)
data_extraction_method_var.set("HTML Content")

# CSS Selector entry
css_selector_label = tk.Label(app, text="CSS Selector:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
css_selector_label.grid(row=2, column=0, pady=5)
css_selector_label.grid_remove()
css_selector_entry = tk.Entry(app, width=50, highlightthickness=0)
css_selector_entry.grid(row=2, column=1, columnspan=2, pady=5, padx=30)
css_selector_entry.grid_remove()

# Tag entry
tag_label = tk.Label(app, text="Tag:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
tag_label.grid(row=2, column=0, pady=5)
tag_entry = tk.Entry(app, width=50, highlightthickness=0)
tag_entry.grid(row=2, column=1, columnspan=2, pady=5)

# ID entry
id_label = tk.Label(app, text="ID:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
id_label.grid(row=3, column=0, pady=5)
id_entry = tk.Entry(app, width=50, highlightthickness=0)
id_entry.grid(row=3, column=1, columnspan=2, pady=5)

# Class entry
class_label = tk.Label(app, text="Class:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
class_label.grid(row=4, column=0, pady=5)
class_entry = tk.Entry(app, width=50, highlightthickness=0)
class_entry.grid(row=4, column=1, columnspan=2, pady=5, padx=30)

# Save option selection (Radio buttons)
save_option_label = tk.Label(app, text="Select save option:", font=(FONT_NAME, 15), background=LIGHT_BLUE)
save_option_label.grid(row=5, column=0, pady=5)
save_option_var = tk.StringVar()
save_option_json = tk.Radiobutton(app, text="JSON", variable=save_option_var, value="JSON", background=LIGHT_BLUE)
save_option_json.grid(row=5, column=1, pady=5)
save_option_csv = tk.Radiobutton(app, text="CSV", variable=save_option_var, value="CSV", background=LIGHT_BLUE)
save_option_csv.grid(row=5, column=2, pady=5)
save_option_var.set("JSON")

# Scrape button
scrape_button = tk.Button(app, text="Scrape Data", command=scrape_data, background=LIGHT_BLUE,
                          highlightbackground=LIGHT_BLUE)
scrape_button.grid(row=6, column=1, pady=5)

app.mainloop()
