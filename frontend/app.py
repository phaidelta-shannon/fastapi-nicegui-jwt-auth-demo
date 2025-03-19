from nicegui import ui
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

def login():
    username = username_input.value
    password = password_input.value

    try:
        response = requests.post(
            f"{BACKEND_URL}/token",
            data={"username": username, "password": password},
        )
        print("Response from backend:", response.status_code, response.json())  # Debug statement
    except Exception as e:
        print("Error connecting to backend:", e)  # Debug statement
        ui.notify("Failed to connect to the backend.", color="red")
        return

    if response.status_code == 200:
        token = response.json()["access_token"]
        ui.notify("Login successful!")
        fetch_user_data(token)
    else:
        ui.notify("Login failed. Check your credentials.", color="red")

def fetch_user_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BACKEND_URL}/users/me/", headers=headers)
        print("Response from backend:", response.status_code, response.json())  # Debug statement
    except Exception as e:
        print("Error connecting to backend:", e)  # Debug statement
        ui.notify("Failed to fetch user data.", color="red")
        return

    if response.status_code == 200:
        user_data = response.json()
        user_label.text = f"Logged in as: {user_data['username']}"
    else:
        ui.notify("Failed to fetch user data.", color="red")

ui.label("Login").classes("text-h4")
username_input = ui.input("Username")
password_input = ui.input("Password", password=True)
ui.button("Login", on_click=login)
user_label = ui.label("").classes("text-h6")

ui.run(port=8080)