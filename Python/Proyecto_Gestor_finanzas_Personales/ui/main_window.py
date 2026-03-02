import FreeSimpleGUI as sg

def build_table_data(movements):

    table_data = []

    for m in movements:
        table_data.append([
            m.date,
            m.title,
            m.amount,
            m.category,
            m.type
        ])

    return table_data


def build_totals(manager):
    return (
        f"Total Incomes: {manager.total_incomes()}",
        f"Total Expenses: {manager.total_expenses()}",
        f"Balance: {manager.balance()}"
    )

def create_main_window(table_data):
    sg.theme("DefaultNoMoreNagging")


    headings = ["Date", "Title", "Amount", "Category", "Type"]

    layout = [
        [
            sg.Text("Start-Date (YYYY-MM-DD)"), sg.Input(key="-START-DATE-", size=(12, 1)), 
                sg.CalendarButton("📅", target="-START-DATE-", format="%Y-%m-%d", close_when_date_chosen=True, no_titlebar=False),
            sg.Text("End-Date (YYYY-MM-DD)"), sg.Input(key="-END-DATE-", size=(12, 1)), 
                sg.CalendarButton("📅", target="-END-DATE-", format="%Y-%m-%d", close_when_date_chosen=True, no_titlebar=False),
        ],
        [
            sg.Button("Filter"),
            sg.Button("Clear"),

        ],
        [
            sg.Table(
                values=table_data,
                headings=headings,
                num_rows=10,
                col_widths=[12, 12, 10, 16, 16],
                justification="center",
                key="-TABLE-",
                enable_events=True,
                expand_x=True,
                expand_y=True,
                auto_size_columns=False
            )
        ],
        [
            sg.Text("", key="-TOTAL-INCOME-"),
            sg.Text("", key="-TOTAL-EXPENSES-"),
            sg.Text("", key="-BALANCE-")
        ],
        [
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income"),
            sg.Button("Export to CSV"),
            sg.Button("Exit")
        ]
    ]

    return sg.Window(
        "Personal Finance Manager",
        layout,
        finalize=True
    )

def build_row_colors(movements, categories):
    colors = []
    category_map = {c.name: c.color for c in categories}

    for index, m in enumerate(movements):
        color = category_map.get(m.category)
        if color:
            colors.append((index, color))

    return colors
