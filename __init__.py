import datetime
import leather
import csv


chartData=[]
with( open("../data/sample-prices.csv")) as csvFile:
    reader = csv.DictReader( csvFile )
    for row in reader:
        date = datetime.datetime.strptime( row["Date"], "%Y-%m-%d").date()
        chartData.append( (date, float( row["Close"] )))


chart = leather.Chart('sample-data')
chart.add_line(chartData)
chart.to_svg('/tmp/sample-data.svg')
