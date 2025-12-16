def normalize(text: str) -> str:
    return (
        text.lower()
        .replace("-", " ")
        .replace("_", " ")
        .strip()
    )



LEAF_INFO = {

    "Rose": {
        "name": "Rose",
        "description": """
The scientific name for a rose plant belongs to the genus Rosa, under the family Rosaceae.

Examples of Species:
• Rosa indica (Indian Rose)
• Rosa gallica (French Rose)
• Rosa canina
• Rosa rugosa

Leaf Characteristics:
• Leaves are alternate and pinnately compound
• Usually have an odd number of leaflets
• Leaflets are oval with sharply toothed edges
• Show reticulate venation

Rose leaves do not have a separate scientific name and are classified as part of the Rosa species itself.
"""
    },

    "Kamakasturi": {
        "name": "Kamakasturi (Sweet Basil)",
        "description": """
Kamakasturi refers to Sweet Basil, scientifically known as Ocimum basilicum, from the Lamiaceae (mint) family.

Key Details:
• Scientific Name: Ocimum basilicum
• Family: Lamiaceae
• Common Names: Sweet Basil, Thai Basil
• Seeds: Known as Sabja seeds

Characteristics:
• Aromatic herb
• Simple, opposite leaves
• Often purple stems
• Tiny flowers

Uses:
• Cooking (Thai & Italian cuisine)
• Ayurvedic remedies
• Health drinks like Falooda
"""
    },

    "Ashoka": {
        "name": "Ashoka Tree",
        "description": """
The Ashoka tree is scientifically named Saraca asoca (Roxb.) De Wilde and belongs to the Fabaceae family.

Key Characteristics:
• Evergreen tree
• Pinnate leaves with 3–7 pairs of leaflets
• Young leaves are coppery-red and drooping

Medicinal Significance:
• Important in Ayurveda
• Used for menstrual health and uterine disorders
• Bark and flowers used in treatments

Common Names:
Ashoka, Sita Ashoka, Sorrowless Tree
"""
    },

    "Neem": {
        "name": "Neem",
        "description": """
Neem is scientifically named Azadirachta indica and belongs to the Meliaceae family.

Key Characteristics:
• Evergreen tropical tree
• Bitter medicinal leaves
• Drought resistant

Uses:
• Skin care
• Antimicrobial treatments
• Natural insect repellent
• Dental hygiene (twigs)

Neem is widely known as a ‘miracle tree’ in traditional medicine.
"""
    },

    "Tamarind": {
        "name": "Tamarind",
        "description": """
The tamarind plant is scientifically named Tamarindus indica and belongs to the Fabaceae family.

Leaf Characteristics:
• Paripinnate (feather-like) leaves
• 10–20 pairs of small oblong leaflets
• Pale green underside

Uses:
• Traditional medicine
• Cooking
• Tanning leather
"""
    },

    "Mint": {
        "name": "Mint",
        "description": """
Mint belongs to the genus Mentha, under the Lamiaceae family.

Common Species:
• Mentha piperita (Peppermint)
• Mentha spicata (Spearmint)
• Mentha arvensis

Characteristics:
• Square stems
• Opposite leaves
• Strong aroma

Uses:
• Food flavoring
• Essential oils
• Digestive medicine
"""
    },

    "Mango": {
        "name": "Mango",
        "description": """
The mango plant is scientifically named Mangifera indica L. and belongs to the Anacardiaceae family.

Leaf Characteristics:
• Simple, leathery leaves
• Young leaves are coppery-red
• Mature leaves are dark green

Medicinal Uses:
• Anti-diabetic
• Antioxidant
• Anti-inflammatory
"""
    },

    "Coffee": {
        "name": "Coffee",
        "description": """
Coffee belongs to the genus Coffea in the Rubiaceae family.

Main Species:
• Coffea arabica
• Coffea canephora (Robusta)

Uses:
• Leaves used for herbal tea
• Beans used for coffee production
"""
    },

    "Papaya": {
        "name": "Papaya",
        "description": """
Papaya leaves come from Carica papaya L., belonging to the Caricaceae family.

Uses:
• Boosting platelets (dengue)
• Digestive health
• Anti-inflammatory

Leaves are rich in alkaloids and antioxidants.
"""
    },

    "Coriander": {
        "name": "Coriander",
        "description": """
Coriander is scientifically named Coriandrum sativum L. and belongs to the Apiaceae family.

Common Names:
• Coriander
• Cilantro
• Dhaniya

Uses:
• Culinary herb
• Medicinal plant
• Rich in antioxidants
"""
    },

    "Bamboo": {
        "name": "Bamboo",
        "description": """
Bamboo belongs to the Poaceae family and commonly the genus Bambusa.

Common Species:
• Bambusa vulgaris
• Bambusa bambos

Leaf Characteristics:
• Long, narrow
• Parallel venation

Uses:
• Thatching
• Forage
• Traditional medicine
"""
    },

    "Aloe Vera": {
        "name": "Aloe Vera",
        "description": """
Aloe Vera is scientifically named Aloe barbadensis miller.

Family:
• Asphodelaceae

Uses:
• Skin healing
• Digestive aid
• Anti-inflammatory

Leaves are fleshy and store medicinal gel.
"""
    },

    "Amla": {
        "name": "Amla",
        "description": """
Amla is scientifically named Phyllanthus emblica L.

Uses:
• Immunity booster
• Rich in Vitamin C
• Ayurvedic medicine

Also known as Indian Gooseberry.
"""
    },

    "Asthma Weed": {
        "name": "Asthma Weed",
        "description": """
Asthma Weed is scientifically named Euphorbia hirta L.

Uses:
• Asthma
• Bronchitis
• Digestive disorders

Produces milky latex when broken.
"""
    },

    "Pumpkin": {
        "name": "Pumpkin Leaves",
        "description": """
Pumpkin leaves come from Cucurbita species.

Common Types:
• Cucurbita pepo
• Cucurbita maxima

Leaves are edible and nutritious.
"""
    },

    "Taro": {
        "name": "Taro",
        "description": """
Taro is scientifically named Colocasia esculenta.

Uses:
• Edible leaves
• Medicinal value

Leaves must be cooked to remove irritation.
"""
    },

    "Balloon Vine": {
        "name": "Balloon Vine",
        "description": """
Balloon Vine is scientifically named Cardiospermum halicacabum.

Uses:
• Rheumatism
• Skin diseases
• Fever

Commonly called Mudakathan Keerai.
"""
    },

    "Amruthaballi": {
        "name": "Amruthaballi (Giloy)",
        "description": """
Amruthaballi is scientifically named Tinospora cordifolia.

Uses:
• Immunity booster
• Detoxification
• Fever management
"""
    },

    "Oleander": {
        "name": "Oleander",
        "description": """
Oleander is scientifically named Nerium oleander.

Warning:
⚠️ Highly toxic if ingested.

Used as an ornamental plant.
"""
    },

    "Jackfruit": {
        "name": "Jackfruit",
        "description": """
Jackfruit is scientifically named Artocarpus heterophyllus.

Leaf Characteristics:
• Large
• Glossy
• Leathery

Used in traditional medicine and cooking.
"""
    }

}

LEAF_LOOKUP = {
    normalize(k): v for k, v in LEAF_INFO.items()
}