# K-Means from Scratch

A compact educational implementation of K-means clustering using NumPy. The project generates a two-cluster synthetic dataset, assigns points to their nearest centroids, updates centroids iteratively, checks for convergence, and visualizes the result.

## How it works

1. `dataset.py` creates two groups of two-dimensional Gaussian points.
2. `kmeans.py` randomly initializes centroids and alternates between cluster assignment and centroid updates.
3. Training stops when the centroids converge or the iteration limit is reached.
4. `visualization.py` plots the labeled points and final centroids.

## Repository contents

| File | Purpose |
| --- | --- |
| `main.py` | Entry point for generation, clustering, and visualization |
| `dataset.py` | Synthetic data generator |
| `kmeans.py` | NumPy implementation of the K-means algorithm |
| `visualization.py` | Matplotlib cluster plot |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib
python main.py
```

The random generator is not seeded, so the samples, starting centroids, and final plot can differ between runs. This implementation assumes two-dimensional data and does not explicitly recover from an empty cluster.
