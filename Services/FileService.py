import pandas as pd

fileName = 'MessageFile.csv'  #Dosya Aynı proje içerisinde, istenirse başka bir path verilerek okunabilir
def readCsvFile():
    data = pd.read_csv(fileName,encoding = 'ISO-8859-9')
    data_dict = data.to_dict('list')
    phoneNumbers = data_dict['Phone Number']
    messages = data_dict['Message']
    userData = zip(phoneNumbers,messages)
    return userData


