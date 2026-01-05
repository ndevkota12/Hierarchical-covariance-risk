import numpy as np

def hierarchical_covariance(S, tree_distances, lam):
    """
    Hierarchy-regularized covariance estimation using soft-thresholding.

    Solves:
        min ||Σ - S||_F^2 + λ Σ_{i≠j} d_T(i,j) |Σ_ij|

    Parameters
    ----------
    S : np.ndarray, shape (n,n)
        Sample covariance matrix.
    tree_distances : np.ndarray, shape (n,n)
        Ultrametric distance matrix d_T(i,j).
    lam : float
        Regularization strength.

    Returns
    -------
    Sigma_hat : np.ndarray, shape (n,n)
        Regularized covariance matrix.
    """
    n = S.shape[0]
    Sigma_hat = S.copy()

    for i in range(n):
        for j in range(n):
            if i != j:
                # soft-thresholding
                penalty = lam * tree_distances[i, j]
                if S[i, j] > penalty:
                    Sigma_hat[i, j] = S[i, j] - penalty
                elif S[i, j] < -penalty:
                    Sigma_hat[i, j] = S[i, j] + penalty
                else:
                    Sigma_hat[i, j] = 0.0
    return Sigma_hat
