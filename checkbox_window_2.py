import tkinter as tk


def create_gui(words):
    root = tk.Tk()

    keywords = []

    max_col = 5

    for i, word in enumerate(words):
        var = tk.IntVar()
        keywords.append(var)
        row = i // max_col
        col = i % max_col

        cb = tk.Checkbutton(root, text=word, variable=keywords[i])
        cb.grid(row=row, column=col, sticky="w", padx=20, pady=15)

    def invert():
        for word in keywords:
            word.set(not word.get())

    invert_cb = tk.Checkbutton(root, text="Invert", command=invert)
    invert_cb.grid(columnspan=max_col, pady=30)

    submit_button = tk.Button(root, text="Submit", )
    submit_button.grid(row=i + 3, column=0, columnspan=len(words), pady=10)

    root.mainloop()


example_words = ["cat", "dog", "bird", "fish", "cow", "horse", "pig", "sheep", "goat",
                 "cat", "dog", "bird", "big-sword-fish", "cow", "horse", "pig-vey-clever-animal", "sheep", "goat"]

if __name__ == "__main__":
    create_gui(example_words)
