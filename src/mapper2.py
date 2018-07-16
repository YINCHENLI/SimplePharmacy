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
    key, value = line.split('\t', 1) 
    drug, name = key.split('&')
    print('%s\t%s' % (drug, value))
