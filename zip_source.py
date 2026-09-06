import os
import zipfile

def create_zip():
    zipf = zipfile.ZipFile('AlFalah-Full-Source.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('.'):
        # Exclude unnecessary directories
        dirs[:] = [d for d in dirs if d not in ['.gradle', 'build', 'node_modules', '.git']]
        for file in files:
            if file == 'AlFalah-Full-Source.zip' or file == 'zip_source.py':
                continue
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, '.'))
    zipf.close()

create_zip()
