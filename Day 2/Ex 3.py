# get input for 5 subject add all of it and find average. avg<35 - additional detail required else good to go
print("Students Mark Details - Maximum Mark 100")
maths = int(input("Enter Maths Mark: "))
social = int(input("Enter Social Mark: "))
science = int(input("Enter Science Mark: "))
tamil = int(input("Enter Tamil Mark: "))
english = int(input("Enter English Mark: "))
total = (maths+social+science+tamil+english)/5
print(f"Total Mark: {total}")
if total <= 35:
    print("Additional Details Required")
else:
    print("you are good to go")