import bpy
# 1. select object which name is end with ".L"
# 2. run script.
# 3. you can see object which name is end with ".R" and which is constraint "copy location invert_x". 

selected = []
for i in bpy.context.selected_objects:
  selected.append(i)

for ob in bpy.context.scene.objects:
  ob.select = False

for i in selected:
  i.select = True
  objectName = i.name
  objectName = objectName.replace('.L' , "")
  bpy.ops.object.duplicate()
  newObj = bpy.data.objects[objectName + '.L.001']
  i.select = False
  newObj.select = True
  newObj.name = objectName + '.R'
  constraint = newObj.constraints.new('COPY_LOCATION')
  constraint.invert_x = True
  constraint.target = bpy.data.objects[objectName + '.L']
  newObj.select = False
