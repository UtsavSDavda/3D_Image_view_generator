# 3D_Image_view_generator
Generates various views from a 3D image.
Currently the code inputs a 3D image of various formats supported by Trimesh.
The code generates the top view of these images and shows it.
**How it works:**
The code inputs the 3D image via trimesh and generates faces and vertices out of it. (Formats of the image are the ones Trimesh supports like stl or obj.)
Vertices of the X-Y plane are filtered and taken for further processing.
The X-Y vertices are projected on a plane.
Matplotlib is used to draw out the top view using these vertices.
All the points are connected to each other via edges.
The final image is presented once done.

To use this code, just enter the image path in the code and run.
