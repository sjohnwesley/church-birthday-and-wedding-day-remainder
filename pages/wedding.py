import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from database.db import (
    add_wedding,
    get_weddings,
    update_wedding,
    delete_wedding
)


# ============================================================
# COLORS
# ============================================================

BG_COLOR = "#101820"
CARD_COLOR = "#182630"
EVENT_COLOR = "#202F38"
EVENT_HOVER = "#263943"

PRIMARY = "#7FB3B0"
PRIMARY_LIGHT = "#203A3B"

WEDDING_COLOR = "#B3A4C8"
WEDDING_BG = "#302C3A"

TEXT_COLOR = "#F2F5F4"
MUTED_TEXT = "#A8B7BC"
SUBTLE_TEXT = "#84969D"

BORDER_COLOR = "#30414A"
EVENT_BORDER = "#344850"


class WeddingsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=BG_COLOR
        )

        self.editing_id = None

        # ====================================================
        # MAIN SCROLL AREA
        # ====================================================

        self.container = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
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

        ctk.CTkLabel(
            header,
            text="Wedding Anniversaries",
            font=("Arial", 30, "bold"),
            text_color=TEXT_COLOR
        ).pack(anchor="w")

        ctk.CTkLabel(
            header,
            text="Manage church member wedding anniversaries",
            font=("Arial", 14),
            text_color=MUTED_TEXT
        ).pack(anchor="w", pady=(4, 0))

        # ====================================================
        # ADD / EDIT CARD
        # ====================================================

        form_card = ctk.CTkFrame(
            self.container,
            fg_color=CARD_COLOR,
            corner_radius=18,
            border_width=1,
            border_color=BORDER_COLOR
        )

        form_card.pack(
            fill="x",
            pady=(0, 20)
        )

        # Form title

        self.form_title = ctk.CTkLabel(
            form_card,
            text="Add Wedding Anniversary",
            font=("Arial", 20, "bold"),
            text_color=TEXT_COLOR
        )

        self.form_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )

        # ====================================================
        # NAMES
        # ====================================================

        names_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        names_frame.pack(
            fill="x",
            padx=25
        )

        # Husband

        husband_frame = ctk.CTkFrame(
            names_frame,
            fg_color="transparent"
        )

        husband_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        ctk.CTkLabel(
            husband_frame,
            text="Husband",
            font=("Arial", 13, "bold"),
            text_color=MUTED_TEXT
        ).pack(anchor="w", pady=(0, 6))

        self.husband_entry = ctk.CTkEntry(
            husband_frame,
            height=42,
            corner_radius=10,
            border_color=BORDER_COLOR,
            fg_color=EVENT_COLOR,
            text_color=TEXT_COLOR,
            placeholder_text="Enter husband's name",
            placeholder_text_color=SUBTLE_TEXT
        )

        self.husband_entry.pack(
            fill="x"
        )

        # Wife

        wife_frame = ctk.CTkFrame(
            names_frame,
            fg_color="transparent"
        )

        wife_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 0)
        )

        ctk.CTkLabel(
            wife_frame,
            text="Wife",
            font=("Arial", 13, "bold"),
            text_color=MUTED_TEXT
        ).pack(anchor="w", pady=(0, 6))

        self.wife_entry = ctk.CTkEntry(
            wife_frame,
            height=42,
            corner_radius=10,
            border_color=BORDER_COLOR,
            fg_color=EVENT_COLOR,
            text_color=TEXT_COLOR,
            placeholder_text="Enter wife's name",
            placeholder_text_color=SUBTLE_TEXT
        )

        self.wife_entry.pack(
            fill="x"
        )

        # ====================================================
        # DATE
        # ====================================================

        ctk.CTkLabel(
            form_card,
            text="Wedding Anniversary Date",
            font=("Arial", 13, "bold"),
            text_color=MUTED_TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(18, 6)
        )

        date_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        date_frame.pack(
            anchor="w",
            padx=25
        )

        # Day

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
            fg_color=EVENT_COLOR,
            button_color=PRIMARY,
            button_hover_color=PRIMARY,
            text_color=TEXT_COLOR
        )

        self.day_menu.pack(
            side="left",
            padx=(0, 8)
        )

        # Month

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
            fg_color=EVENT_COLOR,
            button_color=PRIMARY,
            button_hover_color=PRIMARY,
            text_color=TEXT_COLOR
        )

        self.month_menu.pack(
            side="left",
            padx=8
        )

        # Year

        current_year = datetime.now().year

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
            width=105,
            height=40,
            corner_radius=10,
            fg_color=EVENT_COLOR,
            button_color=PRIMARY,
            button_hover_color=PRIMARY,
            text_color=TEXT_COLOR
        )

        self.year_menu.pack(
            side="left",
            padx=8
        )

        # ====================================================
        # FORM BUTTONS
        # ====================================================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        self.save_button = ctk.CTkButton(
            button_frame,
            text="Save Anniversary",
            height=42,
            width=180,
            corner_radius=10,
            fg_color=PRIMARY,
            hover_color="#6FA29F",
            text_color="#101820",
            font=("Arial", 14, "bold"),
            command=self.save_wedding
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
            fg_color="transparent",
            hover_color=EVENT_HOVER,
            border_width=1,
            border_color=BORDER_COLOR,
            text_color=MUTED_TEXT,
            font=("Arial", 14),
            command=self.cancel_edit
        )

        self.cancel_button.pack(
            side="left",
            padx=10
        )

        # ====================================================
        # SEARCH HEADER
        # ====================================================

        search_header = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        search_header.pack(
            fill="x",
            pady=(5, 10)
        )

        ctk.CTkLabel(
            search_header,
            text="Anniversaries",
            font=("Arial", 22, "bold"),
            text_color=TEXT_COLOR
        ).pack(side="left")

        self.count_label = ctk.CTkLabel(
            search_header,
            text="0",
            font=("Arial", 13, "bold"),
            text_color=WEDDING_COLOR,
            fg_color=WEDDING_BG,
            corner_radius=10,
            padx=12,
            pady=5
        )

        self.count_label.pack(
            side="left",
            padx=10
        )

        # ====================================================
        # SEARCH
        # ====================================================

        self.search_entry = ctk.CTkEntry(
            self.container,
            height=42,
            corner_radius=10,
            fg_color=CARD_COLOR,
            border_color=BORDER_COLOR,
            text_color=TEXT_COLOR,
            placeholder_text="Search by husband or wife...",
            placeholder_text_color=SUBTLE_TEXT
        )

        self.search_entry.pack(
            fill="x",
            pady=(0, 15)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.load_weddings()
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

        self.load_weddings()

    # ========================================================
    # CLEAR LIST
    # ========================================================

    def clear_list(self):

        for widget in self.list_frame.winfo_children():
            widget.destroy()

    # ========================================================
    # LOAD WEDDINGS
    # ========================================================

    def load_weddings(self):

        self.clear_list()

        weddings = get_weddings()

        # Sort by month and day

        def sort_key(item):

            try:
                return datetime.strptime(
                    item[3],
                    "%d/%m/%Y"
                ).strftime("%m%d")

            except:
                return "9999"

        weddings.sort(
            key=sort_key
        )

        # Search

        search = (
            self.search_entry
            .get()
            .strip()
            .lower()
        )

        if search:

            weddings = [
                wedding
                for wedding in weddings
                if (
                    search in wedding[1].lower()
                    or search in wedding[2].lower()
                )
            ]

        # Update count

        self.count_label.configure(
            text=str(len(weddings))
        )

        # No results

        if not weddings:

            empty_card = ctk.CTkFrame(
                self.list_frame,
                fg_color=CARD_COLOR,
                corner_radius=15,
                border_width=1,
                border_color=BORDER_COLOR
            )

            empty_card.pack(
                fill="x",
                pady=10
            )

            ctk.CTkLabel(
                empty_card,
                text="💍",
                font=("Arial", 35)
            ).pack(
                pady=(25, 5)
            )

            ctk.CTkLabel(
                empty_card,
                text="No wedding anniversaries found",
                font=("Arial", 17, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                pady=(0, 5)
            )

            ctk.CTkLabel(
                empty_card,
                text="Add a wedding anniversary using the form above.",
                font=("Arial", 13),
                text_color=MUTED_TEXT
            ).pack(
                pady=(0, 25)
            )

            return

        # ====================================================
        # WEDDING CARDS
        # ====================================================

        for member_id, husband, wife, anniversary in weddings:

            try:

                date = datetime.strptime(
                    anniversary,
                    "%d/%m/%Y"
                )

                short_date = date.strftime(
                    "%d %b"
                )

            except:

                short_date = anniversary

            card = ctk.CTkFrame(
                self.list_frame,
                fg_color=EVENT_COLOR,
                corner_radius=15,
                border_width=1,
                border_color=EVENT_BORDER
            )

            card.pack(
                fill="x",
                pady=7
            )

            # Left side

            left = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            left.pack(
                side="left",
                fill="both",
                expand=True,
                padx=18,
                pady=15
            )

            # Icon

            icon = ctk.CTkLabel(
                left,
                text="💍",
                font=("Arial", 25),
                text_color=WEDDING_COLOR
            )

            icon.pack(
                side="left",
                padx=(0, 15)
            )

            # Names

            info = ctk.CTkFrame(
                left,
                fg_color="transparent"
            )

            info.pack(
                side="left",
                fill="x",
                expand=True
            )

            ctk.CTkLabel(
                info,
                text=f"{husband} & {wife}",
                font=("Arial", 17, "bold"),
                text_color=TEXT_COLOR
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                info,
                text="Wedding Anniversary",
                font=("Arial", 12),
                text_color=MUTED_TEXT
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

            # Date

            date_badge = ctk.CTkLabel(
                card,
                text=short_date,
                font=("Arial", 13, "bold"),
                text_color=WEDDING_COLOR,
                fg_color=WEDDING_BG,
                corner_radius=9,
                padx=12,
                pady=7
            )

            date_badge.pack(
                side="left",
                padx=10
            )

            # Buttons

            button_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            button_frame.pack(
                side="right",
                padx=15
            )

            ctk.CTkButton(
                button_frame,
                text="Edit",
                width=70,
                height=34,
                corner_radius=8,
                fg_color=PRIMARY_LIGHT,
                hover_color=EVENT_HOVER,
                text_color=PRIMARY,
                font=("Arial", 12, "bold"),
                command=lambda i=member_id,
                h=husband,
                w=wife,
                a=anniversary:
                    self.edit_wedding(
                        i,
                        h,
                        w,
                        a
                    )
            ).pack(
                side="left",
                padx=3
            )

            ctk.CTkButton(
                button_frame,
                text="Delete",
                width=70,
                height=34,
                corner_radius=8,
                fg_color="#3A2A2A",
                hover_color="#4A3030",
                text_color="#E3A092",
                font=("Arial", 12, "bold"),
                command=lambda i=member_id:
                    self.remove_wedding(i)
            ).pack(
                side="left",
                padx=3
            )

    # ========================================================
    # SAVE / UPDATE
    # ========================================================

    def save_wedding(self):

        husband = (
            self.husband_entry
            .get()
            .strip()
        )

        wife = (
            self.wife_entry
            .get()
            .strip()
        )

        if husband == "" or wife == "":

            messagebox.showwarning(
                "Missing Details",
                "Please enter both husband and wife names."
            )

            return

        try:

            month_number = (
                self.months.index(
                    self.month_var.get()
                ) + 1
            )

            day = int(
                self.day_var.get()
            )

            year = int(
                self.year_var.get()
            )

            # Validate actual date

            datetime(
                year,
                month_number,
                day
            )

            anniversary = (
                f"{day:02d}/"
                f"{month_number:02d}/"
                f"{year}"
            )

        except ValueError:

            messagebox.showwarning(
                "Invalid Date",
                "Please select a valid anniversary date."
            )

            return

        # Add

        if self.editing_id is None:

            add_wedding(
                husband,
                wife,
                anniversary
            )

        # Update

        else:

            update_wedding(
                self.editing_id,
                husband,
                wife,
                anniversary
            )

        self.reset_form()

        self.load_weddings()

    # ========================================================
    # EDIT
    # ========================================================

    def edit_wedding(
        self,
        member_id,
        husband,
        wife,
        anniversary
    ):

        self.editing_id = member_id

        self.husband_entry.delete(
            0,
            "end"
        )

        self.husband_entry.insert(
            0,
            husband
        )

        self.wife_entry.delete(
            0,
            "end"
        )

        self.wife_entry.insert(
            0,
            wife
        )

        try:

            date = datetime.strptime(
                anniversary,
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

        except:

            pass

        self.form_title.configure(
            text="Edit Wedding Anniversary"
        )

        self.save_button.configure(
            text="Update Anniversary"
        )

        # Scroll to top

        try:

            self.container._parent_canvas.yview_moveto(0)

        except:

            pass

    # ========================================================
    # CANCEL EDIT
    # ========================================================

    def cancel_edit(self):

        self.reset_form()

    # ========================================================
    # RESET FORM
    # ========================================================

    def reset_form(self):

        self.editing_id = None

        self.husband_entry.delete(
            0,
            "end"
        )

        self.wife_entry.delete(
            0,
            "end"
        )

        self.form_title.configure(
            text="Add Wedding Anniversary"
        )

        self.save_button.configure(
            text="Save Anniversary"
        )

        # Reset date

        self.day_var.set("1")

        self.month_var.set(
            self.months[
                datetime.now().month - 1
            ]
        )

        self.year_var.set(
            str(datetime.now().year)
        )

    # ========================================================
    # DELETE
    # ========================================================

    def remove_wedding(self, member_id):

        answer = messagebox.askyesno(
            "Delete Wedding",
            "Delete this wedding anniversary?"
        )

        if answer:

            delete_wedding(
                member_id
            )

            self.load_weddings()