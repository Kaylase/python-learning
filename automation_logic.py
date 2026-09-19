city = "Kyiv"
price = 12000
paid = False

if city == "Kyiv" and price > 10000:
    print("Send to manager")

elif not paid:
    print("Send payment reminder")

else:
    print("No action")
