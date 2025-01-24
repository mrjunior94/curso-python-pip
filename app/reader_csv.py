import csv


def reader_csv(path):
  with open(path, encoding = "utf8", errors= 'ignore' ) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader: 
      iterable = zip(header, row)
      country_dict = dict((iterable))
      data.append(country_dict)
    return data 

if __name__ == '__main__':
  data = reader_csv('data.csv')
  print(data)