# Queen - Woman = property_1

# Apples - Apple = property_2

# Apple + property1 = X ? -- What word is most similar?



# Import database and libraries
# import sample_vecetors
import numpy as np

# with open('sample_vectors.txt', 'r') as file:
#         vectors = file.read()
#         print(vectors)

# Read in database as numpy vectors
# vectors = np.loadtxt('sample_vecetors.txt', dtype='str').astype(np.float32)

# Create vector array for each word

Man = np.array([1.0, 0.0, 0.0], dtype='str').astype(np.float32)
King = np.array([1.0, 1.0, 0.0], dtype='str').astype(np.float32)

Woman = np.array([0.0, 0.0, 1.0], dtype='str').astype(np.float32)
Queen= np.array[(np.array(King - Man))]

print(Queen)

# measure properties (differences between words)

# Find differences between words with cosine similarity (this is property_X)



# Find most similar word to property_X

