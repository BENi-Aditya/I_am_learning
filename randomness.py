import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 0      # Mean (center)
sigma = 1   # Standard Deviation (spread)
sample_size = 10_000

# Generate normal distribution data
data = np.random.normal(loc=mu, scale=sigma, size=sample_size)

# Create histogram
plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(data, bins=50, density=True, 
                          alpha=0.7, color='skyblue',
                          edgecolor='black')

# Plot theoretical PDF (Probability Density Function)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2, label='Theoretical PDF')

# Format plot
plt.title(f"Normal Distribution\nμ={mu}, σ={sigma}, Samples={sample_size}")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(alpha=0.3)
plt.legend()
plt.show()