import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)
root.configure(bg='black')

# Function to update time
def update_time():
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %B %d, %Y')
    
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    
    # Update every 1000ms (1 second)
    time_label.after(1000, update_time)

# Create time label
time_label = tk.Label(
    root,
    font=('Arial', 48, 'bold'),
    background='black',
    foreground='cyan'
)
time_label.pack(pady=10)

# Create date label
date_label = tk.Label(
    root,
    font=('Arial', 16),
    background='black',
    foreground='white'
)
date_label.pack()

# Start the clock
update_time()

# Run the application
root.mainloop()