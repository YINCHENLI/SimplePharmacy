#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
echo "drug_name,num_prescriber,total_cost" > ./output/top_cost_drug.txt
cat ./input/de_cc_data.txt  | python ./src/mapper1.py | sort -t $'\t' -k1,1 | python ./src/reducer1.py | python ./src/mapper2.py | sort -t $'\t' -k1,1 | python ./src/reducer2.py | sort -t $',' -k3rn >> ./output/top_cost_drug.txt