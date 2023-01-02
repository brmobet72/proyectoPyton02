import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header= next(reader)
    data=[]
    for row in reader:
      iterable=zip(header,row)
      country_dict={key: value for key, value in iterable}
      data.append(country_dict)
    return data
def read_country(country):
  data=read_csv('./app/data.csv')
  result=list(item for item in data if item['Country/Territory']==country)
  return result
if __name__=='__main__':
  data=read_csv('./app/data.csv')
  print(data[0])
  result=read_country('Zimbabwe')
  print (result)