def textfile_grabber(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()

    return log_content
