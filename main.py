from classes.file_processing import FileProcessing


if __name__ == '__main__':
    directory = 'resources/facturas'
    process = FileProcessing()
    processed_data = process.process_directory(directory)