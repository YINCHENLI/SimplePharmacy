import sys  
  
current_drug = None
current_cost = None
current_num = 1

for line in sys.stdin:  
    line = line.strip()  
    drug, cost = line.split('\t', 1)
    try:  
        cost = float(cost)  
    except ValueError:  
        continue  
    if current_drug == drug:  
        current_cost += cost
        current_num = current_num + 1
    else:  
        if current_drug:  
            print('%s,%s,%.2f' % (current_drug, current_num, current_cost))  
        current_drug = drug  
        current_cost = cost 
        current_num = 1
 


if current_drug == drug:  
    print('%s,%s,%.2f' % (current_drug, current_num, current_cost))  
