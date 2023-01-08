import bpy

# Create a new scene

# Set the frame rate to 24 frames per second
bpy.context.scene.render.fps = 24

# Set the start and end frames of the animation
start_frame = 1
end_frame = 48



# Add a sphere to the scene
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5)
sphere = bpy.context.object
sphere.location = (0, 0, 1.5)

# Set the material properties of the objects
mat = bpy.data.materials.new(name="Material")
mat.diffuse_color = (1, 1, 1, 1)
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs[0].default_value = (1, 1, 1, 1)  # Set the diffuse color to white
bsdf.inputs[17].default_value = 10  # Set the specular intensity to 10
bsdf.inputs[18].default_value = 0.5  # Set the roughness to 0.5
bsdf.inputs[20].default_value = 6  # Set the emission strength to 5
bsdf.inputs[19].default_value = (1, 0.75, 0.5, 1)  # Set the diffuse color to white

sphere.data.materials.append(mat)

# Animate the lamp
for frame in range(start_frame, end_frame + 1):
    # Set the lamp to be fully lit at the start of the animation
    if frame == start_frame:
        sphere.scale = (1, 1, 1)
        sphere.keyframe_insert(data_path="scale", frame=frame)
    # Gradually turn off the lamp over the course of the animation
    else:
        sphere.scale[2] = 1 - (frame - start_frame) / (end_frame - start_frame)
        sphere.keyframe_insert(data_path="scale", frame=frame)
        bsdf.inputs[20].default_value -= 0.15
        bsdf.inputs[20].keyframe_insert(data_path="default_value",frame=frame)
