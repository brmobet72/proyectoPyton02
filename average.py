import read_csv
import charts

data=read_csv.read_csv('./Proyecto/data.csv')
data=list(filter(lambda item:item['Continent']=='North America',data))
average_date=list(map(lambda item:float(item['World Population Percentage']!=0), data))
country=list(map(lambda item:item['Country/Territory'], data))
charts.generater_pie_chart(country, average_date)