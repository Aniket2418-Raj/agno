import math

P = (4, 4)
points = [(9, 8), (5, 5), (7, 7), (10, 10), (6, 6)]

# Step 1: Compute distances using map + lambda
distances = list(
    map(lambda pt: round(math.sqrt((pt[0]-P[0])**2 + (pt[1]-P[1])**2), 2), points)
)
print(distances)

# Step 2: Filter points closer than a threshold
threshold = 6
closer_points = list(filter(lambda pt: math.sqrt((pt[0]-P[0])**2 + (pt[1]-P[1])**2) < threshold, points))

print("Points closer than", threshold, ":", closer_points)
