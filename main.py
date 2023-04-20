from classes.recognize_invoice import RecognizeInvoice
from classes.save_to_csv import SaveToCsv

if __name__ == '__main__':
    sample = RecognizeInvoice()
    sample.recognize_invoice()
    info = sample.get_info()
    save = SaveToCsv()
    save.save_to_csv(info)
    print(info)