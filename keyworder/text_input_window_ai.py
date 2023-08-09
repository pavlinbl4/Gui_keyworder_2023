import tkinter as tk


class InputWindow:
    def __init__(self):
        self.result = []



    def create_window(self):
        window = tk.Tk()

        # Set the height of the window to 100 pixels
        window_width = 570
        window_height = 240
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int(screen_width / 4)
        y = int(screen_height / 2 - window_height / 2)
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Disable the ability to resize the window
        window.resizable(False, False)

        # Set the title of the window
        window.title("Input Window")

        # Set the input label
        tk.Label(window, text="Enter your information:").grid(row=0, column=0)

        # Set the input text field
        input_field = tk.Text(window, height=8, wrap="word")
        input_field.grid(row=1, column=0, sticky="WE")

        def confirm_input(self):
            self.result.append(input_field.get("1.0", 'end-1c'))
            self.window.destroy()

        def cancel_input(self):
            self.window.destroy()

        # Set the button to submit the information
        submit_button = tk.Button(window, text="Submit", command=confirm_input)
        submit_button.grid(row=2, column=0, pady=5)

        # Set the button to cancel the input
        cancel_button = tk.Button(window, text="Cancel", command=cancel_input)
        cancel_button.grid(row=3, column=0)

        input_var = tk.StringVar()
        input_field = tk.Entry(window, textvariable=input_var)

        # Run the window
        window.mainloop()







if __name__ == '__main__':
    window = InputWindow()
    print(window.create_window())