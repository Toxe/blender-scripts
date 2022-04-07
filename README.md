# Blender Scripts

## Operators

### Align Bone to Transform Orientation

Align bone to a custom transform orientation and recalculate roll so that the bone Z axis points along the custom orientation X axis.

[op_align_bone_to_transform_orientation.py](op_align_bone_to_transform_orientation.py)

- Select object face.  
  ![align_bone_to_transform_orientation_01.png](images/align_bone_to_transform_orientation_01.png)

- Create custom transform orientation ("Face" in this case) and keep it selected.  
  ![align_bone_to_transform_orientation_02.png](images/align_bone_to_transform_orientation_02.png)

- Snap (Shift-S) --> Cursor to Selected  
  ![align_bone_to_transform_orientation_03.png](images/align_bone_to_transform_orientation_03.png)

- Enter armature Edit Mode.  
  ![align_bone_to_transform_orientation_04.png](images/align_bone_to_transform_orientation_04.png)

- Either add a new bone or select an existing bone.  
  ![align_bone_to_transform_orientation_05.png](images/align_bone_to_transform_orientation_05.png)

- F3 --> "Align Bone to Transform Orientation"  
  ![align_bone_to_transform_orientation_06.png](images/align_bone_to_transform_orientation_06.png)

Now the bone sits orthogonal on the selected face and is rolled in a way that its Z axis points along the X axis of the custom transform orientation.


## Test Scripts

Just a couple of test scripts.

### [test_move_cursor.py](test_move_cursor.py)

Get location of a vertex and move cursor to Z +1 in local space.

### [test_object_info.py](test_object_info.py)

Show object info and convert vertex coordinates between local and global space.
