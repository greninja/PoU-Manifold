Code for an approach to smoothly patch together charts(given) of a manifold to give a global structure

## Files description:

## Partition of unity description with diagram

A partition of unity is a useful, though technical, tool that helps us work in local coordinates. This can be a tricky matter when we’re doing things all over our manifold, since it’s almost never the case that the entire manifold fits into a single coordinate patch. A (smooth) partition of unity is a way of breaking the function with the constant value 1 up into a bunch of (smooth) pieces that will be easier to work with.

PoU subordinate to an open cover

## Spherical Dataset description

We have taken patches/ overlapping charts s.t. atmost '4' patches overlap at any given point.

![Alt text](/home/shadab/python/PoU-Manifold/src/spherical_dataset.png?raw=true)

## Global approximation

## Our approach:

# We explored with using C-inf smooth Bump Functions instead of 'pyramid (max{0, r-(c-x)})' "A Dimension Reduction Technique for Local Linear Regression" by Joseph Lucas

# We take the patches to be charts of a manifold, collectively forming a smooth atlas, which are discs in R^2.

# # We have created individual charts from the dataset
