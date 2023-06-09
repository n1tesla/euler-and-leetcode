from math import comb
def lattice_path(grid_size):
    return comb(grid_size*2,grid_size)

if __name__=='__main__':
    print(lattice_path(20))
