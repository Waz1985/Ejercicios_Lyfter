from datetime import date
import FreeSimpleGUI as sg



def create_movement_window(categories, movement_type):
    today = date.today().isoformat() 

    layout = [
        [sg.Text(f"Add {movement_type}")],
        [sg.Text("Date (YYYY-MM-DD)"), sg.Input(default_text=today, key="-DATE-", size=(12, 1)), 
            sg.CalendarButton("📅", target="-DATE-", format="%Y-%m-%d", close_when_date_chosen=True, no_titlebar=False)],
        [sg.Text("Title"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    return sg.Window(
        f"Add {movement_type}",
        layout,
        modal=True,
        finalize=True
    )

