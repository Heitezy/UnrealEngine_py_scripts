import unreal
import os
import sys

# Function to change the texture group of a texture asset
def change_texture_group_settings(full_asset_path):
    # Get Asset Path from full asset path
    directory, filename_with_extension = os.path.split(full_asset_path)
    filename, extension = os.path.splitext(filename_with_extension)
    full_asset_path = os.path.join(directory, f"{filename}.{filename}")
    split_index = full_asset_path.find("\\Content\\")

    if split_index != -1:
       texture_asset_path = "/Game" + full_asset_path[split_index + len("\\Content"):].replace("\\", "/")
    else:
       print(f"Asset Path not found: {full_asset_path}")

    # Load the texture asset
    texture_asset = unreal.EditorAssetLibrary.load_asset(texture_asset_path)

    if texture_asset:
        # Set the group to UI
        texture_asset.set_editor_property("lod_group", unreal.TextureGroup.TEXTUREGROUP_UI)

        # Save the changes to the texture asset
        unreal.EditorAssetLibrary.save_loaded_asset(texture_asset)

        print(f"Texture group of {texture_asset_path} set to UI.")
    else:
        print(f"Texture asset not found: {texture_asset_path}")

# Check if a folder path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python TextureGroupToUI.py <full_folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

# Check if the provided folder path exists
if not os.path.exists(folder_path):
    print(f"Folder does not exist: {folder_path}")
    sys.exit(1)

# Iterate through the files in the specified folder
for root, _, files in os.walk(folder_path):
    for file_name in files:
        if file_name.lower().endswith(".uasset"):  # Adjust the file extension as needed
            full_asset_path = os.path.join(root, file_name)
            change_texture_group_settings(full_asset_path)
