import time

bottle_of_beer = 99

while bottle_of_beer != 0:

    if bottle_of_beer == 2:
        print(str(bottle_of_beer) + " bottles of beer on the wall, " + str(bottle_of_beer) + " bottles of beer")
        bottle_of_beer -= 1
        print("Take one down and pass it around, " + str(bottle_of_beer) + " bottle of beer on the wall")
    elif bottle_of_beer == 1:
        print(str(bottle_of_beer) + " bottle of beer on the wall, " + str(bottle_of_beer) + " bottle of beer")
        bottle_of_beer -= 1
        print("Take one down and pass it around, no more bottles of beer on the wall")
    else:
        print(str(bottle_of_beer) + " bottles of beer on the wall, " + str(bottle_of_beer) + " bottles of beer")
        bottle_of_beer -= 1
        print("Take one down and pass it around, " + str(bottle_of_beer) + " bottles of beer on the wall.")
    time.sleep(5)

print("No more bottles of beer on the wall, no more bottles of beer")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")