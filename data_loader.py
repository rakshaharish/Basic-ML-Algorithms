import csv
def read_data(filename):
    with open(filename,'r') as csvfile:
        datareader=csv.reader(csvfile,delimiter=',')
        header=next(datareader)
        metadata=[]
        traindata=[]
        for name in header:
            metadata.append(name)
            for row in datareader:
                traindata.append(row)
    return (metadata,traindata)
