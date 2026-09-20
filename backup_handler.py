import shutil
from tkinter import messagebox


def backup_database():

    shutil.copy(
        "data/church.db",
        "church_backup.db"
    )

    messagebox.showinfo(
        "Backup",
        "Backup created successfully."
    )


def restore_database():

    shutil.copy(
        "church_backup.db",
        "data/church.db"
    )

    messagebox.showinfo(
        "Restore",
        "Database restored successfully."
    )