import bpy
for mod in bpy.context.object.modifiers:
  mod.show_expanded = False
  name = ""
  if "Cast" in mod.name :
    name = mod.object.name.replace(".","")
  if "Warp" in mod.name :
    name = mod.object_from.name.replace(".","")
  if not name == "":
    mod.name = name
