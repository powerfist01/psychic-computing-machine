import pandas as pd

class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_get_structured_data(self):
        
        structured_data = []
        df = pd.read_excel(self.file_path, )

        for _, row in df.iterrows():

            description = row.get('description')
            quantity = row.get('quantity')
            amount = row.get('amount')
            category = row.get('category')

            structured_data.append({
                'description': description,
                'quantity': quantity,
                'amount': amount,
                'category': category
            })

        return structured_data
    