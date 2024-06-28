import numpy as np
import os
import json

# Generate a random 3D image for demonstration purposes
image = np.random.rand(512, 216, 51)

# Create a directory to store the slices
os.makedirs('data', exist_ok=True)

# Save each slice as a JSON file
for i in range(image.shape[2]):
    slice_data = image[:, :, i].tolist()  # Convert to list for JSON serialization
    with open(f'data/slice_{i + 1}.json', 'w') as f:
        json.dump(slice_data, f)
