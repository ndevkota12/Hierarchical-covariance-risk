# Hierarchical-covariance-risk: Portfolio volatility risk calculator using covariance and hierarchy

# Hierarchy-Regularized Covariance Estimation for Robust Portfolio Risk

This repository studies a hierarchy-aware covariance estimator for portfolio risk
estimation. The method enforces tree-structured regularization using ultrametric
distances derived from hierarchical clustering.

## Motivation
Sample covariance matrices are noisy and unstable under limited data. Financial
assets exhibit latent hierarchical structure (sectors, macro drivers). Encoding
this structure improves out-of-sample risk estimation and portfolio stability.

## Method
We estimate the covariance matrix Σ by solving:

min ||Σ − S||_F² + λ Σ_{i≠j} d_T(i,j) |Σ_ij|

where S is the sample covariance and d_T(i,j) is the ultrametric distance between
assets i and j on a hierarchical tree.
