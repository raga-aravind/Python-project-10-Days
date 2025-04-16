"""
Speeding Ticket Fines
Create a program that calculates fines based on a car's speed:
If speed > 120, print "Hefty fine of $500".
If speed > 100, print "Fine of $200".
If speed > 80, print "Fine of $100".
Otherwise, print "No fine, drive safely!"
"""

print("Speeding Ticket Fines")
speed = int(input("Enter The Car speed in km : "))
if speed > 120:
    print("Hefty fine of Rs:500")
elif speed >100:
    print("Fine of Rs:200")
elif speed > 80:
    print("Fine of Rs:100")
else:
    print("No fine, drive safely!")