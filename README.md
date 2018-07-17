# Simple Pharmacy

This is a pipe similation of two MapReduce Jobs:

1. The first job sum up the costs for drugs
2. The second job count the unique users.

The sorting of the key is writen in shell which takes advantage of linux envirnment of sorting.

```
#pipe simulation
cat ./input/de_cc_data.txt | python ./src/mapper1.py | sort -t $'\t' -k1,1 | python ./src/reducer1.py | python ./src/mapper2.py | sort -t $'\t' -k1,1 | python ./src/reducer2.py | sort -t $',' -k3rn >> ./output/top_cost_drug.txt
```

There is another java + hadoop + hdfs version that can be run on clusters in my another repo:

<https://github.com/YINCHENLI/InsightDataPharmacy>
