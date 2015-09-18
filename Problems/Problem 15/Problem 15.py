# Problem 15: paths through a grid

import scipy.special

def problem15(grid_size):
	
	return int(scipy.special.binom(2 * grid_size, grid_size))

if __name__ == '__main__': 
    print(problem15(20))