grid = [
    [1, 0, 1],
    [1, 0, 0],
    [0, 1, 1]]

grid = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 0],
    [0, 1, 1]]


#plan:
# while land
#   search for first land
#   check if land in any existing islands
#   start a new set of coords (tuples) with that land in i
#   check adjancent spots
# add adjacent spot to land mass
# recurse until land is dried up

land_masses = []
checked = set()

def main():
    """Search the grid"""
    for y, row in enumerate(grid):
        print y, row
        for x, plot in enumerate(row):
            print x, plot
            if plot:
                print 'found land'
                if not any([(x, y) in z for z in land_masses]):
                    mass = set()
                    land_masses.append(mass)
                    checked.add((x, y))
                    define_land_mass(x, y, mass)

def check(tup, mass):
    if tup not in checked:
        print 'checking', tup
        checked.add(tup)
    
        try:
            if grid[tup[1]][tup[0]]:
                define_land_mass(*tup, mass)
        except IndexError:
            pass
                
    

def define_land_mass(x, y, mass):
    """Given coords, add all adjacent unknown coords to land mass."""
    if grid[y][x]:
        mass.add((x, y))

    check((x + 1, y))
    check((x - 1, y))                
    check((x, y + 1))                
    check((x, y - 1))                
