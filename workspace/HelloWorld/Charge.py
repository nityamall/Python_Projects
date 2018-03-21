country=input("Which country are u from ?").upper()
tc=input("What is ur total charge ?")
tc=int(tc)
gst=0
pc=0
if(country == "INDIA"):
    prov=input("What is ur province ?").lower()
    if(prov =="kolkata"):
        gst=5/100*tc
        tc=tc+gst
        print("Total cost -:%d"%tc)
    elif(prov =="delhi" or prov =="punjab" or prov =="kashmir" or prov =="himachal pradhesh"):
        gst=13/100*tc
        tc=tc+gst
        print ("Total cost --> %d"%tc)
    else:
        gst=0.05/100*tc
        pc=0.06/100*tc
        tc=tc+gst+pc
        print("Total cost -> %f"%tc)
else:
    print("TAXES ARE NOT CHARGED")
    print("Total cost --> %d"%tc)
print(" Challenge Done Successfully !!! Nitya Mall")