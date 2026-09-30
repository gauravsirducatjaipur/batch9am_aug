total_unit = int(input("Enter the consumption unit "))
unit_price = 11
gst = 12


total_amount = total_unit * unit_price
gst_amount =(total_amount*12)/100
final_amount = total_amount + gst_amount

print("The total amount is ", total_amount)
print("The GST amount is ", gst_amount)
print("The final amount is ", final_amount)
