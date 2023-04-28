from classes.save_to_csv import SaveToCsv
from utils import process_file, process_directory

data = []

if __name__ == '__main__':
    directory = 'facturas'
    process_directory(directory)
    save = SaveToCsv()
    save.save_to_csv(data)