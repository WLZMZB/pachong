import csv

with open('../demo.csv', 'a+') as file:
    writer = csv.writer(file)
    # 一次写一行
    writer.writerow('')
    # 一次写多行
    # writer.writerows()
