class Analysis:
    
    def __init__(self,dataframe):
        self.data = dataframe
        print('Dataframe recvied = {}'.format(type(self.data)))

    def null_values(self):
        y = self.data.isnull().values.sum()
        return y

    def number_rows_columns(self):
        a = self.data.shape[0]
        b = self.data.shape[1]
        return a,b

    def size_dataset(self):
        size = self.data.size 
        return size

    def column_dtype(self):
        types = self.data.dtypes
        return types

    def duplicates(self):
        a = self.data.duplicated().sum()
        return a
