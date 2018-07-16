import sys  
  
current_drug = None
current_cost = None
  
for line in sys.stdin:  
    line = line.strip()  
    drug, cost = line.split('\t',1)  
    try:  
        cost = float(cost)  
    except ValueError:  
        continue  
    if current_drug == drug:  
        current_cost += cost
    else:  
        if current_drug:  
            print('%s\t%s' % (current_drug, current_cost))  
        current_drug = drug  
        current_cost = cost 
  
if current_drug == drug:  
    print('%s\t%s' % (current_drug, current_cost)) 