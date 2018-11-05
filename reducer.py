inputFile = open("mapper_output.txt", "r")
outputFile = open("joboutput", "w")
total_sales = 0
prev_key = None
type = None
item_list = []
price_list = []

for curr in inputFile:
        data = curr.strip().split("\t")
        if(len(data)!=2):
                continue
        item, price = data
        if prev_key and prev_key != item: item_list.append(prev_key);price_list.append(total_sales);prev_key = item;total_sales = 0
        prev_key = item
        total_sales += float(price)

if prev_key != None:
        item_list.append(prev_key)
        price_list.append(total_sales)

toys_container=[]
consumer_container=[]

for i in range(len(item_list)):
    if(item_list[i]=="Toys"):
        toys_container.append(price_list[i])
    else:
        consumer_container.append(price_list[i])

outputFile.write("Toys Total = %.2f \nConsumer Electronics = %.2f" % (sum(toys_container), sum(consumer_container)))
