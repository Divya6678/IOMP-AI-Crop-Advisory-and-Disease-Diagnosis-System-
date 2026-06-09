DISEASE_KEYS = [
    "Apple_scab", "Black_rot", "Cedar_apple_rust", "healthy", "Powdery_mildew", 
    "Cercospora_leaf_spot Gray_leaf_spot", "Common_rust_", "Northern_Leaf_Blight", 
    "Esca_(Black_Measles)", "Leaf_blight_(Isariopsis_Leaf_Spot)", 
    "Haunglongbing_(Citrus_greening)", "Bacterial_spot", "Early_blight", 
    "Late_blight", "Leaf_scorch", "Leaf_Mold", "Septoria_leaf_spot", 
    "Spider_mites Two-spotted_spider_mite", "Target_Spot", 
    "Tomato_Yellow_Leaf_Curl_Virus", "Tomato_mosaic_virus"
]

RECOMMENDATIONS = {
    "healthy": {
        "Low": {"organic": "No action needed.", "chemical": "None.", "advice": "Continue standard care."},
        "Medium": {"organic": "No action needed.", "chemical": "None.", "advice": "Continue standard care."},
        "High": {"organic": "No action needed.", "chemical": "None.", "advice": "Your crop is completely healthy!"}
    },
    "Apple_scab": {
        "Low": {"organic": "Rake and destroy fallen leaves.", "chemical": "Preventative Captan or Mancozeb.", "advice": "Prune trees to increase airflow."},
        "Medium": {"organic": "Apply liquid copper soap.", "chemical": "Myclobutanil fungicide.", "advice": "Apply fungicide before rain occurs."},
        "High": {"organic": "Remove heavily infected branches.", "chemical": "Systemic fungicide immediately.", "advice": "Clear all debris around the base of the tree."}
    },
    "Black_rot": {
        "Low": {"organic": "Remove mummified fruit.", "chemical": "Mancozeb in early spring.", "advice": "Ensure adequate sunlight penetration."},
        "Medium": {"organic": "Prune dead or diseased wood.", "chemical": "Myclobutanil or Captan.", "advice": "Spray every 10-14 days."},
        "High": {"organic": "Destroy infected crops.", "chemical": "Strong synthetic fungicide.", "advice": "Do not compost infected materials."}
    },
    "Cedar_apple_rust": {
        "Low": {"organic": "Remove proximate cedar galls.", "chemical": "Copper-based preventive.", "advice": "Plant rust-resistant varieties."},
        "Medium": {"organic": "Neem oil application.", "chemical": "Myclobutanil applications.", "advice": "Apply precisely when apple blossoms open."},
        "High": {"organic": "Remove heavily infected apple leaves.", "chemical": "Systemic sterol inhibitor fungicide.", "advice": "Severely affects fruit yield; isolate if possible."}
    },
    "Powdery_mildew": {
        "Low": {"organic": "Baking soda and soap mixture.", "chemical": "Sulfur-based fungicides.", "advice": "Space plants for better circulation."},
        "Medium": {"organic": "Potassium bicarbonate spray.", "chemical": "Myclobutanil.", "advice": "Avoid overhead watering."},
        "High": {"organic": "Remove heavily mildewed foliage.", "chemical": "Targeted systemic chemical.", "advice": "Pathogen thrives in high humidity; monitor closely."}
    },
    "Cercospora_leaf_spot Gray_leaf_spot": {
        "Low": {"organic": "Crop rotation for 2-3 years.", "chemical": "Chlorothalonil applied early.", "advice": "Water at soil level to keep leaves dry."},
        "Medium": {"organic": "Copper-based fungicide.", "chemical": "Azoxystrobin or Propiconazole.", "advice": "Start spraying before spots merge."},
        "High": {"organic": "Plow under infected crop residue.", "chemical": "Curative systemic fungicide mixed with protectant.", "advice": "Extremely contagious in damp conditions."}
    },
    "Common_rust_": {
        "Low": {"organic": "Plant resistant hybrids.", "chemical": "Preventative Mancozeb.", "advice": "Monitor fields early in the season."},
        "Medium": {"organic": "Neem oil extract.", "chemical": "Pyraclostrobin or Propiconazole.", "advice": "Apply immediately upon spotting pustules."},
        "High": {"organic": "Harvest early if possible.", "chemical": "Aggressive systemic fungicide rotation.", "advice": "Spores travel by wind; alert neighboring fields."}
    },
    "Northern_Leaf_Blight": {
        "Low": {"organic": "Tillage to bury residue.", "chemical": "Preventive azoxystrobin.", "advice": "Plant resistant corn varieties."},
        "Medium": {"organic": "Bacillus subtilis biopesticide.", "chemical": "Fungicide cocktail (Strobilurin & Triazole).", "advice": "Apply around tasseling stage."},
        "High": {"organic": "Chop and incorporate debris deep.", "chemical": "Multiple mode-of-action foliar fungicide.", "advice": "High yield loss expected; act quickly."}
    },
    "Esca_(Black_Measles)": {
        "Low": {"organic": "Identify and mark affected vines.", "chemical": "Apply wound protectants post-pruning.", "advice": "Prune late in the dormant season."},
        "Medium": {"organic": "Trunk renewal (cut below symptoms).", "chemical": "Thiophanate-methyl on fresh pruning wounds.", "advice": "Sanitize pruning shears between vines."},
        "High": {"organic": "Uproot and burn severely decayed vines.", "chemical": "No chemical cure for advanced wood decay.", "advice": "Replant with healthy nursery stock."}
    },
    "Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "Low": {"organic": "Remove spotted initial leaves.", "chemical": "Preventive copper sprays.", "advice": "Ensure adequate canopy aeration."},
        "Medium": {"organic": "Apply sulfur or neem oil.", "chemical": "Broad-spectrum contact fungicide.", "advice": "Repeat applications after heavy rain."},
        "High": {"organic": "Prune and dispose of majorly affected parts.", "chemical": "Systemic triazoles.", "advice": "Do not leave infected leaves on the ground."}
    },
    "Haunglongbing_(Citrus_greening)": {
        "Low": {"organic": "Control Asian citrus psyllids.", "chemical": "Imidacloprid soil drench for vectors.", "advice": "Monitor young flush for psyllids."},
        "Medium": {"organic": "Enhanced nutritional foliar sprays.", "chemical": "Rotational insecticide application.", "advice": "Disease is incurable; focus on vector control."},
        "High": {"organic": "Remove and destroy infected trees.", "chemical": "Aggressive area-wide psyllid suppression.", "advice": "Legal quarantine may be required."}
    },
    "Bacterial_spot": {
        "Low": {"organic": "Use disease-free seed/transplants.", "chemical": "Copper plus mancozeb tank mix.", "advice": "Avoid working in wet fields."},
        "Medium": {"organic": "Apply bacteriophages or Bacillus sprays.", "chemical": "Fixed copper applications.", "advice": "Sprays only suppress, they do not cure."},
        "High": {"organic": "Destroy severely infected plants.", "chemical": "Frequent copper spray rotation.", "advice": "Bacteria spreads rapidly in warm rain."}
    },
    "Early_blight": {
        "Low": {"organic": "Rotate crops (no Solanaceae).", "chemical": "Chlorothalonil applications.", "advice": "Stake plants to lift from soil."},
        "Medium": {"organic": "Apply compost tea or copper soap.", "chemical": "Mancozeb or Azoxystrobin.", "advice": "Treat lower leaves first, where it starts."},
        "High": {"organic": "Bag and dispose of dead foliage.", "chemical": "Targeted anti-sporulant fungicide.", "advice": "Water at base, never overhead."}
    },
    "Late_blight": {
        "Low": {"organic": "Plant certified disease-free tubers/seeds.", "chemical": "Preventative contact fungicide (Mancozeb).", "advice": "Monitor local blight reports."},
        "Medium": {"organic": "Immediate copper spray.", "chemical": "Cymoxanil or Dimethomorph.", "advice": "Spores travel miles; spray immediately."},
        "High": {"organic": "Kill vines to protect tubers (potatoes).", "chemical": "Fast-acting systemic eradicant.", "advice": "Highly destructive; clear out blighted fields fast."}
    },
    "Leaf_scorch": {
        "Low": {"organic": "Deep, infrequent watering.", "chemical": "None (usually environmental).", "advice": "Check soil moisture and salt levels."},
        "Medium": {"organic": "Mulch to retain soil moisture.", "chemical": "None (flush salts with fresh water).", "advice": "Avoid excessive fertilizer application."},
        "High": {"organic": "Provide afternoon shade.", "chemical": "None.", "advice": "Ensure roots are not physically restricted."}
    },
    "Leaf_Mold": {
        "Low": {"organic": "Increase greenhouse ventilation.", "chemical": "Preventative Chlorothalonil.", "advice": "Keep humidity below 85%."},
        "Medium": {"organic": "Prune lower leaves to boost airflow.", "chemical": "Difenoconazole or Mancozeb.", "advice": "Infection happens on the leaf underside."},
        "High": {"organic": "Remove extensive moldy foliage.", "chemical": "Systemic fungicide for mold.", "advice": "Sanitize greenhouse thoroughly off-season."}
    },
    "Septoria_leaf_spot": {
        "Low": {"organic": "Apply thick layer of mulch.", "chemical": "Preventive copper-based fungicide.", "advice": "Prevents soil splashing onto leaves."},
        "Medium": {"organic": "Remove spotted lower leaves.", "chemical": "Chlorothalonil every 7-10 days.", "advice": "Do not touch healthy plants after infected ones."},
        "High": {"organic": "Destroy heavily infected plants.", "chemical": "Strong synthetic fungicide.", "advice": "Can defoliate plant entirely if unchecked."}
    },
    "Spider_mites Two-spotted_spider_mite": {
        "Low": {"organic": "Strong blast of water to dislodge mites.", "chemical": "Horticultural oil or insecticidal soap.", "advice": "Mites thrive in hot, dry, dusty conditions."},
        "Medium": {"organic": "Introduce predatory mites (Phytoseiulus).", "chemical": "Spiromesifen or Abamectin.", "advice": "Ensure thorough coverage under leaves."},
        "High": {"organic": "Prune webbed and yellowed foliage heavily.", "chemical": "Rotation of high-grade miticides.", "advice": "Mites build chemical resistance very quickly."}
    },
    "Target_Spot": {
        "Low": {"organic": "Improve air circulation in canopy.", "chemical": "Basic copper treatments.", "advice": "Monitor interior leaves of the plant."},
        "Medium": {"organic": "Remove lower infected canopy.", "chemical": "Azoxystrobin or Chlorothalonil.", "advice": "Pathogen thrives in high humidity."},
        "High": {"organic": "Discard severely spotted plants.", "chemical": "Systemic fungicides.", "advice": "Wash hands/tools after handling."}
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "Low": {"organic": "Use reflective mulches to deter whiteflies.", "chemical": "Insecticide strictly targeting whiteflies.", "advice": "Plant resistant cultivars."},
        "Medium": {"organic": "Use floating row covers early on.", "chemical": "Systemic insecticide (e.g., Imidacloprid).", "advice": "Once infected, the plant cannot be cured."},
        "High": {"organic": "Rogue (pull up) infected plants unconditionally.", "chemical": "None for virus; kill vector insects.", "advice": "Bag the plant immediately so whiteflies don't scatter."}
    },
    "Tomato_mosaic_virus": {
        "Low": {"organic": "Wash hands with soap and water before handling.", "chemical": "None.", "advice": "Virus is highly mechanically transmitted."},
        "Medium": {"organic": "Disinfect tools with 10% bleach solution.", "chemical": "None.", "advice": "Do not use tobacco products near plants."},
        "High": {"organic": "Burn or throw away all infected debris.", "chemical": "None.", "advice": "Virus remains viable in soil debris for years."}
    }
}