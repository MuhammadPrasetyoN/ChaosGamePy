import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np

def chaos_game(iterasi, gradual):
    # titik ujung segitiga awal
    sudut = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    # titik random awal
    point = np.random.rand(2)

    plt.figure(figsize=(6, 6), facecolor='black')
    plt.title(f'Chaos Game with {iterasi} Iterations', fontsize=14, color='cyan')
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(0, 1)
    plt.ylim(0, np.sqrt(3) / 2)

    # Scatter plot in interactive mode
    plt.ion()
    scatter = plt.scatter([], [], s=0.5, color='cyan')
    legend_text = plt.text(0.05, 0.95, '', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

    nilai_x = [point[0]]
    nilai_y = [point[1]]
    scatter.set_offsets(np.c_[nilai_x, nilai_y])

    # Color gradient setup: start at cyan, end at purple
    start_color = np.array([0, 1, 1])  # Cyan
    end_color = np.array([0.5, 0, 0.5])  # Purple

    for i in range(1, iterasi+1):
        # memilih titik ujung random
        titik = sudut[np.random.choice(len(sudut))]
        # temukan titik tengah antara titik saat ini dan titik yang dipilih
        point = (point + titik) / 2
        nilai_x.append(point[0])
        nilai_y.append(point[1])

        color = start_color * (1 - i / iterasi) + end_color * (i / iterasi)

        if gradual:
            # Update scatter data gradually
            scatter.set_offsets(np.c_[nilai_x, nilai_y])
            # Update legend with current iteration
            legend_text.set_text(f'Iteration: {i}/{iterasi}')
            legend_text.set_color('cyan')
            scatter.set_color([color])
            plt.draw()
            plt.pause(0.001)  # Pause for a short moment to create the animation effect

    # If not gradual, just plot all points at once
    if not gradual:
        scatter.set_offsets(np.c_[nilai_x, nilai_y])
        scatter.set_color([end_color])
        legend_text.set_text(f'Iteration: {iterasi}/{iterasi}')
        legend_text.set_color('cyan')
        plt.draw()

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Function to handle the GUI input
def get_iterations():
    # Create a window for input
    root = tk.Tk()
    root.title("Chaos Game")
    root.configure(bg="black")
    root.geometry("400x250")

    # Frame for iterations input
    iter_frame = tk.Frame(root, bg="black")
    iter_frame.grid(row=0, column=0, pady=(10, 0), padx=10, columnspan=2)
    tk.Label(iter_frame, text="Enter the number of iterations:", font=("Arial", 12), fg="cyan", bg="black").pack(
        side=tk.LEFT)
    iter_entry = tk.Entry(iter_frame, font=("Arial", 10), width=15, justify='center')
    iter_entry.pack(side=tk.LEFT, padx=5)

    # Frame for plotting options
    choice_var = tk.IntVar(value=0)
    options_frame = tk.Frame(root, bg="black")
    options_frame.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
    tk.Label(options_frame, text="Do you want to see the points plotted gradually?", font=("Arial", 10), fg="cyan",
             bg="black").pack(anchor="w")
    tk.Radiobutton(options_frame, text="Gradually", variable=choice_var, value=0, font=("Arial", 10), fg="white",
                   bg="black", selectcolor="black").pack(anchor="w")
    tk.Radiobutton(options_frame, text="Directly", variable=choice_var, value=1, font=("Arial", 10), fg="white",
                   bg="black", selectcolor="black").pack(anchor="w")

    # Function to start the chaos game based on user input
    def start_game():
        try:
            iterasi = int(iter_entry.get())
            if iterasi <= 0:
                raise ValueError("Number of iterations must be positive.")
            gradual = (choice_var.get() == 0)
            mode = "gradually" if gradual else "directly"
            messagebox.showinfo("Chaos Game", f"Starting Chaos Game with {iterasi} iterations, displaying {mode}.")
            root.destroy()  # Close the input window
            chaos_game(iterasi, gradual)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid positive integer for iterations.")

    # Add a button to submit the input
    submit_button = tk.Button(root, text="Start Chaos Game", command=start_game, font=("Arial", 12), bg="cyan",
                              fg="black")
    submit_button.grid(row=4, column=0, columnspan=3, pady=20)

    root.mainloop()

if __name__ == '__main__':
    get_iterations()


