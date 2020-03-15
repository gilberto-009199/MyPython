# -*- coding: utf-8 -*-
monica = int(input());
filhoA = int(input());
filhoB = int(input());

filhoC = monica - (filhoA + filhoB);

if filhoA > filhoB and filhoA > filhoC:
    print("%.0f"% filhoA);
if filhoB > filhoC and filhoB > filhoA :
    print("%.0f"% filhoB);
if filhoC > filhoA and filhoC > filhoB :
    print("%.0f"% filhoC);