class SaveToCsv():
    def __init__(self):
        self.data = []
        

    def save_to_csv(self, data: dict):
        self.data.append(data)
        with open('data.csv', 'w') as f:
            for key in data.keys():
                f.write(
                    "%s,%s," % (key, data[key])
                )
            f.write('\n')

    def create_headers(self):
        with open('data.csv', 'w') as f:
            f.write(
                "business_name,business_address,total,date,"
            )
            f.write('\n')