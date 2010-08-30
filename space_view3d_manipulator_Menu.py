#re creating the functionality of the manipulator menu from 2.49
#
#ported by Michael Williamson
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_addon_info = {
    'name': '3D View: Manipulator Menu',
    'author': 'MichaelW',
    'version': '1',
    'blender': (2, 5, 3),
    'location': 'View3D > Ctrl Space ',
    'description': 'Menu to change the manipulator type and/or disable it',
    'category': '3D View'}
"Add manipulator menu  (Ctrl-space in 3d view)"

"""
Name: '3D Dynamic Menu'
Blender: 253
"""

__author__ = ["MichaelW"]
__version__ = '1.0'
__url__ = [""]
__bpydoc__= """
Dynamic Menu
This adds a the Dynamic Menu in the 3DView.

Usage:
* Ctrl Space in the 3d view

* Choose your function from the menu.

Version history:
V1(MichaelW) initial port form 2.49
    

"""


import bpy

def main(context):
    bpy.context.space_data.manipulator = False

class VIEW3D_OT_disable_manipulator(bpy.types.Operator):
    ''''''
    bl_idname = "VIEW3D_OT_disable_manipulator"
    bl_label = "disable manipulator"

    @staticmethod
    def poll(context):
        return context.active_object != None

    def execute(self, context):
        main(context)
        return {'FINISHED'}



class VIEW3D_MT_ManipulatorMenu(bpy.types.Menu):
    ''''''
    bl_label = "ManipulatorType"
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'



        prop = layout.operator("view3d.enable_manipulator",text ='Translate', icon='MAN_TRANS')
        prop.translate = True

        prop = layout.operator("view3d.enable_manipulator",text ='Rotate', icon='MAN_ROT')
        prop.rotate = True

        prop = layout.operator("view3d.enable_manipulator",text ='Scale', icon='MAN_SCALE')
        prop.scale = True
        layout.separator()

        prop = layout.operator("view3d.enable_manipulator",text ='Combo', icon='MAN_SCALE')
        prop.scale = True
        prop.rotate = True
        prop.translate = True

        layout.separator()
        if not bpy.context.space_data.manipulator:
            bpy.context.space_data.manipulator = True
        layout.operator("view3d.disable_manipulator",text ='Disable', icon='MANIPUL')
        layout.separator()


            
def register():

    km = bpy.context.manager.active_keyconfig.keymaps['3D View']
    for kmi in km.items:
        if kmi.idname == 'wm.context_toggle':
            if kmi.ctrl and not kmi.shift and not kmi.alt and kmi.value =="PRESS":
                if kmi.type =="SPACE":
                    km.remove_item(kmi)
                    break
    kmi = km.items.add('wm.call_menu', 'SPACE', 'PRESS' , ctrl=True)
    kmi.properties.name = "VIEW3D_MT_ManipulatorMenu"


def unregister():

    for kmi in km.items:
        if kmi.idname == 'wm.call_menu':
            if kmi.properties.name == "VIEW3D_MT_ManipulatorMenu":
                km.remove_item(kmi)
                break

if __name__ == "__main__":
    register()