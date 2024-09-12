import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaların listesi 
points = [(1, 2), (3, 5), (6, 8), (9, 12), (4, 7)]

# Mesafeleri saklamak için bir liste
distances = []

# Her bir nokta çifti arasındaki mesafeyi hesaplayan döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Sonuç
min_distance = min(distances)
print(f"Minimum Öklid Mesafesi: {min_distance}")
