import os
import shutil

file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico', '.raw', '.psd', '.heic'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages', '.md'],
    'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
    'presentations': ['.ppt', '.pptx', '.odp', '.key'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg'],
    'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso', '.dmg'],
    'code': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.rb', '.go'],
    'executables': ['.exe', '.msi', '.app', '.deb', '.rpm', '.apk'],
    'ebooks': ['.epub', '.mobi', '.azw', '.pdf', '.fb2'],
    'fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    'data': ['.json', '.xml', '.yaml', '.sql', '.db', '.csv'],
    '3d': ['.3mf', '.stl', '.step', '.gcode']
}

def organize_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if ext in extensions:
                    folder = os.path.join(path, category)
                    os.makedirs(folder, exist_ok=True)
                    src = os.path.join(path, file)
                    dst = os.path.join(folder, file)
                    shutil.move(src, dst)
                    moved = True
                    break
            if not moved:
                unknown_folder = os.path.join(path, "unknown")
                os.makedirs(unknown_folder, exist_ok=True)
                src = os.path.join(path, file)
                dst = os.path.join(unknown_folder, file)
                shutil.move(src, dst)

path = input("Directory to clean: ")
organize_files(path)
