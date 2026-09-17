coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[6,7]]
for i in range(len(coordinates)-1):
    if coordinates[i][0]+1==coordinates[i+1][0] or coordinates[i][0]==coordinates[i+1][0]:
        pass
    else:
        print("False")
        break