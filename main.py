from classes.save_to_csv import SaveToCsv
from utils.file_processing import FileProcessing


if __name__ == '__main__':
    directory = 'traininghihi'
    process = FileProcessing()
    processed_data = process.process_directory(directory)
    save = SaveToCsv()
    save.save_to_csv(processed_data)