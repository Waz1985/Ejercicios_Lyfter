from core.manager import Manager
from core.models import Category
from core.persistence import load_categories, load_movements, save_categories
from ui.category_window import create_category_window
from ui.main_window import create_main_window, build_table_data, build_totals, build_row_colors
from ui.movement_window import create_movement_window
from core.persistence import save_movements, export_report
from ui.events import event_add_expense, event_add_income, event_add_category, event_filter_button, event_clear_filter, event_export_report 
import FreeSimpleGUI as sg


CATEGORIES_PATH = "data/categories.csv"
MOVEMENTS_PATH = "data/movements.csv"

def main():
    
    manager = Manager()
    manager.categories = load_categories(CATEGORIES_PATH)
    manager.movements = load_movements(MOVEMENTS_PATH)
    total_incomes, total_expenses, balance = build_totals(manager)

    table_data = build_table_data(manager.movements)

    window = create_main_window(table_data)

    window["-TABLE-"].update(
    values=build_table_data(manager.movements),
    row_colors=build_row_colors(manager.movements, manager.categories)
    )

    window["-TOTAL-INCOME-"].update(f"{total_incomes}")
    window["-TOTAL-EXPENSES-"].update(f"{total_expenses}")
    window["-BALANCE-"].update(f"{balance}")


    while True:
        event, values = window.read()

        if event in (None, "Exit"):
            break
        
        #Add EXPENSE event        
        if event == "Add Expense":
            if not manager.has_categories():
                sg.popup_error("You must add at least one category first")
                continue

            event_add_expense(manager, create_movement_window, save_movements, 
                            MOVEMENTS_PATH, window, build_table_data, build_row_colors)

            total_incomes, total_expenses, balance = build_totals(manager)

            window["-TOTAL-INCOME-"].update(total_incomes)
            window["-TOTAL-EXPENSES-"].update(total_expenses)
            window["-BALANCE-"].update(balance)


        #Add INCOME event
        if event == "Add Income":
            if not manager.has_categories():
                sg.popup_error("You must add at least one category first")
                continue

            event_add_income(manager, create_movement_window, save_movements, 
                            MOVEMENTS_PATH, window, build_table_data, build_row_colors)
            
            total_incomes, total_expenses, balance = build_totals(manager)

            window["-TOTAL-INCOME-"].update(total_incomes)
            window["-TOTAL-EXPENSES-"].update(total_expenses)
            window["-BALANCE-"].update(balance)

        #Event add Category
        if event == "Add Category":
            cat_window = create_category_window()

            event_add_category(manager, cat_window, Category, save_categories, CATEGORIES_PATH)

        if event == "Filter":
            event_filter_button(manager, values, window, build_table_data, build_row_colors)
        
        if event == 'Clear':
            event_clear_filter(manager, window, build_table_data, build_row_colors)
        
        if event == "Export to CSV":
            event_export_report(manager, export_report)

    window.close()


if __name__ == "__main__":
    main()
