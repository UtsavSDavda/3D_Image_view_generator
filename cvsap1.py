import trimesh
import numpy as np
import matplotlib.pyplot as plt
def save_model(filepath):
    mesh = trimesh.load(filepath)
    vertices = mesh.vertices
    faces = mesh.faces
    vertices_xy = vertices[:, :2]
    return vertices_xy, faces

def floor_plan(vertices, faces):
    plt.figure(figsize=(10, 8))
    for face in faces:
        polygon = vertices[face]
        polygon = np.vstack([polygon, polygon[0]])
        plt.plot(polygon[:, 0], polygon[:, 1], 'k-')
    plt.title('Top View of 3D Model')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

filepath = 'path_to_file'
vertices_xy, faces = save_model(filepath)
floor_plan(vertices_xy, faces)



