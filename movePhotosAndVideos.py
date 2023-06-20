import os
import shutil
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring

def select_folder():
    Tk().withdraw()
    folder_path = askdirectory()
    return folder_path

def select_date():
    Tk().withdraw()
    date_str = askstring("Sélection de la date", "Veuillez entrer la date (au format jj-mm-aaaa) :")
    return date_str

def move_files(source_path, destination_path, start_date, end_date):
    start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
    end_date = datetime.strptime(end_date, '%d-%m-%Y').date()

    moved_files = []

    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            creation_date = datetime.fromtimestamp(os.path.getmtime(file_path)).date()

            if start_date <= creation_date <= end_date:
                destination_file_path = os.path.join(destination_path, file)
                shutil.move(file_path, destination_file_path)
                moved_files.append(destination_file_path)

    return moved_files

# Sélection du dossier source
print("Sélectionnez le dossier source :")
source_path = select_folder()

# Sélection du dossier de destination
print("Sélectionnez le dossier de destination :")
destination_path = select_folder()

# Entrée des dates
print("Sélectionnez la date de début :")
start_date = select_date()
print("Sélectionnez la date de fin :")
end_date = select_date()

# Déplacement des fichiers
moved_files = move_files(source_path, destination_path, start_date, end_date)
print(f"Total de fichiers déplacés : {len(moved_files)}")

# Ouvrir l'explorateur de fichiers dans le dossier de destination
os.startfile(destination_path)
