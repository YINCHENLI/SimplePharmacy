import sys  

'''
String line = value.toString();//
String[] drugs = line.split("\t");//use ',' to seperate
String[] prescriberNumAndCosts = drugs[1].split(",");

double costSum = Double.parseDouble(prescriberNumAndCosts[1]);

StringBuilder sb = new StringBuilder();
sb.append(drugs[0]);//drug name
sb.append(":");
sb.append(prescriberNumAndCosts[0]);//num of prescribers

context.write(new DoubleWritable(costSum), new Text(sb.toString().trim()));
'''
for line in sys.stdin:  

    line = line.strip()
    drugs = line.split(",")
    if drugs[0] == 'id':
        continue
    name = drugs[1] + '-' + drugs[2]
    print('%s\t%s' % (drugs[3] + '&' + name, drugs[4]))
