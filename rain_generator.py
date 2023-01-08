import bpy
import random

# Set the frame rate to 24 frames per second
bpy.context.scene.render.fps = 24

# Set the start and end frames of the animation
start_frame = 1
end_frame = 80

# Set the number of droplets to create
num_droplets = 100

# Set the material properties of the droplet
mat = bpy.data.materials.new(name="Material")
mat.use_nodes = True
mat.diffuse_color = (1, 1, 1, 1)
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs[0].default_value = (1, 1, 1, 1)  # Set the diffuse color to white
bsdf.inputs[17].default_value = 10  # Set the specular intensity to 10
bsdf.inputs[18].default_value = 0.5  # Set the roughness to 0.5
bsdf.inputs[20].default_value = 5  # Set the emission strength to 5

# Create the droplets
for i in range(num_droplets):
    # Create a droplet object
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=0.1)
    droplet = bpy.context.object

    # Set the initial position of the droplets
    x_pos = random.uniform(-10, 10)
    y_pos = random.uniform(-10, 10)
    z_pos = random.uniform(10, 20)

    # Set the initial position and orientation of the droplet
    droplet.location = (x_pos, y_pos, z_pos)
    droplet.rotation_euler = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    droplet.keyframe_insert(data_path="location", frame=start_frame)
    droplet.keyframe_insert(data_path="rotation_euler", frame=start_frame)

    # Animate the droplet falling
    for frame in range(start_frame, end_frame + 1):
        # Set the droplet to its initial position at the start of the animation
        if frame == start_frame:
            droplet.location = (x_pos, y_pos, z_pos)
            droplet.keyframe_insert(data_path="location", frame=frame)
        # Gradually move the droplet downward
        else:
            droplet.location[2] -= 1
            droplet.keyframe_insert(data_path="location", frame=frame)

    # Randomize the color and emission strength of the droplet
    mat.diffuse_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1)
    bsdf.inputs[20].default_value = random.uniform(5, 10)
    
    # Assign the material to the droplet
    droplet.data.materials.append(mat)
    
    # Shift the position of the next droplet slightly to the right

# Set the end frame of the animation
bpy.context.scene.frame_end = end_frame
