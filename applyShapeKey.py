import bpy
nameList = []
for i in bpy.context.object.modifiers:
  nameList.append(i.name)
  nameList.append(i.name + "Backup")

def findInNameList(modList):
  for i in modList:
    if( not (i.name in nameList) ):
      return i

for i in bpy.context.object.modifiers:
  name = i.name
  if("ARMATURE" in i.type):
    continue
  print(name)
  modList = bpy.context.object.modifiers
  bpy.ops.object.modifier_copy(modifier=name)
  newMod = findInNameList(modList)
  bpy.context.object.modifiers[name].name = name + "Backup"
  print(newMod.name)
  newMod.name = name
  bpy.ops.object.modifier_apply(apply_as='SHAPE', modifier=name)
  i.show_viewport = False
  mmd_root = bpy.context.object.parent.parent.mmd_root
  #mmd_root.active_morph = 0
  bpy.ops.mmd_tools.morph_add()
  mmd_root.vertex_morphs["New Morph"].name = name

