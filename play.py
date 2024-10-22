import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np

def chaos_game(iterasi, gradual):
    # titik ujung segitiga awal
    sudut = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    # titik random awal
    point = np.random.rand(2)

    plt.figure(figsize=(6, 6))
    plt.title(f'Chaos Game with {iterasi} Iterations')
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, np.sqrt(3) / 2)

    # Scatter plot in interactive mode
    plt.ion()
    scatter = plt.scatter([], [], s=0.5, color='black')
    legend_text = plt.text(0.05, 0.95, '', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

    nilai_x = [point[0]]
    nilai_y = [point[1]]
    scatter.set_offsets(np.c_[nilai_x, nilai_y])

    for i in range(1, iterasi+1):
        # memilih titik ujung random
        titik = sudut[np.random.choice(len(sudut))]
        # temukan titik tengah antara titik saat ini dan titik yang dipilih
        point = (point + titik) / 2
        nilai_x.append(point[0])
        nilai_y.append(point[1])

        if gradual:
            # Update scatter data gradually
            scatter.set_offsets(np.c_[nilai_x, nilai_y])
            # Update legend with current iteration
            legend_text.set_text(f'Iteration: {i}/{iterasi}')
            plt.draw()
            plt.pause(0.001)  # Pause for a short moment to create the animation effect

    # If not gradual, just plot all points at once
    if not gradual:
        scatter.set_offsets(np.c_[nilai_x, nilai_y])
        legend_text.set_text(f'Iteration: {iterasi}/{iterasi}')
        plt.draw()

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Function to handle the GUI input
# Function to handle the GUI input
def get_iterations():
    # Create a window for input
    root = tk.Tk()
    root.title("Chaos Game")

    tk.Label(root, text="Enter the number of iterations:").grid(row=0, column=0, padx=10, pady=10)
    iter_entry = tk.Entry(root)
    iter_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create a variable to store the choice (0 for gradual, 1 for direct)
    choice_var = tk.IntVar(value=0)
    tk.Radiobutton(root, text="Gradually", variable=choice_var, value=0).grid(row=1, column=0, padx=10, pady=5)
    tk.Radiobutton(root, text="Directly", variable=choice_var, value=1).grid(row=1, column=1, padx=10, pady=5)

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
    submit_button = tk.Button(root, text="Start", command=start_game)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == '__main__':
    get_iterations()


