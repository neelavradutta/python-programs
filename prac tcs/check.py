
coordinates = [[0,0],[0,1],[0,-1]]
for i in range(len(coordinates)-1):
    if coordinates[i][0]+1==coordinates[i+1][0] or coordinates[i][0]==coordinates[i+1][0]:
        pass
    else:
        print("False")
        break

print(sorted(coordinates))