p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("enter:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam")
else:
   print("not a spam")
