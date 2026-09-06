import os
import zipfile

def create_zip():
    zipf = zipfile.ZipFile('AlFalah-Full-Source.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('.'):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in ['.gradle', 'build', 'node_modules', '.git', 'public', 'builds', 'backend', 'scripts']]
        for file in files:
            if file.endswith('.apk') or file.endswith('.zip') or file.startswith('AlFalah-Full-Source'):
                continue
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, '.'))
    zipf.close()

create_zip()
