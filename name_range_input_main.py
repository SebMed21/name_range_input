# create five list arrays
range_1 = []
range_2 = []
range_3 = []
range_4 = []
range_5 = []

# create while loops
while True:
        # in the while loop prompt the user to input numbers
        try:
            number = int(input("Please enter a number : (1-50)"))

            # append the correct numbers into the corresponding list
            if number >= 1 and number <= 10:
                range_1.append(number)
                print("yes")
                
            elif number >= 11 and number <= 20:
                range_2.append(number)
                print("yes")
                
            elif number >= 21 and number <= 30:
                range_3.append(number)
                print("yes")

            elif number >= 31 and number <= 40:
                range_4.append(number)
                print("yes")

            elif number >= 41 and number <= 50:
                range_5.append(number)
                print("yes")

            # if the user inputs an incorrect number break the loop
            elif number <= 0 or number >= 51:
                break   

        except:
            break

            #print(f"1 to 10: {range_1}")
            #print(f"11 to 20: {range_2}")
            #print(f"21 to 30: {range_3}")
            #print(f"31 to 40: {range_4}")
            #print(f"41 to 50: {range_5}")
