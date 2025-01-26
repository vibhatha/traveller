import pyarrow.csv as pv


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.table = None

    def load_data(self):
        try:
            self.table = pv.read_csv(self.file_path)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")

    def get_data(self):
        if self.table is not None:
            return self.table
        else:
            print("Data not loaded. Please call load_data() first.")
            return None
