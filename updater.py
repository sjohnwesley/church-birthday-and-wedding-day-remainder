import os
import sys
import time
import zipfile
import shutil
import tempfile
import subprocess
import ctypes
import argparse
from pathlib import Path
from urllib.request import Request, urlopen


# ============================================================
# CHURCH REMINDER UPDATER
# ============================================================

APP_EXE_NAME = "Church Reminder.exe"


# ============================================================
# ADMIN CHECK
# ============================================================

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def restart_as_admin():
    """
    Restart this updater with administrator permission.
    """

    params = " ".join(
        f'"{arg}"'
        for arg in sys.argv[1:]
    )

    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        params,
        None,
        1
    )

    sys.exit(0)


# ============================================================
# DOWNLOAD
# ============================================================

def download_file(url, destination):

    if not url.startswith("https://"):
        raise ValueError(
            "Update URL must use HTTPS."
        )

    request = Request(
        url,
        headers={
            "User-Agent": "Church-Reminder-Updater"
        }
    )

    with urlopen(request, timeout=60) as response:

        with open(destination, "wb") as file:

            while True:

                chunk = response.read(1024 * 1024)

                if not chunk:
                    break

                file.write(chunk)


# ============================================================
# WAIT FOR MAIN APPLICATION
# ============================================================

def wait_for_process(pid, timeout=60):

    if not pid:
        return

    start_time = time.time()

    while time.time() - start_time < timeout:

        try:

            result = subprocess.run(
                [
                    "tasklist",
                    "/FI",
                    f"PID eq {pid}"
                ],
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            if str(pid) not in result.stdout:
                return

        except Exception:
            return

        time.sleep(1)


# ============================================================
# SAFE ZIP EXTRACTION
# ============================================================

def extract_update(zip_path, extract_folder):

    with zipfile.ZipFile(
        zip_path,
        "r"
    ) as archive:

        for member in archive.infolist():

            member_path = Path(
                extract_folder,
                member.filename
            ).resolve()

            extract_root = Path(
                extract_folder
            ).resolve()

            if not str(member_path).startswith(
                str(extract_root)
            ):
                raise Exception(
                    "Unsafe file detected in update package."
                )

        archive.extractall(
            extract_folder
        )


# ============================================================
# UPDATE APPLICATION
# ============================================================

def install_update(
    extracted_folder,
    application_folder
):

    new_exe = Path(
        extracted_folder
    ) / APP_EXE_NAME

    current_exe = Path(
        application_folder
    ) / APP_EXE_NAME

    if not new_exe.exists():

        raise FileNotFoundError(
            f"{APP_EXE_NAME} was not found in the update package."
        )

    # --------------------------------------------------------
    # Backup current EXE
    # --------------------------------------------------------

    backup_exe = current_exe.with_suffix(
        ".exe.old"
    )

    if backup_exe.exists():

        try:
            backup_exe.unlink()
        except Exception:
            pass

    shutil.copy2(
        current_exe,
        backup_exe
    )

    # --------------------------------------------------------
    # Replace application
    # --------------------------------------------------------

    try:

        shutil.copy2(
            new_exe,
            current_exe
        )

    except Exception:

        # Restore old version if replacement fails

        if backup_exe.exists():

            shutil.copy2(
                backup_exe,
                current_exe
            )

        raise

    # --------------------------------------------------------
    # Remove backup
    # --------------------------------------------------------

    try:
        backup_exe.unlink()
    except Exception:
        pass


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--url",
        required=True,
        help="HTTPS URL of the update ZIP"
    )

    parser.add_argument(
        "--pid",
        type=int,
        default=0,
        help="PID of the running Church Reminder application"
    )

    parser.add_argument(
        "--app-dir",
        required=True,
        help="Installation directory"
    )

    args = parser.parse_args()

    # --------------------------------------------------------
    # Request administrator permission
    # --------------------------------------------------------

    if not is_admin():

        restart_as_admin()
        return

    # --------------------------------------------------------
    # Temporary working directory
    # --------------------------------------------------------

    temp_folder = tempfile.mkdtemp(
        prefix="church_reminder_update_"
    )

    try:

        zip_path = os.path.join(
            temp_folder,
            "update.zip"
        )

        extract_folder = os.path.join(
            temp_folder,
            "extracted"
        )

        os.makedirs(
            extract_folder,
            exist_ok=True
        )

        # ----------------------------------------------------
        # Download
        # ----------------------------------------------------

        print("Downloading update...")

        download_file(
            args.url,
            zip_path
        )

        # ----------------------------------------------------
        # Extract
        # ----------------------------------------------------

        print("Extracting update...")

        extract_update(
            zip_path,
            extract_folder
        )

        # ----------------------------------------------------
        # Wait for main application to close
        # ----------------------------------------------------

        print("Waiting for Church Reminder to close...")

        wait_for_process(
            args.pid
        )

        # ----------------------------------------------------
        # Install
        # ----------------------------------------------------

        print("Installing update...")

        install_update(
            extract_folder,
            args.app_dir
        )

        # ----------------------------------------------------
        # Start updated application
        # ----------------------------------------------------

        updated_exe = os.path.join(
            args.app_dir,
            APP_EXE_NAME
        )

        subprocess.Popen(
            [updated_exe],
            cwd=args.app_dir
        )

        print("Update completed.")

    except Exception as error:

        message = (
            "Church Reminder could not be updated.\n\n"
            f"Reason:\n{error}"
        )

        ctypes.windll.user32.MessageBoxW(
            None,
            message,
            "Church Reminder Update",
            0x10
        )

    finally:

        # Give the new application time to start
        time.sleep(2)

        try:
            shutil.rmtree(
                temp_folder,
                ignore_errors=True
            )
        except Exception:
            pass


if __name__ == "__main__":
    main()