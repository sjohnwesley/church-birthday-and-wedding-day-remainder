import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from database.db import (
    add_birthday,
    get_birthdays,
    update_birthday,
    delete_birthday
)


# ============================================================
# DARK SOOTHING COLOR PALETTE
# ============================================================

BG_COLOR = "#101820"
CARD_COLOR = "#182630"
EVENT_CARD_COLOR = "#202F38"
EVENT_HOVER = "#263943"

PRIMARY_COLOR = "#7FB3B0"
PRIMARY_HOVER = "#689996"
PRIMARY_BG = "#203A3B"

BIRTHDAY_COLOR = "#E3A092"
BIRTHDAY_BG = "#3A2B2A"

TEXT_COLOR = "#F2F5F4"
MUTED_TEXT = "#A8B7BC"
SUBTLE_TEXT = "#84969D"

BORDER_COLOR = "#30414A"


class BirthdaysPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BG_COLOR
        )

        self.editing_id = None

        self.months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        self.build_ui()
        self.load_birthdays()

    # ========================================================
    # BUILD UI
    # ========================================================

    def build_ui(self):

        # ====================================================
        # MAIN SCROLLABLE AREA
        # ====================================================

        self.container = ctk.CTkScrollableFrame(
            self,
            fg_color=BG_COLOR,
            scrollbar_button_color="#344850",
            scrollbar_button_hover_color="#49616B"
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ====================================================
        # HEADER
        # ====================================================

        header = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            pady=(0, 20)
        )

        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_frame,
            text="🎂  Birthdays",
            font=("Arial", 28, "bold"),
            text_color=TEXT_COLOR,
            anchor="w"
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_frame,
            text="Manage member birthdays",
            font=("Arial", 13),
            text_color=MUTED_TEXT,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(4, 0)
        )

        # ====================================================
        # COUNT BADGE
        # ====================================================

        self.count_label = ctk.CTkLabel(
            header,
            text="0 birthdays",
            font=("Arial", 13, "bold"),
            text_color=BIRTHDAY_COLOR,
            fg_color=BIRTHDAY_BG,
            corner_radius=10
        )

        self.count_label.pack(
            side="right",
            padx=5,
            pady=5
        )

        # ====================================================
        # ADD / EDIT FORM
        # ====================================================

        self.form_card = ctk.CTkFrame(
            self.container,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        self.form_card.pack(
            fill="x",
            pady=(0, 20)
        )

        # Form title
        self.form_title = ctk.CTkLabel(
            self.form_card,
            text="Add Birthday",
            font=("Arial", 18, "bold"),
            text_color=TEXT_COLOR
        )

        self.form_title.pack(
            anchor="w",
            padx=22,
            pady=(18, 15)
        )

        # ----------------------------------------------------
        # NAME
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.form_card,
            text="Member Name",
            font=("Arial", 12, "bold"),
            text_color=MUTED_TEXT
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 6)
        )

        self.name_entry = ctk.CTkEntry(
            self.form_card,
            height=42,
            corner_radius=10,
            fg_color=EVENT_CARD_COLOR,
            border_color=BORDER_COLOR,
            text_color=TEXT_COLOR,
            placeholder_text="Enter member name...",
            placeholder_text_color=SUBTLE_TEXT
        )

        self.name_entry.pack(
            fill="x",
            padx=22
        )

        # ----------------------------------------------------
        # BIRTHDAY LABEL
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.form_card,
            text="Birthday",
            font=("Arial", 12, "bold"),
            text_color=MUTED_TEXT
        ).pack(
            anchor="w",
            padx=22,
            pady=(15, 6)
        )

        # ----------------------------------------------------
        # DATE SELECTORS
        # ----------------------------------------------------

        date_frame = ctk.CTkFrame(
            self.form_card,
            fg_color="transparent"
        )

        date_frame.pack(
            fill="x",
            padx=22
        )

        current_year = datetime.now().year

        self.day_var = ctk.StringVar(
            value="1"
        )

        self.day_menu = ctk.CTkOptionMenu(
            date_frame,
            values=[
                str(i)
                for i in range(1, 32)
            ],
            variable=self.day_var,
            width=90,
            height=40,
            corner_radius=10,
            fg_color=EVENT_CARD_COLOR,
            button_color=PRIMARY_COLOR,
            button_hover_color=PRIMARY_HOVER,
            text_color=TEXT_COLOR
        )

        self.day_menu.pack(
            side="left",
            padx=(0, 8)
        )

        self.month_var = ctk.StringVar(
            value=self.months[
                datetime.now().month - 1
            ]
        )

        self.month_menu = ctk.CTkOptionMenu(
            date_frame,
            values=self.months,
            variable=self.month_var,
            width=145,
            height=40,
            corner_radius=10,
            fg_color=EVENT_CARD_COLOR,
            button_color=PRIMARY_COLOR,
            button_hover_color=PRIMARY_HOVER,
            text_color=TEXT_COLOR
        )

        self.month_menu.pack(
            side="left",
            padx=8
        )

        self.year_var = ctk.StringVar(
            value=str(current_year)
        )

        self.year_menu = ctk.CTkOptionMenu(
            date_frame,
            values=[
                str(y)
                for y in range(
                    current_year,
                    1900,
                    -1
                )
            ],
            variable=self.year_var,
            width=110,
            height=40,
            corner_radius=10,
            fg_color=EVENT_CARD_COLOR,
            button_color=PRIMARY_COLOR,
            button_hover_color=PRIMARY_HOVER,
            text_color=TEXT_COLOR
        )

        self.year_menu.pack(
            side="left",
            padx=8
        )

        # ----------------------------------------------------
        # BUTTONS
        # ----------------------------------------------------

        button_frame = ctk.CTkFrame(
            self.form_card,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=22,
            pady=20
        )

        self.save_button = ctk.CTkButton(
            button_frame,
            text="＋  Save Birthday",
            height=42,
            width=170,
            corner_radius=10,
            font=("Arial", 13, "bold"),
            fg_color=PRIMARY_COLOR,
            hover_color=PRIMARY_HOVER,
            text_color="#102024",
            command=self.save_birthday
        )

        self.save_button.pack(
            side="left"
        )

        self.cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            height=42,
            width=100,
            corner_radius=10,
            font=("Arial", 13),
            fg_color="transparent",
            hover_color=EVENT_HOVER,
            border_width=1,
            border_color=BORDER_COLOR,
            text_color=MUTED_TEXT,
            command=self.cancel_edit
        )

        self.cancel_button.pack(
            side="left",
            padx=10
        )

        # ====================================================
        # SEARCH
        # ====================================================

        search_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        search_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            height=44,
            corner_radius=12,
            fg_color=CARD_COLOR,
            border_color=BORDER_COLOR,
            text_color=TEXT_COLOR,
            placeholder_text="🔍  Search birthdays by name...",
            placeholder_text_color=SUBTLE_TEXT
        )

        self.search_entry.pack(
            fill="x"
        )

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.load_birthdays()
        )

        # ====================================================
        # LIST
        # ====================================================

        self.list_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.list_frame.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # CLEAR LIST
    # ========================================================

    def clear_list(self):

        for widget in self.list_frame.winfo_children():
            widget.destroy()

    # ========================================================
    # LOAD BIRTHDAYS
    # ========================================================

    def load_birthdays(self):

        self.clear_list()

        birthdays = get_birthdays()

        # Sort by month and day
        try:

            birthdays.sort(
                key=lambda x:
                datetime.strptime(
                    x[2],
                    "%d/%m/%Y"
                ).strftime("%m%d")
            )

        except Exception:
            pass

        search = (
            self.search_entry
            .get()
            .strip()
            .lower()
        )

        if search:

            birthdays = [
                birthday
                for birthday in birthdays
                if search in birthday[1].lower()
            ]

        # Update count
        self.count_label.configure(
            text=f"{len(birthdays)} birthday"
            + ("s" if len(birthdays) != 1 else "")
        )

        # No results
        if not birthdays:

            empty_card = ctk.CTkFrame(
                self.list_frame,
                fg_color=CARD_COLOR,
                corner_radius=16,
                border_width=1,
                border_color=BORDER_COLOR
            )

            empty_card.pack(
                fill="x",
                pady=5
            )

            ctk.CTkLabel(
                empty_card,
                text="🎂",
                font=("Arial", 30)
            ).pack(
                pady=(25, 5)
            )

            ctk.CTkLabel(
                empty_card,
                text="No birthdays found",
                font=("Arial", 16, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                pady=(0, 3)
            )

            ctk.CTkLabel(
                empty_card,
                text="Add a birthday using the form above.",
                font=("Arial", 12),
                text_color=MUTED_TEXT
            ).pack(
                pady=(0, 25)
            )

            return

        # ====================================================
        # CREATE CARDS
        # ====================================================

        for (
            member_id,
            name,
            birthday
        ) in birthdays:

            try:

                date = datetime.strptime(
                    birthday,
                    "%d/%m/%Y"
                )

                short_date = date.strftime(
                    "%d %b"
                )

            except Exception:

                short_date = birthday

            # ------------------------------------------------
            # CARD
            # ------------------------------------------------

            card = ctk.CTkFrame(
                self.list_frame,
                fg_color=EVENT_CARD_COLOR,
                corner_radius=14,
                border_width=1,
                border_color=BORDER_COLOR
            )

            card.pack(
                fill="x",
                pady=6
            )

            # ------------------------------------------------
            # LEFT ICON
            # ------------------------------------------------

            icon_box = ctk.CTkFrame(
                card,
                width=50,
                height=50,
                corner_radius=14,
                fg_color=BIRTHDAY_BG
            )

            icon_box.pack(
                side="left",
                padx=(15, 15),
                pady=13
            )

            icon_box.pack_propagate(False)

            ctk.CTkLabel(
                icon_box,
                text="🎂",
                font=("Arial", 21)
            ).place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

            # ------------------------------------------------
            # INFORMATION
            # ------------------------------------------------

            info = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            info.pack(
                side="left",
                fill="x",
                expand=True,
                pady=12
            )

            ctk.CTkLabel(
                info,
                text=name,
                font=("Arial", 16, "bold"),
                text_color=TEXT_COLOR,
                anchor="w"
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                info,
                text="Birthday",
                font=("Arial", 11),
                text_color=MUTED_TEXT,
                anchor="w"
            ).pack(
                anchor="w",
                pady=(2, 0)
            )

            # ------------------------------------------------
            # DATE
            # ------------------------------------------------

            date_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            date_frame.pack(
                side="right",
                padx=18
            )

            ctk.CTkLabel(
                date_frame,
                text=short_date,
                font=("Arial", 16, "bold"),
                text_color=BIRTHDAY_COLOR
            ).pack()

            # ------------------------------------------------
            # ACTION BUTTONS
            # ------------------------------------------------

            actions = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            actions.pack(
                side="right",
                padx=(0, 12)
            )

            ctk.CTkButton(
                actions,
                text="Edit",
                width=65,
                height=34,
                corner_radius=9,
                font=("Arial", 11, "bold"),
                fg_color=PRIMARY_BG,
                hover_color=PRIMARY_COLOR,
                text_color=PRIMARY_COLOR,
                command=lambda i=member_id,
                n=name,
                d=birthday:
                self.edit_birthday(
                    i,
                    n,
                    d
                )
            ).pack(
                side="left",
                padx=3
            )

            ctk.CTkButton(
                actions,
                text="Delete",
                width=65,
                height=34,
                corner_radius=9,
                font=("Arial", 11, "bold"),
                fg_color="#3A2427",
                hover_color="#63363B",
                text_color="#E39A9F",
                command=lambda i=member_id:
                self.remove_birthday(i)
            ).pack(
                side="left",
                padx=3
            )

    # ========================================================
    # SAVE BIRTHDAY
    # ========================================================

    def save_birthday(self):

        name = (
            self.name_entry
            .get()
            .strip()
        )

        if name == "":

            messagebox.showwarning(
                "Missing Name",
                "Please enter the member's name."
            )

            return

        try:

            month_number = (
                self.months.index(
                    self.month_var.get()
                ) + 1
            )

            birthday = (
                f"{int(self.day_var.get()):02d}/"
                f"{month_number:02d}/"
                f"{self.year_var.get()}"
            )

            # Validate date
            datetime.strptime(
                birthday,
                "%d/%m/%Y"
            )

        except ValueError:

            messagebox.showwarning(
                "Invalid Date",
                "Please select a valid birthday."
            )

            return

        # Add
        if self.editing_id is None:

            add_birthday(
                name,
                birthday
            )

        # Update
        else:

            update_birthday(
                self.editing_id,
                name,
                birthday
            )

            self.editing_id = None

        self.reset_form()
        self.load_birthdays()

    # ========================================================
    # EDIT BIRTHDAY
    # ========================================================

    def edit_birthday(
        self,
        member_id,
        name,
        birthday
    ):

        self.editing_id = member_id

        # Name
        self.name_entry.delete(
            0,
            "end"
        )

        self.name_entry.insert(
            0,
            name
        )

        # Date
        try:

            date = datetime.strptime(
                birthday,
                "%d/%m/%Y"
            )

            self.day_var.set(
                str(date.day)
            )

            self.month_var.set(
                self.months[
                    date.month - 1
                ]
            )

            self.year_var.set(
                str(date.year)
            )

        except Exception:
            pass

        # Update form title
        self.form_title.configure(
            text="Edit Birthday"
        )

        # Update button
        self.save_button.configure(
            text="✓  Update Birthday"
        )

        # Scroll to top
        self.container._parent_canvas.yview_moveto(
            0
        )

    # ========================================================
    # CANCEL EDIT
    # ========================================================

    def cancel_edit(self):

        self.editing_id = None

        self.reset_form()

    # ========================================================
    # RESET FORM
    # ========================================================

    def reset_form(self):

        self.name_entry.delete(
            0,
            "end"
        )

        current_date = datetime.now()

        self.day_var.set(
            "1"
        )

        self.month_var.set(
            self.months[
                current_date.month - 1
            ]
        )

        self.year_var.set(
            str(current_date.year)
        )

        self.form_title.configure(
            text="Add Birthday"
        )

        self.save_button.configure(
            text="＋  Save Birthday"
        )

    # ========================================================
    # DELETE BIRTHDAY
    # ========================================================

    def remove_birthday(
        self,
        member_id
    ):

        answer = messagebox.askyesno(
            "Delete Birthday",
            "Are you sure you want to delete this birthday?"
        )

        if answer:

            delete_birthday(
                member_id
            )

            self.load_birthdays()
