from backend.generate import generate
from backend.generate_log_filename import generate_log_filename
from backend.scan_folder import scan_folder
from backend.textfile_grabber import textfile_grabber

folder_path = r"insert here your own folder path"

log_file = scan_folder(folder_path)

log_content_before = textfile_grabber(log_file)

answer = input("Have you already executed your main.py script on the folder? (yes/no)")

if answer == 'yes':

    log_file_after = scan_folder(folder_path)

    log_content_after = textfile_grabber(log_file_after)

Python_Script_description = '''Insert here an accurate description of your Python script, what it does and what are its main functions'''

print(generate(log_content_before, log_content_after, Python_Script_description))



