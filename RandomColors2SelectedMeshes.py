import bpy
import random

# Seçili objeleri alın
selected_objects = bpy.context.selected_objects

# Her bir seçili objeye unique bir materyal ata ve rastgele renk ver
for i, obj in enumerate(selected_objects):
    if obj.type == 'MESH':

        #bpy.ops.object.material_slot_remove()
        obj.data.materials.clear()
        # Yeni bir materyal oluştur
        material = bpy.data.materials.new(name=f"RandomColor_{i}")
        
        obj.data.materials.append(material)
        # Rastgele renk oluştur
        random_color = (random.random(), random.random(), random.random(), 1.0)

        # Materyale rastgele renk ata
        material.use_nodes = True
        nodes = material.node_tree.nodes
        principled_bsdf = nodes.get("Principled BSDF")
        output = nodes.get("Material Output")

        if principled_bsdf and output:
            principled_bsdf.inputs['Base Color'].default_value = random_color

# Ekrana güncellemeleri yansıt
bpy.context.view_layer.update()