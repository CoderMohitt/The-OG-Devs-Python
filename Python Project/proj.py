import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not file_path:
        return
    
    global df
    df = pd.read_csv(file_path)

    df['Total'] = df['Quantity'] * df['Price']

    total_sales = df['Total'].sum()
    total_items = df['Quantity'].sum()
    top_product = df.groupby("Product")['Total'].sum().idxmax()

    total_sales_label.config(text=f"Total Sales : Rs{total_sales}")
    total_items_label.config(text=f"Total Items Sold : {total_items}")
    top_product_label.config(text=f"Top product : Rs{top_product}")

    show_charts()

def show_charts():
    sales_by_product = df.groupby('Product')['Total'].sum()

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    sales_by_product.plot(kind='bar', ax=[0], color='skyblue')

    ax[0].set_title('Total Sales by Product')

    ax[0].set_xlabel('Product')
    ax[0].set_ylabel('Sales ')

    sales_by_product.plot(kind='pie', ax=ax[1], autopct='%1.1f%%', startangle=140)

    ax[1].set_title('Sales Distribution by Product')
    ax[1].set_ylabel('')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

window = tk.Tk()
window.title('Sales Dashboard')

upload_button = tk.Button(window, text='Upload CSV File', command=load_file)
upload_button.pack(pady=10)

total_sales_label = tk.Label(window, text='Total Sales: Rs0')
total_sales_label.pack(pady=5)

total_items_label = tk.Label(window, text='Total Items Sold: 0')
total_items_label.pack(pady=5)

top_product_label = tk.Label(window, text='Top Product: None')
top_product_label.pack(pady=5)

window.mainloop()