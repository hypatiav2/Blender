import bpy
import random
import math


# Set the frame rate to 24 frames per second
bpy.context.scene.render.fps = 24

# Set the start and end frames of the animation
start_frame = 1
end_frame = 240

# Set the initial position of the spheres
num_spheres = 27
radius = 3
angle = 0.0

# Add 50 glowing spheres
for i in range(num_spheres):
    # Calculate the position of the sphere
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    z = - i * 0.15 + 4

    # Create a new sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.2, location=(x, y, z))
    sphere = bpy.context.object

    # Get a random color
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)

    # Set the material properties of the sphere
    mat = bpy.data.materials.new(name="Material")
    mat.diffuse_color = (r, g, b, 1)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = (r, g, b, 1)  # Set the diffuse color to the random color
    bsdf.inputs[17].default_value = 10  # Set the specular intensity to 10
    bsdf.inputs[18].default_value = 0.5  # Set the roughness to 0.5
    bsdf.inputs[19].default_value = (r, g, b, 1)
    bsdf.inputs[20].default_value = 2  # Set the emission strength to 5

    # Assign the material to the sphere
    bpy.context.object.data.materials.append(mat)

    # Animate the sphere
    for frame in range(start_frame, end_frame + 1):
        angle += math.pi / 24  # Increment the angle by a small amount each frame
        x = radius * math.cos(angle)  # Calculate the new x-coordinate of the sphere
        y = radius * math.sin(angle)  # Calculate the new y-coordinate of the sphere
        sphere.location[0] = x  # Set the x-coordinate of the sphere
        sphere.location[1] = y  # Set the y-coordinate of the sphere
        sphere.keyframe_insert(data_path="location", frame=frame)

    # Update the radius and angle for the next sphere
    radius -= 0.1
    angle += math.pi / 4

# Set the start and end frames of the animation
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

