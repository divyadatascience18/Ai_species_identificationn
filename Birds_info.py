def normalize(text: str) -> str:
    return (
        text.lower()
        .replace("-", " ")
        .replace("_", " ")
        .strip()
    )




BIRDS_INFO = {

    "White-Breasted Kingfisher": {
        "name": "White-Breasted Kingfisher",
        "description": """
The White-Breasted Kingfisher, scientifically named Halcyon smyrnensis, is a vibrant, large kingfisher common across Asia, known for its bright blue back/wings, chestnut head/belly, and distinct white throat/breast, a tree kingfisher that often hunts away from water for insects, small reptiles, rodents, and even birds, making it a familiar sight in urban areas perched on wires or buildings.

Key Characteristics:
Appearance: Striking bright blue back, wings, and tail; dark brown head, shoulders, and flanks; pure white throat and breast; large red bill and red legs; large white patches on wings visible in flight.
Size: A large kingfisher, about 27–28 cm long.
Habitat: Found well away from water in gardens, agricultural fields, and towns, as well as near wetlands.
Diet: Diverse, including insects, crabs, lizards, frogs, rodents, and even small birds.
Behavior: Calls loudly from prominent perches; flight is fast and direct.
Distribution: Widespread from Turkey to the Philippines and Indonesia.
Other Names: White-throated Kingfisher, Smyrna Kingfisher.
"""
    },

    "Rufous Treepie": {
        "name": "Rufous Treepie",
        "description": """
The Rufous Treepie (Dendrocitta vagabunda) is a distinctive, long-tailed member of the crow family (Corvidae) found across the Indian Subcontinent and Southeast Asia, known for its rusty-orange body, black head, and noisy, musical calls.

Key Characteristics:
Appearance: Cinnamon/rusty-orange body with a contrasting black head and mantle, silvery-grey and white wing patches, and a long graduated grey tail tipped in black.
Call: Loud, varied, and often metallic.
Habitat: Forests, scrublands, gardens, and agricultural areas.
Diet: Omnivorous, eating insects, fruits, seeds, nectar, eggs, and small vertebrates.
Behavior: Intelligent, curious, often seen in pairs or small groups.
Scientific Name: Dendrocitta vagabunda
Family: Corvidae
"""
    },

    "Ruddy Shelduck": {
        "name": "Ruddy Shelduck",
        "description": """
The Ruddy Shelduck, scientifically named Tadorna ferruginea, is a distinctive orange-brown duck with a pale head, black tail and flight feathers, and large white wing patches, known as the Brahminy Duck in India.

Key Characteristics:
Appearance: Bright ruddy orange-brown body with a creamy head and neck; males have a black neck ring.
Size: Large, goose-like duck, 58–70 cm long.
Call: Loud honking sound.

Habitat & Behavior:
Habitat: Inland water bodies like lakes, rivers, and reservoirs.
Nesting: Holes in cliffs, trees, or burrows.
Migration: Breeds in Europe and Central Asia, winters in South Asia.

Scientific Name: Tadorna ferruginea
Family: Anatidae
Conservation Status: Least Concern
"""
    },

    "Red-Wattled Lapwing": {
        "name": "Red-Wattled Lapwing",
        "description": """
The Red-Wattled Lapwing (Vanellus indicus) is a noisy, ground-dwelling bird known for its loud 'did-he-do-it?' calls, common in wetlands across South Asia.

Key Characteristics:
Scientific Name: Vanellus indicus
Family: Charadriidae
Appearance: Large plover with prominent red wattles near the eyes.
Vocalization: Sharp alarm calls.
Habitat: Wetlands, agricultural fields.
Behavior: Ground-nesting and aggressively defends nests.
Diet: Insects, snails, and invertebrates.
Distribution: South Asia, Southeast Asia, and West Asia.
"""
    },

    "Northern Lapwing": {
        "name": "Northern Lapwing",
        "description": """
The Northern Lapwing (Vanellus vanellus) is a distinctive shorebird known for its long crest, black-and-white plumage with a green sheen, and its 'peewit' call.

Key Characteristics:
Appearance: Prominent wispy crest and iridescent green-black back.
Habitat: Open grasslands, wetlands, and fields.
Diet: Insects, worms, soil invertebrates.
Behavior: Elaborate aerial displays and aggressive nest defense.
Distribution: Europe, Asia, North Africa.

Conservation:
IUCN Status: Near Threatened
"""
    },

    "Indian Roller": {
        "name": "Indian Roller",
        "description": """
The Indian Roller (Coracias benghalensis) is a vividly colored bird known for its bright blue wing flashes and acrobatic courtship rolls.

Key Facts:
Scientific Name: Coracias benghalensis
Appearance: Brown head and back, pinkish throat, bright blue wings and tail.
Habitat: Open grasslands, scrub forests, roadside trees.
Diet: Insects, reptiles, amphibians.
Cultural Significance: Sacred to Vishnu; state bird of Karnataka, Telangana, and Odisha.
Local Name: Neelkanth
"""
    },

    "Indian Grey Hornbill": {
        "name": "Indian Grey Hornbill",
        "description": """
The Indian Grey Hornbill (Ocyceros birostris) is a common grey bird known for its unique nesting behavior where the female seals herself inside a tree cavity.

Key Characteristics:
Scientific Name: Ocyceros birostris
Appearance: Grey body, blackish bill with small casque.
Habitat: Dry plains, foothills, urban parks.
Diet: Fruits, insects, small reptiles.
Behavior: Monogamous pairs.
Conservation: Least Concern
"""
    },

    "House Crow": {
        "name": "House Crow",
        "description": """
The House Crow (Corvus splendens) is a highly adaptable bird common across South Asia and many other parts of the world.

Key Facts:
Scientific Name: Corvus splendens
Family: Corvidae
Characteristics: Black and grey plumage.
Behavior: Strong association with human settlements.
Origin: Native to South Asia.
"""
    },

    "Hoopoe": {
        "name": "Hoopoe",
        "description": """
The Hoopoe (Upupa epops) is a distinctive bird with a prominent crest, cinnamon plumage, and black-and-white wings.

Key Details:
Scientific Name: Upupa epops
Genus: Upupa
Family: Upupidae
Distribution: Eurasia, Africa, Madagascar.
Other Species: African Hoopoe, Madagascar Hoopoe.
"""
    },

    "Common Myna": {
        "name": "Common Myna",
        "description": """
The Common Myna (Acridotheres tristis) is an adaptable urban bird known for its brown body, black head, and yellow eye patches.

Scientific Classification:
Scientific Name: Acridotheres tristis
Family: Sturnidae
Diet: Omnivorous
Habitat: Urban areas and open woodlands
"""
    },

    "Common Kingfisher": {
        "name": "Common Kingfisher",
        "description": """
The Common Kingfisher (Alcedo atthis) is a small, brightly colored bird found near water bodies.

Key Details:
Scientific Name: Alcedo atthis
Common Names: Eurasian Kingfisher, River Kingfisher
Habitat: Rivers, lakes, wetlands
Diet: Small fish
"""
    },

    "Cattle Egret": {
        "name": "Cattle Egret",
        "description": """
The Cattle Egret (Bubulcus ibis) is a white heron commonly seen near livestock.

Key Information:
Scientific Name: Bubulcus ibis
Family: Ardeidae
Order: Pelecaniformes
Description: White plumage with buff breeding colors.
"""
    },

    "Asian Green Bee-eater": {
        "name": "Asian Green Bee-eater",
        "description": """
The Asian Green Bee-eater (Merops orientalis) is a small, brightly colored bird with vibrant green plumage.

Scientific Name: Merops orientalis
Family: Meropidae
Description: Green body, blue throat, black eye mask.
Habitat: Grasslands and woodlands.
"""
    },

    "Indian Peacock": {
        "name": "Indian Peacock",
        "description": """
Pavo cristatus, a large, colorful pheasant known for the male's iridescent blue plumage and spectacular train of eye-spotted feathers.

Key Characteristics:
Scientific Name: Pavo cristatus
Male: Glistening blue neck and long train
Female: Brown, lacks train
Habitat: Forests and human settlements
Diet: Omnivorous
National Bird of India
"""
    },

    "White Wagtail": {
        "name": "White Wagtail",
        "description": """
The White Wagtail (Motacilla alba) is a small black, white, and grey bird known for its long tail and energetic tail-wagging behavior.

Key Characteristics:
Appearance: Black, white, and grey plumage
Habitat: Open landscapes and urban areas
Diet: Insects and spiders
Distribution: Eurasia and Africa
Scientific Name: Motacilla alba
"""
    }

}
BIRDS_LOOKUP = {
    normalize(k): v for k, v in BIRDS_INFO.items()
}