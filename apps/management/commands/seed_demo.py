from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.models import Category, Product, ProductReview

# Nomiga mos haqiqiy oziq-ovqat rasmlari
DEMO = [
    {
        "cat": "Meva", "icon": "🍎",
        "items": [
            ("Qizil olma", 18000, "Shirin, yangi qizil olma. 1 kg.", 5, 10,
             "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1570913149827-d2ac84ab3f9a?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
             ]),
            ("Banan", 22000, "Ekvador banani, pishgan. 1 kg.", 5, 0,
             "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1603833665858-e61d17a86224?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1528825871115-3581a5419a26?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
             ]),
            ("Apelsin", 25000, "Shirin apelsin, C vitamini boy. 1 kg.", 4, 5,
             "https://images.unsplash.com/photo-1547514701-42782124196d?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg",
             ]),
        ],
    },
    {
        "cat": "Sabzavot", "icon": "🥕",
        "items": [
            ("Pomidor", 15000, "Yerli pomidor, salat uchun. 1 kg.", 5, 0,
             "https://images.unsplash.com/photo-1546470427-e26264be0d17?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1561136594-7f68413baa99?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/8/89/Tomato_je.jpg",
             ]),
            ("Bodring", 12000, "Yangi bodring. 1 kg.", 5, 0,
             "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1604977048156-dd63c9f8c1a4?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/9/96/ARS_cucumber.jpg",
             ]),
            ("Sabzi", 8000, "Toza sabzi. 1 kg.", 4, 0,
             "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1447175008436-170170753886?auto=format&fit=crop&w=800&q=80",
                 "https://upload.wikimedia.org/wikipedia/commons/a/a2/Vegetable-Carrot-Bundle.jpg",
             ]),
        ],
    },
    {
        "cat": "Sut mahsulotlari", "icon": "🥛",
        "items": [
            ("Sut 1L", 14000, "Tabiiy sigir suti, 1 litr.", 5, 0,
             "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1628088062854-d1870b4553da?auto=format&fit=crop&w=800&q=80",
             ]),
            ("Pishloq", 45000, "Qattiq pishloq, 500 g.", 5, 15,
             "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1452195100486-9cc805987862?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1552767059-cee187cfeff2?auto=format&fit=crop&w=800&q=80",
             ]),
        ],
    },
    {
        "cat": "Non mahsulotlari", "icon": "🍞",
        "items": [
            ("Non", 5000, "Yangilangan non, 1 dona.", 5, 0,
             "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1585478259715-876acc5be8eb?auto=format&fit=crop&w=800&q=80",
             ]),
            ("Croissant", 12000, "Yumshoq croissant, 1 dona.", 5, 0,
             "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1623334044303-2410213960c1?auto=format&fit=crop&w=800&q=80",
             ]),
        ],
    },
    {
        "cat": "Ichimliklar", "icon": "🧃",
        "items": [
            ("Apelsin sharbati", 18000, "Tabiiy sharbat, 1L.", 4, 10,
             "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1600271886742-f049cd799b17?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=800&q=80",
             ]),
            ("Mineral suv", 4000, "Gazlangan mineral suv, 1.5L.", 5, 0,
             "https://images.unsplash.com/photo-1523362628745-0c100150b504?auto=format&fit=crop&w=800&q=80",
             [
                 "https://images.unsplash.com/photo-1560023907-5f339617ea55?auto=format&fit=crop&w=800&q=80",
                 "https://images.unsplash.com/photo-1548832633-13ebbdc5c8e1?auto=format&fit=crop&w=800&q=80",
             ]),
        ],
    },
]


class Command(BaseCommand):
    help = "Demo mahsulotlar — nomiga mos rasmlar bilan"

    def handle(self, *args, **options):
        created_p = 0
        for block in DEMO:
            cat, _ = Category.objects.get_or_create(
                slug=slugify(block["cat"]) or "cat",
                defaults={"name": block["cat"], "icon": block["icon"]},
            )
            if not cat.icon:
                cat.icon = block["icon"]
                cat.save(update_fields=["icon"])
            for name, price, about, rating, sale, cover, gallery in block["items"]:
                p, created = Product.objects.get_or_create(
                    name=name,
                    defaults={
                        "price": price,
                        "about": about,
                        "category": cat,
                        "rating": rating,
                        "sale": sale,
                        "is_active": True,
                        "unit": "dona" if block["cat"] == "Non mahsulotlari" else "kg",
                        "cover_url": cover,
                        "gallery_urls": "\n".join(gallery),
                        "min_count": 1,
                    },
                )
                p.cover_url = cover
                p.gallery_urls = "\n".join(gallery)
                p.rating = rating
                p.is_active = True
                p.about = about
                p.price = price
                p.sale = sale
                if p.category_id is None:
                    p.category = cat
                p.save()
                if created:
                    created_p += 1
                    ProductReview.objects.get_or_create(
                        product=p,
                        name="Demo mijoz",
                        defaults={"rating": rating, "comment": "Juda sifatli mahsulot!"},
                    )
        self.stdout.write(self.style.SUCCESS(f"Tayyor. Yangi: {created_p}. Rasmlar nomiga mos yangilandi."))
