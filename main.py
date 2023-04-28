from classes.save_to_csv import SaveToCsv
from classes.file_processing import FileProcessing


if __name__ == '__main__':
    directory = 'traininghihi'
    process = FileProcessing()
    processed_data = process.process_directory(directory)