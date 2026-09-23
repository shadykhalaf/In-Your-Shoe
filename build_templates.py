import json

# --- Liquid snippets ---

# Size chart: file_reference (image) metafield — must use image_url filter to render as <img>
# image_url works directly on the metafield object for file_reference types
size_chart_liquid = (
    "{%- assign sc = product.metafields.custom.size_chart -%}"
    "{%- if sc != blank -%}"
    "{{ sc | image_url: width: 800 | image_tag: loading: 'lazy', style: 'max-width:100%;height:auto;display:block;', alt: product.title }}"
    "{%- endif -%}"
)

# Care guide metafield (rich text)
care_guide_liquid = (
    "{%- if product.metafields.descriptors.care_guide != blank -%}"
    "{{ product.metafields.descriptors.care_guide.value }}"
    "{%- endif -%}"
)

# Model sizes: styled box, only shows when metafield has content
model_liquid = (
    "{%- assign model_mf = product.metafields.custom.model -%}"
    "{%- if model_mf != blank -%}"
    '<div class="feature-badge" style="background:#EDF2EA;padding:12px 14px;border-radius:4px;display:flex;gap:10px;align-items:flex-start;">'
    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:2px;">'
    '<circle cx="12" cy="12" r="10"></circle>'
    '<line x1="12" y1="8" x2="12" y2="12"></line>'
    '<line x1="12" y1="16" x2="12.01" y2="16"></line>'
    "</svg>"
    '<span style="font-size:0.875rem;color:#222222;line-height:1.5;">{{ model_mf.value }}</span>'
    "</div>"
    "{%- endif -%}"
)

# --- Common accordion blocks (shared by both templates) ---
def care_guide_accordion():
    return {
        "type": "accordion",
        "settings": {
            "show_below_gallery": False,
            "icon": "none",
            "title": "Care Guide",
            "liquid": care_guide_liquid
        }
    }

def shipping_accordion():
    return {
        "type": "accordion",
        "settings": {
            "show_below_gallery": False,
            "icon": "none",
            "title": "Shipping Policy",
            "content": ""
        }
    }

def exchange_accordion():
    return {
        "type": "accordion",
        "settings": {
            "show_below_gallery": False,
            "icon": "none",
            "title": "Exchange & Refund",
            "content": ""
        }
    }

# ============================================================
# product.json  (Default - no sizes, no size chart)
# ============================================================
product_default = {
    "sections": {
        "main": {
            "type": "main-product",
            "blocks": {
                "vendor_1":           {"type": "vendor", "settings": {}},
                "title_1":            {"type": "title", "settings": {"heading_tag": "h1"}},
                "sku_1":              {"type": "sku", "disabled": True, "settings": {}},
                "price_1":            {"type": "price", "settings": {"show_taxes_notice": False}},
                "rating_1":           {"type": "rating", "settings": {"show_empty": False, "rating_mode": "rating"}},
                "separator_1":        {"type": "separator", "settings": {}},
                "description_1":      {"type": "description", "settings": {"collapse_content": True, "show_below_gallery": False}},
                "quantity_selector_1":{"type": "quantity_selector", "settings": {}},
                "buy_buttons_1":      {"type": "buy_buttons", "settings": {"show_payment_button": True, "show_gift_card_recipient": False}},
                "accordion_care":     care_guide_accordion(),
                "accordion_shipping": shipping_accordion(),
                "accordion_exchange": exchange_accordion(),
                "share_buttons_1":    {"type": "share_buttons", "settings": {}},
                "complementary_1":    {"type": "complementary_products", "disabled": True, "settings": {"title": "Pairs well with", "products_count": 4, "show_below_gallery": True, "stack_products": False, "show_quick_buy": True}}
            },
            "block_order": [
                "vendor_1", "title_1", "sku_1", "price_1", "rating_1",
                "separator_1", "description_1",
                "quantity_selector_1", "buy_buttons_1",
                "accordion_care", "accordion_shipping", "accordion_exchange",
                "share_buttons_1", "complementary_1"
            ],
            "settings": {}
        },
        "related-products": {"type": "related-products", "settings": {}}
    },
    "order": ["main", "related-products"]
}

# ============================================================
# product.sizes.json  (Sizes - variant picker + size chart + model sizes)
# ============================================================
product_sizes = {
    "sections": {
        "main": {
            "type": "main-product",
            "blocks": {
                "vendor_1":             {"type": "vendor", "settings": {}},
                "title_1":              {"type": "title", "settings": {"heading_tag": "h1"}},
                "sku_1":                {"type": "sku", "disabled": True, "settings": {}},
                "price_1":              {"type": "price", "settings": {"show_taxes_notice": False}},
                "rating_1":             {"type": "rating", "settings": {"show_empty": False, "rating_mode": "rating"}},
                "model_sizes_1":        {"type": "liquid", "settings": {"liquid": model_liquid}},
                "separator_1":          {"type": "separator", "settings": {}},
                "description_1":        {"type": "description", "settings": {"collapse_content": True, "show_below_gallery": False}},
                "variant_picker_1":     {"type": "variant_picker", "settings": {"hide_sold_out_variants": False, "selector_style": "block", "swatch_selector_style": "swatch"}},
                "quantity_selector_1":  {"type": "quantity_selector", "settings": {}},
                "buy_buttons_1":        {"type": "buy_buttons", "settings": {"show_payment_button": True, "show_gift_card_recipient": False}},
                "accordion_size_chart": {"type": "accordion", "settings": {"show_below_gallery": False, "icon": "none", "title": "Size Chart", "liquid": size_chart_liquid}},
                "accordion_care":       care_guide_accordion(),
                "accordion_shipping":   shipping_accordion(),
                "accordion_exchange":   exchange_accordion(),
                "share_buttons_1":      {"type": "share_buttons", "settings": {}},
                "complementary_1":      {"type": "complementary_products", "disabled": True, "settings": {"title": "Pairs well with", "products_count": 4, "show_below_gallery": True, "stack_products": False, "show_quick_buy": True}}
            },
            "block_order": [
                "vendor_1", "title_1", "sku_1", "price_1", "rating_1",
                "model_sizes_1", "separator_1", "description_1",
                "variant_picker_1", "quantity_selector_1", "buy_buttons_1",
                "accordion_size_chart", "accordion_care", "accordion_shipping", "accordion_exchange",
                "share_buttons_1", "complementary_1"
            ],
            "settings": {}
        },
        "related-products": {"type": "related-products", "settings": {}}
    },
    "order": ["main", "related-products"]
}

# Write files
base = r"c:\Users\COMPU ZONE\inyourshoe-prestige\templates"

with open(base + r"\product.json", "w", encoding="utf-8") as f:
    json.dump(product_default, f, indent=2, ensure_ascii=False)

with open(base + r"\product.sizes.json", "w", encoding="utf-8") as f:
    json.dump(product_sizes, f, indent=2, ensure_ascii=False)

# Verify both
for name in ["product.json", "product.sizes.json"]:
    with open(base + "\\" + name, "r", encoding="utf-8") as f:
        data = json.load(f)
    blocks = data["sections"]["main"]["blocks"]
    order  = data["sections"]["main"]["block_order"]
    print(f"{name}: OK | {len(blocks)} blocks | order matches: {sorted(blocks.keys()) == sorted(order)}")
