Code to smoothly patch together local functions defined on charts (given) of a manifold to give a global approximation. 

## Files description :

- `bumpfunction.py`  : Consists of a class containing the required smooth C-inf bump functions
- `create_charts.py` : Consists code to create individual charts of the manifold
- `main.py` 		 : Consists of `main` function which computes the global approximated value using PoU
- `regression.py` 	 : Consists of a function used to fit linear/ polynomial curves to data using OLS
- `visualization.py` : For visualizing spherical manifold and individual charts

## To run:

If you averse `.pyc` files:

```
$ cd src/
$ python -B main.py
```

## Partition of unity:

A [partition of unity](https://en.wikipedia.org/wiki/Partition_of_unity) is a useful, though technical, tool that helps us work in local coordinates. This can be a tricky matter when we’re doing things all over our manifold, since it’s almost never the case that the entire manifold fits into a single coordinate patch. A (smooth) partition of unity is a way of breaking the function with the constant value 1 up into a bunch of (smooth) pieces that are easier to work with.

More precisely, for any covering of X (a topological space; here it is a manifold, which is a topological space with additional properties) by open subsets {Uₘ},there exists a sequence of smooth nonnegative functions {ϴₙ}, on X, called a partition of unity, subordinate to the [open cover](https://en.wikipedia.org/wiki/Cover_(topology)#Cover_in_topology) {Uₘ} such that for every point, x ∈ X :

- the sum of all function values at x is 1, i.e., ∑ ϴₙ(x) = 1

- 0 ≤ ϴₙ(x) ≤ 1 and all 'n'

- supp ϴₙ ⊆ Uₘ for each m, where 'supp' is the [support](https://en.wikipedia.org/wiki/Support_(mathematics)) of the function.

- The family of supports (supp ϴₙ) is locally finite, meaning that every point has a neighbourhood that intersects supp ϴₙ for only finitely many values of n

## Bump Functions:

A *bump function* is a function on Cartesian Space R^n, for some n ∈ R with values in the real numbers R

					b : R^n -> R  *such that*

1) **_b_** is smooth
2) **_b_** has compact support
 
## Global approximation

Partition of unity can be used to patch together local smooth objects into global ones.

## Approach:

- We have taken the smooth functions to be 3 smooth [Bump Functions](https://en.wikipedia.org/wiki/Bump_function)

- Here we are taking the sets in open cover to be coordinate charts of a manifold, collectively forming a smooth atlas, which are discs in R^2.

- We have created individual charts from the dataset

- We have fitted linear/ Polynomial curves, locally, on each chart. Plausible further work : Trying to approximate any other scalar valued function (R^n -> R)

## Spherical Dataset description:

We have taken patches/ overlapping charts such that atmost 4 patches overlap.

## Sample dataset:

[Spherical manifold dataset Image](./src/images/sphere_manifold.png)