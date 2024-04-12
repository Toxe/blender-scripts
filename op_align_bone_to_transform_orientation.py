import bpy


def main(context):
    # place bone at cursor
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    # rotate bone
    head_pos = context.active_bone.head.copy()
    bpy.ops.transform.translate(
        value=(0, 0, 1),
        orient_type=context.scene.transform_orientation_slots[0].type,
        constraint_axis=(False, False, True),
    )
    context.active_bone.tail = context.active_bone.head.copy()
    context.active_bone.head = head_pos

    # transpose transform orientation to get global X axis vector
    custom_orientation = context.scene.transform_orientation_slots[0].custom_orientation
    global_x_axis_vector = custom_orientation.matrix.transposed().row[0]

    # move cursor +1.0 along transform orientation X axis
    context.scene.cursor.location += 1.0 * global_x_axis_vector

    # recalculate bone roll so that bone Z axis will point towards the cursor
    bpy.ops.armature.calculate_roll(type="CURSOR")


class AlignBoneToTransformOrientationOperator(bpy.types.Operator):
    """Align bone rotation and roll to transform orientation."""

    bl_idname = "object.align_bone_to_transform_orientation_operator"
    bl_label = "Align Bone to Transform Orientation"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {"FINISHED"}


def menu_func(self, context):
    self.layout.operator(
        AlignBoneToTransformOrientationOperator.bl_idname, text=AlignBoneToTransformOrientationOperator.bl_label
    )


# register and add to the "object" menu (required to also use F3 search "Align Bone to Transform Orientation" for quick access)
def register():
    bpy.utils.register_class(AlignBoneToTransformOrientationOperator)
    bpy.types.VIEW3D_MT_armature_context_menu.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AlignBoneToTransformOrientationOperator)
    bpy.types.VIEW3D_MT_armature_context_menu.remove(menu_func)


if __name__ == "__main__":
    register()
