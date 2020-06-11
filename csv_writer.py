import csv

with open('Tile_position.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tile", "Xindex", "Yindex"])
    writer.writerow([1,0,1])
    writer.writerow([2,0,0])
    writer.writerow([3,2,0])
    writer.writerow([4,2,1])
    writer.writerow([5,2,2])
    writer.writerow([6,1,1])
    writer.writerow([7,0,2])
    writer.writerow([8,1,0])
    writer.writerow([9,1,2])
