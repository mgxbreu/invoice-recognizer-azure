from consts import headers
import csv

class SaveToCsv():
    def __init__(self):
        self.data = []
        
    def save_to_csv(self, data: dict):
        self.data.append(data)
        with open('data.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    
    def write_row(self, row):
        with open('data.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            
            if f.tell() == 0:
                writer.writeheader()

            writer.writerow(row)
        