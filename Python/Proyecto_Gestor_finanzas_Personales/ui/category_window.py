import FreeSimpleGUI as sg

def create_category_window():
    layout = [
        [sg.Text("Category name")],
        [sg.Input(key="-CATEGORY-")],
        [sg.Text("Color")],
        [sg.ColorChooserButton("Choose color", target="-COLOR-INPUT-")],
        [sg.Input(key="-COLOR-INPUT-", visible=False)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    return sg.Window(
        "Add Category",
        layout,
        modal=True,
        finalize=True
    )
