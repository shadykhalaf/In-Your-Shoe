import json
base = r"c:\Users\COMPU ZONE\inyourshoe-prestige\templates"
for fname in ["product.json", "product.sizes.json"]:
    with open(base + "\\" + fname, "r", encoding="utf-8") as f:
        data = json.load(f)
    main = data["sections"]["main"]
    settings = main.get("settings", {})
    print(fname, "section settings:", settings)
