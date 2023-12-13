import zipfile
import os
import datetime

def create_archive(source_dir, destination_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = os.path.join(destination_dir, f'backup_{timestamp}.zip')
    
    try:
        with zipfile.ZipFile(archive_name, 'w') as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, source_dir))
    except Exception as e:
        print(f"Error creating backup archive: {e}")
        return None
    
    print(f"Backup archive created: {archive_name}")
    return archive_name

# Replace these paths with your source and destination directories
source_directory = 'E:\Quickbooks Files'
destination_directory = r'\\casaos.local\\TheBookladyNE'

backup_file = create_archive(source_directory, destination_directory)
if backup_file:
    print("Backup creation completed successfully!")
else:
    print("Backup creation failed.")

input("Press Enter to exit...")
