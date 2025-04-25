import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load CSV and display stats
def load_file():
    # Ask user to upload a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if not file_path:
        return
    
    # Load CSV into pandas dataframe
    global df
    df = pd.read_csv(file_path)
    
    # Calculate necessary statistics
    df['Total'] = df['Quantity'] * df['Price']
    total_sales = df['Total'].sum()
    total_items = df['Quantity'].sum()
    top_product = df.groupby('Product')['Total'].sum().idxmax()

    # Update labels with stats
    total_sales_label.config(text=f"Total Sales: ₹{total_sales}")
    total_items_label.config(text=f"Total Items Sold: {total_items}")
    top_product_label.config(text=f"Top Product: {top_product}")

    # Generate and display charts
    show_charts()

# Function to generate and show charts
def show_charts():
    # Group data by product for plotting
    sales_by_product = df.groupby('Product')['Total'].sum()

    # Create the bar chart
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Bar chart
    sales_by_product.plot(kind='bar', ax=ax[0], color='skyblue')
    ax[0].set_title('Total Sales by Product')
    ax[0].set_xlabel('Product')
    ax[0].set_ylabel('Sales (₹)')

    # Pie chart
    sales_by_product.plot(kind='pie', ax=ax[1], autopct='%1.1f%%', startangle=140)
    ax[1].set_title('Sales Distribution by Product')
    ax[1].set_ylabel('')

    # Embed the charts into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Create the main Tkinter window
window = tk.Tk()
window.title("Sales Dashboard")

# Create and pack the widgets
upload_button = tk.Button(window, text="Upload CSV File", command=load_file)
upload_button.pack(pady=10)

total_sales_label = tk.Label(window, text="Total Sales: ₹0")
total_sales_label.pack(pady=5)

total_items_label = tk.Label(window, text="Total Items Sold: 0")
total_items_label.pack(pady=5)

top_product_label = tk.Label(window, text="Top Product: None")
top_product_label.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
