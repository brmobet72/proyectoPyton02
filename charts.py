import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fig, ax=plt.subplots()
  ax.bar(labels, values)
  plt.show()
def generater_pie_chart(labels,values):
  fig, ax=plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

def genrate_line_chart(labels,values):
  fig, ax=plt.subplots()
  ax.plot(labels,values)
  plt.show()
  
if __name__=='__main__':
  labels = ['a','b','c']
  values =[10,40,50]
  genrate_line_chart(labels,values)