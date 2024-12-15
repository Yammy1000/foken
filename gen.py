import random
import base64
from faker import Faker

fake = Faker()
warning = "use.token.not.user:"


def random_string(length: int) -> str:
    """Generate a random alphanumeric string."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choices(chars, k=length))


def generate_discord_token():
    """Generate a fake Discord token."""
    header = base64.urlsafe_b64encode(random_string(8).encode()).decode().strip("=")
    payload = base64.urlsafe_b64encode(random_string(24).encode()).decode().strip("=")
    signature = random_string(40)
    return f"{warning}{header}.{payload}.{signature}"


def generate_roblox_cookie():
    """Generate a fake Roblox cookie."""
    cookie = f"{random_string(8)}-{random_string(4)}-{random_string(4)}-{random_string(4)}-{random_string(12)}"
    return f"{warning}{cookie}"


def generate_steam():
    """Generate a fake Steam account."""
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    return f"{username}:{password}:{email}"


def generate_gmail():
    """Generate a fake Gmail account."""
    email = fake.email()
    password = fake.password()
    return f"{email}:{password}"


def generate_netflix():
    """Generate a fake Netflix account."""
    email = fake.email()
    password = fake.password()
    return f"{email}:{password}"


def generate_spotify():
    """Generate a fake Spotify account."""
    username = fake.user_name()
    password = fake.password()
    return f"{username}:{password}"


def generate_instagram():
    """Generate a fake Instagram account."""
    username = fake.user_name()
    password = fake.password()
    return f"{username}:{password}"
