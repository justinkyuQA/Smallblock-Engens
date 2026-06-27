from smallblock.assets import AssetManager

assets = AssetManager()

print("Project exists:",
      assets.exists("projects","demo.json"))

project = assets.json("projects","demo.json")

print(project)

print("Name:", project["name"])
print("Version:", project["version"])
print("Author:", project["author"])
