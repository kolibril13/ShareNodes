import bpy

class SHARENODES_PT_panel(bpy.types.Panel):
    bl_label = "ShareNodes"
    bl_idname = "SHARENODES_PT_panel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "ShareNodes"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "GeometryNodeTree"

    def draw(self, context):
        layout = self.layout
        layout.operator("sharenodes.export_node_tree", text="Export Node Tree")
        layout.operator("sharenodes.import_node_tree", text="Import Node Tree")


class SHARENODES_OT_export(bpy.types.Operator):
    bl_idname = "sharenodes.export_node_tree"
    bl_label = "Export Node Tree"

    def execute(self, context):
        print("hello world")
        return {"FINISHED"}


class SHARENODES_OT_import(bpy.types.Operator):
    bl_idname = "sharenodes.import_node_tree"
    bl_label = "Import Node Tree"

    def execute(self, context):
        print("goodbye")
        return {"FINISHED"}



def register():
    bpy.utils.register_class(SHARENODES_PT_panel)
    bpy.utils.register_class(SHARENODES_OT_export)
    bpy.utils.register_class(SHARENODES_OT_import)


def unregister():
    bpy.utils.unregister_class(SHARENODES_PT_panel)
    bpy.utils.unregister_class(SHARENODES_OT_export)
    bpy.utils.unregister_class(SHARENODES_OT_import)

