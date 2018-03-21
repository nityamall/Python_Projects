def hp_calc(age,apples_eaten,cigg_smoked):
    answer=(100-age)+(apples_eaten*3.5)-(cigg_smoked*2)
    print("%f"%answer)
sayan=[21,4,3]
hp_calc(sayan[0],sayan[1],sayan[2])
hp_calc(*sayan)
