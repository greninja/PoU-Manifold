"""
The data points are uniformly distributed on a unit sphere.
To generate these 3-dimensional points, we first generate standard
normally distributed points as vectors lying in 3d space, and then
normalize these vectors (X:= X / ||X||) to make it lie on a sphere
(S^2) which acts as our manifold. 
"""
import numpy as np 

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec
"""
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))
"""
xi, yi, zi = sample_spherical(100)
data_points = []
map(lambda x,y,z : data_points.append((x,y,z)), xi,yi,zi)     
dictionary_datapoints = {k:np.array(v) for k,v in enumerate(data_points)}
chart1, chart2, chart3, chart4, chart5, chart6 = (dict() for _ in range(6))

def create_charts(dictionary_datapoints):
    """
    Creating the 6 charts of the sphere. This snippet maps 6 hemispheres
    homeomorphically to 6 different open regions in R^2 (discs). For e.g. :
    the maps (x, y, z) -> (x, y), and its inverse (x, y) -> 
    (x, y, squareroot(1-x^2-y^2)), are continuous maps from the open
    hemisphere (for which z <= 0) to open disk x^2 + y^2 < 1
    and from the open disk back to sphere (S^2), respectively.
    """    
    for i, point in dictionary_datapoints.iteritems():
        if point[2] > 0 :
            chart1[i] = point[:2] 
        else:
        	chart2[i] = point[:2]
        
        if point[1] > 0:
        	chart3[i] = point[::len(point)-1]
        else:
        	chart4[i] = point[::len(point)-1]
        
        if point[0] > 0:
        	chart5[i] = point[1:]
        else:
        	chart6[i] = point[1:]

create_charts(dictionary_datapoints)

dictionary_of_charts = {
    'chart1' : chart1,
    'chart2' : chart2,
    'chart3' : chart3,
    'chart4' : chart4,
    'chart5' : chart5,
    'chart6' : chart6,
}

