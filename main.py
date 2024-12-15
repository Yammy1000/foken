import tkinter as tk
from ui import login_screen, show_main_ui
from gen import (
    generate_discord_token,
    generate_roblox_cookie,
    generate_steam,
    generate_gmail,
    generate_netflix,
    generate_spotify,
    generate_instagram,
)
from webhook import send_to_discord_webhook


def log_to_widget(widget, message):
    """Insert a log message into the widget."""
    widget.insert(tk.END, message + "\n")
    widget.see(tk.END)


def start_generation(token_count, batch_size, botnet_count, token_type, preview_widget, log_widget):
    """Handle token generation and webhook sending."""
    log_to_widget(log_widget, "Starting token generation...")

    # Map token type to generator functions
    generators = {
        "Discord Token": generate_discord_token,
        "Roblox Cookie": generate_roblox_cookie,
        "Steam": generate_steam,
        "Gmail": generate_gmail,
        "Netflix": generate_netflix,
        "Spotify": generate_spotify,
        "Instagram": generate_instagram,
    }

    if token_type not in generators:
        log_to_widget(log_widget, "Invalid token type selected!")
        return

    generator = generators[token_type]

    tokens = [generator() for _ in range(int(token_count))]
    preview_widget.delete("1.0", tk.END)
    preview_widget.insert("1.0", "\n".join(tokens[:10]))

    # Save tokens and send to Discord webhook
    with open("generated_tokens.txt", "w") as file:
        file.write("\n".join(tokens))

    send_to_discord_webhook("generated_tokens.txt", f"{token_type} Generation Complete", lambda msg: log_to_widget(log_widget, msg))

    # Clear tokens after sending
    tokens.clear()
    preview_widget.delete("1.0", tk.END)
    log_to_widget(log_widget, f"{token_type} generation and upload completed.")


if __name__ == "__main__":
    login_screen(lambda: show_main_ui(start_generation))
