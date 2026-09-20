import customtkinter as ctk

from database.db import create_tables
from pages.home import HomePage
from pages.birthday import BirthdaysPage
from pages.wedding import WeddingsPage

from excel_handler import (
    export_to_excel,
    import_from_excel,
    download_template
)

from notification import show_weekly_notifications

from backup_handler import (
    backup_database,
    restore_database
)


# ============================================================
# APP COLOR PALETTE
# ============================================================

BG_COLOR = "#101820"
SIDEBAR_COLOR = "#121D25"
CONTENT_COLOR = "#101820"

CARD_COLOR = "#182630"
BUTTON_COLOR = "#1D2D37"
BUTTON_HOVER = "#263943"

PRIMARY_COLOR = "#7FB3B0"
PRIMARY_HOVER = "#689996"

TEXT_COLOR = "#F2F5F4"
MUTED_TEXT = "#A8B7BC"
SUBTLE_TEXT = "#84969D"

BORDER_COLOR = "#30414A"


# ============================================================
# DATABASE
# ============================================================

create_tables()


# ============================================================
# CUSTOMTKINTER
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# ============================================================
# MAIN APPLICATION
# ============================================================

class ChurchReminderApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.title(
            "Church Reminder"
        )

        self.geometry(
            "1250x750"
        )

        self.minsize(
            1100,
            700
        )

        self.configure(
            fg_color=BG_COLOR
        )

        # ----------------------------------------------------
        # SIDEBAR
        # ----------------------------------------------------

        self.menu = ctk.CTkFrame(
            self,
            width=245,
            corner_radius=0,
            fg_color=SIDEBAR_COLOR
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(False)

        # ----------------------------------------------------
        # CHURCH BRANDING
        # ----------------------------------------------------

        brand_frame = ctk.CTkFrame(
            self.menu,
            fg_color="transparent"
        )

        brand_frame.pack(
            fill="x",
            padx=25,
            pady=(30, 25)
        )

        # Church icon
        ctk.CTkLabel(
            brand_frame,
            text="⛪",
            font=("Arial", 30)
        ).pack(
            anchor="w"
        )

        # Church name
        ctk.CTkLabel(
            brand_frame,
            text="Birthday & Wedding Reminder",
            font=("Arial", 22, "bold"),
            text_color=TEXT_COLOR,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        ctk.CTkLabel(
            brand_frame,
            text="Church",
            font=("Arial", 22, "bold"),
            text_color=PRIMARY_COLOR,
            anchor="w"
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            brand_frame,
            text="Birthday & Wedding\nReminder",
            font=("Arial", 11),
            text_color=MUTED_TEXT,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # Divider
        ctk.CTkFrame(
            self.menu,
            height=1,
            fg_color=BORDER_COLOR
        ).pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        # ----------------------------------------------------
        # NAVIGATION AREA
        # ----------------------------------------------------

        self.menu_scroll = ctk.CTkScrollableFrame(
            self.menu,
            width=205,
            fg_color="transparent",
            scrollbar_button_color="#344850",
            scrollbar_button_hover_color="#49616B"
        )

        self.menu_scroll.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # ----------------------------------------------------
        # NAVIGATION LABEL
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.menu_scroll,
            text="MENU",
            font=("Arial", 10, "bold"),
            text_color=SUBTLE_TEXT,
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=(5, 8)
        )

        # ----------------------------------------------------
        # HOME
        # ----------------------------------------------------

        self.home_btn = self.create_menu_button(
            "⌂",
            "Home",
            self.show_home
        )

        # ----------------------------------------------------
        # BIRTHDAYS
        # ----------------------------------------------------

        self.birthday_btn = self.create_menu_button(
            "🎂",
            "Birthdays",
            self.show_birthdays
        )

        # ----------------------------------------------------
        # WEDDINGS
        # ----------------------------------------------------

        self.wedding_btn = self.create_menu_button(
            "💍",
            "Weddings",
            self.show_weddings
        )

        # ----------------------------------------------------
        # DATA SECTION
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.menu_scroll,
            text="DATA",
            font=("Arial", 10, "bold"),
            text_color=SUBTLE_TEXT,
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=(25, 8)
        )

        # Export
        self.export_btn = self.create_menu_button(
            "↑",
            "Export Excel",
            export_to_excel
        )

        # Import
        self.import_btn = self.create_menu_button(
            "↓",
            "Import Excel",
            self.import_excel
        )

        # Template
        self.template_btn = self.create_menu_button(
            "▣",
            "Excel Template",
            download_template
        )

        # ----------------------------------------------------
        # BACKUP SECTION
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.menu_scroll,
            text="BACKUP",
            font=("Arial", 10, "bold"),
            text_color=SUBTLE_TEXT,
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=(25, 8)
        )

        # Backup
        self.backup_btn = self.create_menu_button(
            "▣",
            "Backup",
            backup_database
        )

        # Restore
        self.restore_btn = self.create_menu_button(
            "↻",
            "Restore",
            restore_database
        )

        # ----------------------------------------------------
        # SETTINGS
        # ----------------------------------------------------

        ctk.CTkLabel(
            self.menu_scroll,
            text="SETTINGS",
            font=("Arial", 10, "bold"),
            text_color=SUBTLE_TEXT,
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=(25, 8)
        )

        self.theme_btn = self.create_menu_button(
            "☾",
            "Theme",
            self.toggle_theme
        )

        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        footer = ctk.CTkFrame(
            self.menu,
            fg_color="transparent"
        )

        footer.pack(
            side="bottom",
            fill="x",
            padx=25,
            pady=20
        )

        ctk.CTkFrame(
            footer,
            height=1,
            fg_color=BORDER_COLOR
        ).pack(
            fill="x",
            pady=(0, 12)
        )

        ctk.CTkLabel(
            footer,
            text="Faith Glory Church",
            font=("Arial", 11, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            footer,
            text="Reminder System  •  v1.0",
            font=("Arial", 10),
            text_color=SUBTLE_TEXT
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        # ----------------------------------------------------
        # CONTENT AREA
        # ----------------------------------------------------

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=CONTENT_COLOR
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # CURRENT PAGE
        # ----------------------------------------------------

        self.current_page = None

        self.show_home()

        # ----------------------------------------------------
        # WEEKLY NOTIFICATIONS
        # ----------------------------------------------------

        show_weekly_notifications()

    # ========================================================
    # CREATE SIDEBAR BUTTON
    # ========================================================

    def create_menu_button(
        self,
        icon,
        text,
        command
    ):

        button = ctk.CTkButton(
            self.menu_scroll,
            text=f"{icon}    {text}",
            height=46,
            corner_radius=12,
            font=("Arial", 14, "bold"),
            fg_color="transparent",
            hover_color=BUTTON_HOVER,
            text_color=MUTED_TEXT,
            anchor="w",
            command=command
        )

        button.pack(
            fill="x",
            padx=8,
            pady=4
        )

        return button

    # ========================================================
    # PAGE BUTTON ACTIVE STATE
    # ========================================================

    def set_active_button(
        self,
        active_button
    ):

        buttons = [
            self.home_btn,
            self.birthday_btn,
            self.wedding_btn
        ]

        for button in buttons:

            button.configure(
                fg_color="transparent",
                text_color=MUTED_TEXT
            )

        active_button.configure(
            fg_color=PRIMARY_COLOR,
            text_color="#102024"
        )

    # ========================================================
    # CLEAR PAGE
    # ========================================================

    def clear_page(self):

        if self.current_page is not None:

            self.current_page.destroy()

            self.current_page = None

    # ========================================================
    # HOME
    # ========================================================

    def show_home(self):

        self.clear_page()

        self.current_page = HomePage(
            self.content
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

        self.set_active_button(
            self.home_btn
        )

    # ========================================================
    # BIRTHDAYS
    # ========================================================

    def show_birthdays(self):

        self.clear_page()

        self.current_page = BirthdaysPage(
            self.content
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

        self.set_active_button(
            self.birthday_btn
        )

    # ========================================================
    # WEDDINGS
    # ========================================================

    def show_weddings(self):

        self.clear_page()

        self.current_page = WeddingsPage(
            self.content
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

        self.set_active_button(
            self.wedding_btn
        )

    # ========================================================
    # IMPORT EXCEL
    # ========================================================

    def import_excel(self):

        import_from_excel()

        if isinstance(
            self.current_page,
            HomePage
        ):

            self.show_home()

        elif isinstance(
            self.current_page,
            BirthdaysPage
        ):

            self.show_birthdays()

        elif isinstance(
            self.current_page,
            WeddingsPage
        ):

            self.show_weddings()

    # ========================================================
    # THEME
    # ========================================================

    def toggle_theme(self):

        if ctk.get_appearance_mode() == "Dark":

            ctk.set_appearance_mode("Light")

        else:

            ctk.set_appearance_mode("Dark")


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app = ChurchReminderApp()

    app.mainloop()