import pandas as pd
from tkinter import filedialog, messagebox
from datetime import datetime

from database.db import (
    add_birthday,
    add_wedding,
    get_birthdays,
    get_weddings
)
def format_date(date_value):
    if pd.isna(date_value):
        return ""

    if isinstance(date_value, pd.Timestamp):
        return date_value.strftime("%d/%m/%Y")

    text = str(date_value).strip()

    for fmt in (
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S"
    ):
        try:
            return datetime.strptime(text, fmt).strftime("%d/%m/%Y")
        except:
            pass

    raise ValueError(f"Invalid date format: {text}")


def export_to_excel():

    birthdays = get_birthdays()
    weddings = get_weddings()

    file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[
            ("Excel File", "*.xlsx")
        ]
    )

    if not file:
        return

    birthday_data = []

    for _, name, birthday in birthdays:
        birthday_data.append({
            "Name": name,
            "Birthday": birthday
        })

    wedding_data = []

    for _, husband, wife, anniversary in weddings:
        wedding_data.append({
            "Husband": husband,
            "Wife": wife,
            "Anniversary": anniversary
        })

    with pd.ExcelWriter(file) as writer:

        pd.DataFrame(
            birthday_data
        ).to_excel(
            writer,
            sheet_name="Birthdays",
            index=False
        )

        pd.DataFrame(
            wedding_data
        ).to_excel(
            writer,
            sheet_name="Weddings",
            index=False
        )

    messagebox.showinfo(
        "Success",
        "Excel exported successfully."
    )


def import_from_excel():

    file = filedialog.askopenfilename(
        filetypes=[
            ("Excel File", "*.xlsx")
        ]
    )

    if not file:
        return

    errors = []

    imported_birthdays = 0
    imported_weddings = 0

    try:

        excel = pd.ExcelFile(file)

        # Birthdays
        if "Birthdays" in excel.sheet_names:

            df = pd.read_excel(
                file,
                sheet_name="Birthdays"
            )

            required = ["Name", "Birthday"]

            if not all(col in df.columns for col in required):
                errors.append(
                    "Birthdays sheet: Missing columns."
                )

            else:

                for index, row in df.iterrows():

                    row_number = index + 2

                    try:

                        name = str(
                            row["Name"]
                        ).strip()

                        name = str(
                            row["Name"]
                        ).strip()

                        birthday = format_date(
                            row["Birthday"]
                        )

                        if name == "" or name == "nan":
                            raise ValueError(
                                "Name is empty."
                            )

                        if name == "" or name == "nan":
                            raise ValueError(
                                "Name is empty."
                            )

                        if birthday == "" or birthday == "nan":
                            raise ValueError(
                                "Birthday is empty."
                            )

                        datetime.strptime(
                            birthday,
                            "%d/%m/%Y"
                        )
                        exists = False

                        for _, n, b in get_birthdays():
                            if (
                                n.lower() == name.lower()
                                and b == birthday
                            ):
                                exists = True
                                break

                        if exists:
                            raise ValueError(
                                "Birthday already exists."
                            )

                        add_birthday(
                            name,
                            birthday
                        )

                        imported_birthdays += 1

                    except Exception as e:
                        errors.append(
                            f"Birthdays - Row {row_number}: {e}"
                        )

        # Weddings
        if "Weddings" in excel.sheet_names:

            df = pd.read_excel(
                file,
                sheet_name="Weddings"
            )

            required = [
                "Husband",
                "Wife",
                "Anniversary"
            ]

            if not all(col in df.columns for col in required):
                errors.append(
                    "Weddings sheet: Missing columns."
                )

            else:

                for index, row in df.iterrows():

                    row_number = index + 2

                    try:

                        husband = str(
                            row["Husband"]
                        ).strip()

                        wife = str(
                            row["Wife"]
                        ).strip()

                        anniversary = format_date(
                            row["Anniversary"]
                        )

                        if husband == "" or husband == "nan":
                            raise ValueError(
                                "Husband name is empty."
                            )

                        if wife == "" or wife == "nan":
                            raise ValueError(
                                "Wife name is empty."
                            )

                        if anniversary == "" or anniversary == "nan":
                            raise ValueError(
                                "Anniversary is empty."
                            )

                        datetime.strptime(
                            anniversary,
                            "%d/%m/%Y"
                        )
                        exists = False

                        for _, h, w, a in get_weddings():
                            if (
                                h.lower() == husband.lower()
                                and w.lower() == wife.lower()
                                and a == anniversary
                            ):
                                exists = True
                                break

                        if exists:
                            raise ValueError(
                                "Wedding already exists."
                            )

                        add_wedding(
                            husband,
                            wife,
                            anniversary
                        )

                        imported_weddings += 1

                    except Exception as e:
                        errors.append(
                            f"Weddings - Row {row_number}: {e}"
                        )

        message = (
            f"Imported Successfully\n\n"
            f"✓ Birthdays: {imported_birthdays}\n"
            f"✓ Weddings: {imported_weddings}"
        )

        if errors:
            message += (
                "\n\nSkipped Rows:\n\n"
                + "\n".join(errors)
            )

        messagebox.showinfo(
            "Import Result",
            message
        )

    except Exception as e:

        messagebox.showerror(
            "Import Error",
            str(e)
        )


def download_template():

    file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        initialfile="church_template.xlsx",
        filetypes=[
            ("Excel File", "*.xlsx")
        ]
    )

    if not file:
        return

    birthdays = pd.DataFrame(
        {
            "Name": ["John Wesley"],
            "Birthday": ["15/07/2000"]
        }
    )

    weddings = pd.DataFrame(
        {
            "Husband": ["David"],
            "Wife": ["Sarah"],
            "Anniversary": ["10/06/2015"]
        }
    )

    with pd.ExcelWriter(file) as writer:

        birthdays.to_excel(
            writer,
            sheet_name="Birthdays",
            index=False
        )

        weddings.to_excel(
            writer,
            sheet_name="Weddings",
            index=False
        )

    messagebox.showinfo(
        "Success",
        "Template downloaded successfully."
    )