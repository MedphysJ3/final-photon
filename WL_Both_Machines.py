import os
import shutil
from datetime import datetime, date
from pylinac import WinstonLutz

def has_relevant_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filename.startswith('RI') and os.path.getsize(filepath) in range(804 * 1024 - 100, 804 * 1024 + 100):
            return True
    return False

def find_today_folder(base_dir):
    today = date.today()
    for entry in os.scandir(base_dir):
        if entry.is_dir():
            creation_time = os.path.getctime(entry.path)
            folder_date = date.fromtimestamp(creation_time)
            if folder_date == today and has_relevant_files(entry.path):
                return entry.path
    return None

def copy_files(source_dir, dest_dir):
    if not source_dir:
        return
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        if filename.startswith('RI') and os.path.getsize(filepath) in range(804 * 1024 - 100, 804 * 1024 + 100):
            try:
                shutil.copy2(filepath, os.path.join(dest_dir, filename))
                print(f"Copied: {filename}")
            except Exception as e:
                print(f"Failed to copy {filename}: {str(e)}")

if __name__ == "__main__":
    base_dir = r'\\10.2.169.73\va_transfer\TDS\H191418\DailyQA\6DoF Daily QA'
    base_dest_dir = r'\\ceinvfs03s\shared\Rad_Oncology\Shared\PATIENTS\Stereotactic\Treatment Day Stereo QA\2024'
    today_date_str = datetime.now().strftime('%Y%m%d')
    today_dest_dir = os.path.join(base_dest_dir, f"{today_date_str}_TB1418")

    if not os.path.exists(today_dest_dir):
        os.makedirs(today_dest_dir, exist_ok=True)

    today_source_dir = find_today_folder(base_dir)
    if today_source_dir:
        copy_files(today_source_dir, today_dest_dir)
        wl = WinstonLutz(today_dest_dir)
        wl.analyze(bb_size_mm=10)
        pdf_path = os.path.join(today_dest_dir, "WL_TB1418.pdf")
        wl.publish_pdf(pdf_path)
        print(f"Published Winston Lutz analysis PDF at: {pdf_path}")
    else:
        print(f"No suitable source directory found today in {base_dir}")
#Pause to run script on 4315 machine
        import os
import shutil
from datetime import datetime, date
from pylinac import WinstonLutz

def has_relevant_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filename.startswith('RI') and os.path.getsize(filepath) in range(804 * 1024 - 100, 804 * 1024 + 100):
            return True
    return False

def find_today_folder(base_dir):
    today = date.today()
    for entry in os.scandir(base_dir):
        if entry.is_dir():
            creation_time = os.path.getctime(entry.path)
            folder_date = date.fromtimestamp(creation_time)
            if folder_date == today and has_relevant_files(entry.path):
                return entry.path
    return None

def copy_files(source_dir, dest_dir):
    if not source_dir:
        return
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        if filename.startswith('RI') and os.path.getsize(filepath) in range(804 * 1024 - 100, 804 * 1024 + 100):
            try:
                shutil.copy2(filepath, os.path.join(dest_dir, filename))
                print(f"Copied: {filename}")
            except Exception as e:
                print(f"Failed to copy {filename}: {str(e)}")

if __name__ == "__main__":
    base_dir = r'\\10.2.169.73\va_transfer\TDS\H194315\DailyQA\6DoF Daily QA'
    base_dest_dir = r'\\ceinvfs03s\shared\Rad_Oncology\Shared\PATIENTS\Stereotactic\Treatment Day Stereo QA\2024'
    today_date_str = datetime.now().strftime('%Y%m%d')
    today_dest_dir = os.path.join(base_dest_dir, f"{today_date_str}_TB4315")

    if not os.path.exists(today_dest_dir):
        os.makedirs(today_dest_dir, exist_ok=True)

    today_source_dir = find_today_folder(base_dir)
    if today_source_dir:
        copy_files(today_source_dir, today_dest_dir)
        wl = WinstonLutz(today_dest_dir)
        wl.analyze(bb_size_mm=10)
        pdf_path = os.path.join(today_dest_dir, "WL_TB4315.pdf")
        wl.publish_pdf(pdf_path)
        print(f"Published Winston Lutz analysis PDF at: {pdf_path}")
    else:
        print(f"No suitable source directory found today in {base_dir}")
