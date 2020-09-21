# When we use else with for loop, the control goes to else loop only if the for loop is executed properly.

khana=["roti","chawal","rice"]
for i in khana:
    print(i)

else:
    print("This for loop ended properly")

##########################
print("Program2")
khana1=["roti","chawal","rice"]
for i in khana1:
    print(i)
    break
else:
    print("This for loop did not end properly")

############################
print("Program3")
khana=["roti","chawal","rice"]
for i in khana:
    if i == "Karela" :
        break

else:
    print("This for loop ended properly")

############################
print("Program4")
khana=["roti","chawal","rice"]
for i in khana:
    if i == "roti" :
        break
else:
    print("This for loop not ended properly")