Number = int(input("Entre Number :"))
if Number % 3 == 0 and Number % 2 == 0 :
    print("BOTH")
elif Number % 3 == 0 or Number % 2 == 0 :
    print("ONE")
elif Number % 3 == 1 and Number % 2 == 1 :
    print("NEITHER")
