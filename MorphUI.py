import bpy
class MorphSetting(bpy.types.PropertyGroup):
    value: bpy.props.FloatProperty(name="value")

# UI クラスで変数を定義
class _PT_UI(bpy.types.Panel):
    bl_label = "test"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"
    bpy.utils.register_class(MorphSetting)
    #プロパティ
    bpy.types.Scene.my_items = bpy.props.CollectionProperty(type=MorphSetting)
    
    def draw(self,context):
        # UI に配置
        row = self.layout.row(align=True)
        row.prop(context.scene, "my_item")
        col = bpy.types.Scene.my_items[1]['type']
        col.morphList = ["hoge" , "fuga"]
        
        #変数にアクセス
        #for l in bpy.types.Scene.my_list:
        #    t = str(l)
        #    self.layout.label(text=t)
        
class Button(bpy.types.Operator):
    bl_idname = "dskjal.testbutton"
    bl_label = "push"

    def execute(self, context):
        #プロパティは context.作成した場所.変数名 でアクセスする
        str = context.scene.my_item
        #ただの変数はそのままアクセスする
        bpy.types.Scene.my_list.append(str)
        return{'FINISHED'}
 
# custom property       
#https://memoteu.hatenablog.com/entry/2019/06/17/132448     
        
classes = (
    _PT_UI,
    Button
)
def register():
    from bpy.utils import register_class
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        register_class(cls)

if __name__ == "__main__":
    register()
