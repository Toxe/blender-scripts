import bpy
from mathutils import Vector


def local_to_global_coords(obj, local_coords):
    return obj.matrix_world @ local_coords


def global_to_local_coords(obj, global_coords):
    return obj.matrix_world.inverted() @ global_coords


def set_cursor_to_last_vertex(obj):
    # last vertex
    vert = obj.data.vertices[-1]

    # local coordinates, Z +1 above last vertex
    local_coords = vert.co + Vector([0, 0, 1])

    # move cursor
    global_coords = local_to_global_coords(obj, local_coords)
    bpy.context.scene.cursor.location = global_coords

    print(f"move cursor to vertex #{vert.index} --> {global_coords}")


set_cursor_to_last_vertex(bpy.context.active_object)
