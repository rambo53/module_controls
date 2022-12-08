import os
from app import app

def get_filename(file):
    filename, file_extension = os.path.splitext(file)
    return filename


def get_file_extension(file):
    filename, file_extension = os.path.splitext(file)
    return file_extension
    

def create_directory(new_file):
    
    repo = os.path.expanduser("~")
    directory_controls = os.path.join(repo, app.config["DIRECTORY_NAME"])
    directory_file = os.path.join(directory_controls, get_filename(new_file.filename))

    if not os.path.exists(directory_file):
        os.mkdir(directory_file)
        os.chdir(directory_file)
        os.mkdir('in')
        os.mkdir('out')
    
    new_file.save(os.path.join(directory_file, 'in', new_file.filename))

    return os.path.join(directory_file, 'in', new_file.filename)


