def read_points():
    points = []
    line = input().strip()
    while line:
        x, y, z = map(int, line.split())
        points.append((x, y, z))
        line = input().strip()
    if not points:
        print("Nenhum ponto foi lido - A primeira linha lida estava vazia!!!")
    return points

def read_sphere():
    x, y, z, r = map(int, input().split())
    return (x, y, z), r

def is_inside(point, center, radius):
    x, y, z = point
    cx, cy, cz = center
    return (x - cx)**2 + (y - cy)**2 + (z - cz)**2 <= radius**2

def print_points(points):
    print("Listagem dos Pontos Lidos:")
    for point in points:
        print(point)
    print("Fim da Listagem")

def print_points_inside_sphere(points, center, radius):
    inside_points = [point for point in points if is_inside(point, center, radius)]
    print(f"Listagem dos Pontos Dentro da Esfera ({center}, {radius}:)")
    for point in inside_points:
        print(point)
    print("Fim da Listagem dos Pontos Dentro da Esfera")

def main():
    points = read_points()
    if points:
        sphere_center, sphere_radius = read_sphere()
        print_points(points)
        print_points_inside_sphere(points, sphere_center, sphere_radius)

if __name__ == '__main__':
    main()
