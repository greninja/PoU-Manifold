Code for an approach to smoothly patch together charts(given) of a manifold to give a global structure

## Files description :

- `bumpfunction.py`  : Consists a class containing the required smooth C-inf bump functions
- `create_charts.py` : Consists code to create individual charts of the manifold
- `main.py` 		 : Consists `main` function which computes the global approximated value for the dataset
- `regression.py` 	 : Consists a function used to fit linear curves to data using Ordinary Least Squares
- `visualization.py` : For visualizing spherical manifold and individual charts

## To run:

If you averse `.pyc` files:

```
cd src/
python -B main.py
```

## Partition of unity:

A partition of unity is a useful, though technical, tool that helps us work in local coordinates. This can be a tricky matter when we’re doing things all over our manifold, since it’s almost never the case that the entire manifold fits into a single coordinate patch. A (smooth) partition of unity is a way of breaking the function with the constant value 1 up into a bunch of (smooth) pieces that will be easier to work with.

PoU subordinate to an open cover

## Spherical Dataset description:

We have taken patches/ overlapping charts s.t. atmost '4' patches overlap at any given point.


## Global approximation

## Our approach:

- We explored with using C-inf smooth Bump Functions instead of 'pyramid (max{0, r-(c-x)})' "A Dimension Reduction Technique for Local Linear Regression" by Joseph Lucas

- We take the patches to be charts of a manifold, collectively forming a smooth atlas, which are discs in R^2.

- We have created individual charts from the dataset
