import tkinter as tk
from tkinter import ttk, messagebox

LOGIN_CREDENTIALS = {"username": "Surge410", "password": "Elitify"}


def show_main_ui(start_generation_callback):
    """Main token generator UI."""
    root = tk.Tk()
    root.title("FOKEN")

    bg_color = "#1e1e1e"
    fg_color = "#d4d4d4"
    highlight_color = "#007acc"

    root.configure(bg=bg_color)

    title_label = tk.Label(root, text="FOKEN", font=("Courier", 20), bg=bg_color, fg=highlight_color)
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(root, text="Number of Tokens to Generate:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=5)
    entry_token_count = tk.Entry(root, bg="#252526", fg=fg_color)
    entry_token_count.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Batch Size:", bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=5)
    entry_batch_size = tk.Entry(root, bg="#252526", fg=fg_color)
    entry_batch_size.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Number of Botnets (max 214):", bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=10, pady=5)
    entry_botnet_count = tk.Entry(root, bg="#252526", fg=fg_color)
    entry_botnet_count.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Select Format:", bg=bg_color, fg=fg_color).grid(row=4, column=0, padx=10, pady=5)
    format_choice = ttk.Combobox(
        root,
        values=["Discord Token", "Roblox Cookie", "Steam", "Gmail", "Netflix", "Spotify", "Instagram"],
    )
    format_choice.grid(row=4, column=1, padx=10, pady=5)
    format_choice.set("Discord Token")

    tk.Label(root, text="Token Preview:", bg=bg_color, fg=fg_color).grid(row=5, column=0, columnspan=2)
    preview_console = tk.Text(root, height=5, width=50, bg="#252526", fg=fg_color)
    preview_console.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(root, text="Progress Logs:", bg=bg_color, fg=fg_color).grid(row=7, column=0, columnspan=2)
    log_console = tk.Text(root, height=10, width=50, bg="#252526", fg=fg_color)
    log_console.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    generate_button = tk.Button(
        root,
        text="Generate Tokens",
        command=lambda: start_generation_callback(
            entry_token_count.get(),
            entry_batch_size.get(),
            entry_botnet_count.get(),
            format_choice.get(),
            preview_console,
            log_console,
        ),
        bg=highlight_color,
        fg=fg_color,
    )
    generate_button.grid(row=9, column=0, columnspan=2, pady=10)

    root.mainloop()


def login_screen(main_ui_callback):
    """Login screen for authentication."""
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(
        login_window,
        text="Login",
        command=lambda: validate_login(
            username_entry.get(), password_entry.get(), login_window, main_ui_callback
        ),
    )
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    login_window.mainloop()


def validate_login(username, password, login_window, main_ui_callback):
    """Validate the username and password."""
    if username == LOGIN_CREDENTIALS["username"] and password == LOGIN_CREDENTIALS["password"]:
        messagebox.showinfo("Login Successful", "Welcome!")
        login_window.destroy()
        main_ui_callback()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
