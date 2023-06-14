# List comprehension 
# You are given three integers, x,y,z representing the dimensions of a cuboid along with an integer n. 
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of I+J+K != n. 

x=2
y=2
z=2
n=3
coordinates = [[i,j,k] for i in range(x + 1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n] 
print(coordinates)


