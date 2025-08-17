import os
import time


def generate_log_filename():
    desktop = os.path.join(os.path.expanduser("~"), "Downloads")
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    return  os.path.join(desktop, f"folder_report_{timestamp}.txt")
