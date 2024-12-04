###  A transport company charges the fare according to following table: Distance Charges 1-50 8 Rs./Km 51-100 10 Rs./Km > 100 12 Rs/Km===============

distance=float(input("Enter the distance covered in KM : "))
if distance>=1 and distance<=50:
    fare=distance*8
elif distance>=51 and distance<=100:
    fare=distance*10
elif distance>100:
    fare=distance*12
else:
    print(f"Invalid distance {distance}KM . should be greater than 0")
if fare>0:
    print(f"total distance covered {distance}KM and price is RS.>> {fare} ")
