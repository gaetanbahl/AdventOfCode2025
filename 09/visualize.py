import matplotlib.pyplot as plt

with open("input", "r") as f:
    points = [(int(a), int(b)) for a, b in (line.split(",") for line in f.readlines())]

# Close the polygon by adding the first point at the end
xs = [p[0] for p in points] + [points[0][0]]
ys = [p[1] for p in points] + [points[0][1]]

plt.figure(figsize=(10, 10))
plt.plot(xs, ys, 'b-', linewidth=0.5)
plt.scatter([p[0] for p in points], [p[1] for p in points], s=1, c='red')
plt.gca().set_aspect('equal')
plt.title('Day 09 Input')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
