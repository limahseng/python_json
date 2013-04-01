import json

productdata = """
[
  {"Id":"P01",
   "Image":"apple.jpg",
   "Category":"Healthy fruit"
  },
  {"Id":"P02",
   "Image":"banana.jpg",
   "Category":"Happy food"
  }	
]
"""

# convert from JSON to Python
decoded = json.loads(productdata)

for product in decoded:
    for key, value in product.items():
        print(key, value)


