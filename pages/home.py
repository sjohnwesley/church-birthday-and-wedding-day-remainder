import customtkinter as ctk
from datetime import datetime, timedelta
from database.db import get_birthdays, get_weddings


# ============================================================
# DARK SOOTHING PROFESSIONAL COLOR PALETTE
# ============================================================

# Main background
BG_COLOR = "#101820"

# Main cards / week sections
CARD_COLOR = "#182630"

# Event cards
EVENT_CARD_COLOR = "#202F38"
EVENT_CARD_HOVER = "#263943"

# Main accent
PRIMARY_COLOR = "#7FB3B0"
PRIMARY_LIGHT = "#203A3B"

# Birthday
BIRTHDAY_COLOR = "#E3A092"
BIRTHDAY_BG = "#3A2B2A"

# Wedding
WEDDING_COLOR = "#B3A4C8"
WEDDING_BG = "#302C3A"

# General accent
ACCENT_COLOR = "#91B8A9"
ACCENT_BG = "#263B35"

# Text
TEXT_COLOR = "#F2F5F4"
MUTED_TEXT = "#A8B7BC"
SUBTLE_TEXT = "#84969D"

# Borders
BORDER_COLOR = "#30414A"
EVENT_BORDER = "#344850"


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=BG_COLOR
        )

        # Load database data
        self.birthdays = get_birthdays()
        self.weddings = get_weddings()

        self.build_ui()
        self.load_upcoming()

    # ========================================================
    # MAIN UI
    # ========================================================

    def build_ui(self):

        # Scrollable main area
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
            pady=(0, 25)
        )

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_frame,
            text="Faith Glory Church",
            font=("Arial", 28, "bold"),
            text_color=TEXT_COLOR,
            anchor="w"
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_frame,
            text="Church Dashboard",
            font=("Arial", 15),
            text_color=PRIMARY_COLOR,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        ctk.CTkLabel(
            title_frame,
            text="Birthdays & Wedding Anniversaries",
            font=("Arial", 13),
            text_color=MUTED_TEXT,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        # ----------------------------------------------------
        # DATE BOX
        # ----------------------------------------------------

        date_frame = ctk.CTkFrame(
            header,
            fg_color=CARD_COLOR,
            corner_radius=12,
            border_width=1,
            border_color=BORDER_COLOR
        )

        date_frame.pack(
            side="right",
            padx=5,
            pady=5
        )

        ctk.CTkLabel(
            date_frame,
            text="TODAY",
            font=("Arial", 10, "bold"),
            text_color=PRIMARY_COLOR
        ).pack(
            padx=18,
            pady=(10, 0)
        )

        ctk.CTkLabel(
            date_frame,
            text=datetime.now().strftime("%d %b %Y"),
            font=("Arial", 14, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            padx=18,
            pady=(2, 10)
        )

        # ====================================================
        # STAT CARDS
        # ====================================================

        self.stats_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.stats_frame.pack(
            fill="x",
            pady=(0, 25)
        )

        for i in range(3):
            self.stats_frame.grid_columnconfigure(
                i,
                weight=1
            )

        # Birthday card
        self.birthday_card = self.create_stat_card(
            self.stats_frame,
            "🎂",
            "Birthdays",
            BIRTHDAY_COLOR,
            BIRTHDAY_BG,
            0
        )

        # Wedding card
        self.wedding_card = self.create_stat_card(
            self.stats_frame,
            "💍",
            "Anniversaries",
            WEDDING_COLOR,
            WEDDING_BG,
            1
        )

        # Total card
        self.total_card = self.create_stat_card(
            self.stats_frame,
            "✨",
            "Celebrations",
            ACCENT_COLOR,
            ACCENT_BG,
            2
        )

        # ====================================================
        # EVENTS AREA
        # ====================================================

        self.events_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.events_frame.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat_card(
        self,
        parent,
        icon,
        title,
        icon_color,
        icon_background,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=7
        )

        # Icon box
        icon_box = ctk.CTkFrame(
            card,
            width=48,
            height=48,
            corner_radius=14,
            fg_color=icon_background
        )

        icon_box.pack(
            anchor="w",
            padx=18,
            pady=(18, 8)
        )

        icon_box.pack_propagate(False)

        ctk.CTkLabel(
            icon_box,
            text=icon,
            font=("Arial", 21)
        ).place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Number
        value_label = ctk.CTkLabel(
            card,
            text="0",
            font=("Arial", 28, "bold"),
            text_color=TEXT_COLOR
        )

        value_label.pack(
            anchor="w",
            padx=18
        )

        # Title
        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 13),
            text_color=MUTED_TEXT
        ).pack(
            anchor="w",
            padx=18,
            pady=(0, 18)
        )

        return value_label

    # ========================================================
    # WEEK SECTION
    # ========================================================

    def create_week_section(
        self,
        title,
        start_date,
        end_date
    ):

        section = ctk.CTkFrame(
            self.events_frame,
            fg_color=CARD_COLOR,
            corner_radius=16,
            border_width=1,
            border_color=BORDER_COLOR
        )

        section.pack(
            fill="x",
            pady=(0, 20)
        )

        # ----------------------------------------------------
        # WEEK HEADER
        # ----------------------------------------------------

        header = ctk.CTkFrame(
            section,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=22,
            pady=(18, 10)
        )

        # Title area
        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_frame,
            text=title,
            font=("Arial", 19, "bold"),
            text_color=TEXT_COLOR
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_frame,
            text="Sunday - Saturday",
            font=("Arial", 11),
            text_color=MUTED_TEXT
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        # Date badge
        date_text = (
            f"{start_date.strftime('%d %b')} "
            f"— "
            f"{end_date.strftime('%d %b')}"
        )

        date_badge = ctk.CTkLabel(
            header,
            text=date_text,
            font=("Arial", 12, "bold"),
            text_color=PRIMARY_COLOR,
            fg_color=PRIMARY_LIGHT,
            corner_radius=10
        )

        date_badge.pack(
            side="right",
            padx=5,
            pady=5
        )

        # Divider
        ctk.CTkFrame(
            section,
            height=1,
            fg_color=BORDER_COLOR
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        # ----------------------------------------------------
        # EVENTS
        # ----------------------------------------------------

        event_count = 0

        # ====================================================
        # BIRTHDAYS
        # ====================================================

        for member_id, name, birthday in self.birthdays:

            try:

                date = datetime.strptime(
                    birthday,
                    "%d/%m/%Y"
                )

                event_date = date.replace(
                    year=start_date.year
                )

                if (
                    start_date.date()
                    <= event_date.date()
                    <= end_date.date()
                ):

                    self.create_event_row(
                        section,
                        "🎂",
                        name,
                        "Birthday",
                        event_date,
                        BIRTHDAY_COLOR,
                        BIRTHDAY_BG
                    )

                    event_count += 1

            except Exception:
                pass

        # ====================================================
        # WEDDING ANNIVERSARIES
        # ====================================================

        for (
            member_id,
            husband,
            wife,
            anniversary
        ) in self.weddings:

            try:

                date = datetime.strptime(
                    anniversary,
                    "%d/%m/%Y"
                )

                event_date = date.replace(
                    year=start_date.year
                )

                if (
                    start_date.date()
                    <= event_date.date()
                    <= end_date.date()
                ):

                    self.create_event_row(
                        section,
                        "💍",
                        f"{husband} & {wife}",
                        "Wedding Anniversary",
                        event_date,
                        WEDDING_COLOR,
                        WEDDING_BG
                    )

                    event_count += 1

            except Exception:
                pass

        # ====================================================
        # NO EVENTS
        # ====================================================

        if event_count == 0:

            empty_frame = ctk.CTkFrame(
                section,
                fg_color="transparent"
            )

            empty_frame.pack(
                fill="x",
                padx=22,
                pady=(5, 22)
            )

            ctk.CTkLabel(
                empty_frame,
                text="No celebrations scheduled",
                font=("Arial", 13),
                text_color=MUTED_TEXT
            ).pack(
                anchor="w"
            )

    # ========================================================
    # EVENT ROW
    # ========================================================

    def create_event_row(
        self,
        parent,
        icon,
        name,
        event_type,
        event_date,
        icon_color,
        icon_background
    ):

        # Event card
        row = ctk.CTkFrame(
            parent,
            fg_color=EVENT_CARD_COLOR,
            corner_radius=12,
            border_width=1,
            border_color=EVENT_BORDER
        )

        row.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # ----------------------------------------------------
        # ICON
        # ----------------------------------------------------

        icon_box = ctk.CTkFrame(
            row,
            width=44,
            height=44,
            corner_radius=12,
            fg_color=icon_background
        )

        icon_box.pack(
            side="left",
            padx=(12, 12),
            pady=10
        )

        icon_box.pack_propagate(False)

        ctk.CTkLabel(
            icon_box,
            text=icon,
            font=("Arial", 19)
        ).place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ----------------------------------------------------
        # INFORMATION
        # ----------------------------------------------------

        info = ctk.CTkFrame(
            row,
            fg_color="transparent"
        )

        info.pack(
            side="left",
            fill="x",
            expand=True,
            pady=9
        )

        # NAME
        ctk.CTkLabel(
            info,
            text=name,
            font=("Arial", 14, "bold"),
            text_color=TEXT_COLOR,
            anchor="w"
        ).pack(
            anchor="w"
        )

        # EVENT TYPE
        ctk.CTkLabel(
            info,
            text=event_type,
            font=("Arial", 11),
            text_color=MUTED_TEXT,
            anchor="w"
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        # ----------------------------------------------------
        # DATE
        # ----------------------------------------------------

        date_box = ctk.CTkFrame(
            row,
            fg_color="transparent"
        )

        date_box.pack(
            side="right",
            padx=18
        )

        ctk.CTkLabel(
            date_box,
            text=event_date.strftime("%d"),
            font=("Arial", 17, "bold"),
            text_color=icon_color
        ).pack()

        ctk.CTkLabel(
            date_box,
            text=event_date.strftime("%b"),
            font=("Arial", 10),
            text_color=MUTED_TEXT
        ).pack()

    # ========================================================
    # LOAD UPCOMING
    # ========================================================

    def load_upcoming(self):

        # Clear previous week sections
        for widget in self.events_frame.winfo_children():
            widget.destroy()

        today = datetime.now()

        # ====================================================
        # SUNDAY-BASED WEEK
        # ====================================================

        days_since_sunday = (
            today.weekday() + 1
        ) % 7

        this_week_start = (
            today -
            timedelta(days=days_since_sunday)
        ).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        this_week_end = (
            this_week_start +
            timedelta(days=6)
        )

        next_week_start = (
            this_week_start +
            timedelta(days=7)
        )

        next_week_end = (
            next_week_start +
            timedelta(days=6)
        )

        # ====================================================
        # COUNT THIS WEEK
        # ====================================================

        this_week_birthdays = self.count_birthdays(
            this_week_start,
            this_week_end
        )

        this_week_weddings = self.count_weddings(
            this_week_start,
            this_week_end
        )

        # ====================================================
        # COUNT NEXT WEEK
        # ====================================================

        next_week_birthdays = self.count_birthdays(
            next_week_start,
            next_week_end
        )

        next_week_weddings = self.count_weddings(
            next_week_start,
            next_week_end
        )

        # ====================================================
        # STATISTICS
        # ====================================================

        # Sunday:
        # Show statistics for both weeks

        if today.weekday() == 6:

            birthday_count = (
                this_week_birthdays +
                next_week_birthdays
            )

            wedding_count = (
                this_week_weddings +
                next_week_weddings
            )

        # Monday-Saturday:
        # Show statistics for next week

        else:

            birthday_count = next_week_birthdays
            wedding_count = next_week_weddings

        # Update cards
        self.birthday_card.configure(
            text=str(birthday_count)
        )

        self.wedding_card.configure(
            text=str(wedding_count)
        )

        self.total_card.configure(
            text=str(
                birthday_count +
                wedding_count
            )
        )

        # ====================================================
        # SUNDAY
        # THIS WEEK + NEXT WEEK
        # ====================================================

        if today.weekday() == 6:

            self.create_week_section(
                "This Week",
                this_week_start,
                this_week_end
            )

            self.create_week_section(
                "Next Week",
                next_week_start,
                next_week_end
            )

        # ====================================================
        # MONDAY-SATURDAY
        # NEXT WEEK ONLY
        # ====================================================

        else:

            self.create_week_section(
                "Next Week",
                next_week_start,
                next_week_end
            )

    # ========================================================
    # COUNT BIRTHDAYS
    # ========================================================

    def count_birthdays(
        self,
        start_date,
        end_date
    ):

        count = 0

        for member_id, name, birthday in self.birthdays:

            try:

                date = datetime.strptime(
                    birthday,
                    "%d/%m/%Y"
                )

                event_date = date.replace(
                    year=start_date.year
                )

                if (
                    start_date.date()
                    <= event_date.date()
                    <= end_date.date()
                ):

                    count += 1

            except Exception:
                pass

        return count

    # ========================================================
    # COUNT WEDDINGS
    # ========================================================

    def count_weddings(
        self,
        start_date,
        end_date
    ):

        count = 0

        for (
            member_id,
            husband,
            wife,
            anniversary
        ) in self.weddings:

            try:

                date = datetime.strptime(
                    anniversary,
                    "%d/%m/%Y"
                )

                event_date = date.replace(
                    year=start_date.year
                )

                if (
                    start_date.date()
                    <= event_date.date()
                    <= end_date.date()
                ):

                    count += 1

            except Exception:
                pass

        return count