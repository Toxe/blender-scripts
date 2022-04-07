import bpy


def local_to_global_coords(obj, local_coords):
    return obj.matrix_world @ local_coords


def global_to_local_coords(obj, global_coords):
    return obj.matrix_world.inverted() @ global_coords


def object_info(obj):
    print("Object:", obj.name)
    print("  Location:", obj.location)
    print("  Dimensions:", obj.dimensions)
    print("  Vertices:", len(obj.data.vertices))

    if len(obj.data.vertices) > 0:
        for vert in obj.data.vertices:
            global_coords = local_to_global_coords(obj, vert.co)
            print(f"    Vertex #{vert.index}:")
            print(f"      local: {vert.co}")
            print(f"      global: {global_coords}")
            print(f"      local --> global --> local: {global_to_local_coords(obj, global_coords)}")


object_info(bpy.context.active_object)
