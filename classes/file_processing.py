import os
from classes.recognize_invoice import RecognizeInvoice
from classes.translator import detect_language, translate
from classes.save_to_csv import SaveToCsv

class FileProcessing:
    def __init__(self):
        self.data = []

    def process_file(self, path):
        save = SaveToCsv()
        recognize_invoice = RecognizeInvoice(path)
        recognize_invoice.start_process()
        info = recognize_invoice.serialize_information()
        print(info)
        for key in info:
            if type(info[key] ) == str:
                language = detect_language(info[key])
                info[key] = translate(info[key], language)
        save.write_row(info)

    def process_directory(self, directory):
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                print("--------Recognizing invoice: {}--------".format(path))
                self.process_file(path)
            elif os.path.isdir(path):
                print("Exploring directory: ", path)
                self.process_directory(path)