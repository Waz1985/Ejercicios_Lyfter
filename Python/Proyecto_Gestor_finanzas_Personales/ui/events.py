import FreeSimpleGUI as sg

def event_add_expense(manager, create_movement_window, save_movements, MOVEMENTS_PATH, window, 
                    build_table_data, build_row_colors):
    category_names = [c.name for c in manager.categories]
    mov_window = create_movement_window(category_names, "EXPENSE")

    while True:
        mov_event, mov_values = mov_window.read()

        if mov_event in (None, "Cancel"):
            break

        if mov_event == "Save":
            try:
                manager.add_movement(
                    mov_values["-DATE-"],
                    mov_values["-TITLE-"],
                    mov_values["-AMOUNT-"],
                    mov_values["-CATEGORY-"],
                    "EXPENSE"
                )

                save_movements(MOVEMENTS_PATH, manager.movements)

                # 🔄 refrescar tabla
                window["-TABLE-"].update(
                    values = build_table_data(manager.movements),
                    row_colors = build_row_colors(manager.movements, manager.categories)
                )

                break

            except (ValueError, TypeError) as e:
                sg.popup_error(str(e))

    mov_window.close()

def event_add_income(manager, create_movement_window, save_movements, MOVEMENTS_PATH, window, 
                    build_table_data, build_row_colors):
    category_names = [c.name for c in manager.categories]
    mov_window = create_movement_window(category_names, "INCOME")

    while True:
        mov_event, mov_values = mov_window.read()

        if mov_event in (None, "Cancel"):
            break

        if mov_event == "Save":
            try:
                manager.add_movement(
                    mov_values["-DATE-"],
                    mov_values["-TITLE-"],
                    mov_values["-AMOUNT-"],
                    mov_values["-CATEGORY-"],
                    "INCOME"
                )

                save_movements(MOVEMENTS_PATH, manager.movements)

                window["-TABLE-"].update(
                    values=build_table_data(manager.movements),
                    row_colors=build_row_colors(manager.movements, manager.categories)
                )

                break

            except (ValueError, TypeError) as e:
                sg.popup_error(str(e))

    mov_window.close()

def event_add_category(manager, cat_window, Category, save_categories, CATEGORIES_PATH):
    while True:
        cat_event, cat_values = cat_window.read()

        if cat_event in (None, "Cancel"):
            break

        if cat_event == "Save":
            try:
                name = cat_values["-CATEGORY-"]
                color = cat_values.get("-COLOR-INPUT-") or "#DDDDDD"

                category = Category(name, color)
                manager.add_category(category)

                save_categories(CATEGORIES_PATH, manager.categories)

                break

            except ValueError as e:
                sg.popup_error(str(e))

    cat_window.close()

def event_filter_button(manager, values, window, build_table_data, build_row_colors):
        try:
            start = values["-START-DATE-"]
            end = values["-END-DATE-"]

            filtered = manager.get_movements_between(start, end)

            window["-TABLE-"].update(
                values=build_table_data(filtered),
                row_colors=build_row_colors(manager.movements, manager.categories)
            )

        except ValueError as e:
            sg.popup_error(str(e))

def event_clear_filter(manager, window, build_table_data, build_row_colors):
        window["-TABLE-"].update(
        values=build_table_data(manager.movements),
        row_colors=build_row_colors(manager.movements, manager.categories)
    )
        
def event_export_report(manager, export_report):
    file_path = sg.popup_get_file(
        "Save report",
        save_as=True,
        file_types=(("CSV Files", "*.csv"),),
        default_extension=".csv"
    )

    if file_path:
        try:
            export_report(file_path, manager.movements, manager)
            sg.popup("Report exported successfully")
        except Exception as e:
            sg.popup_error(f"Error exporting file: {e}")
