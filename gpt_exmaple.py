import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.rand(10,10)

# Create the heatmap
plt.imshow(data, cmap='hot')

# Add a color bar
plt.colorbar()

# Show the plot
plt.show()