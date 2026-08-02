mahsulotlar=[
     "un",
    "yog'",
    "sovun",
    "tuxum",
    "piyoz",
    "kartoshka",
    "olma",
    "banan",
    "uzum",
    "qovun",
    ]
savat=[]
print("5ta Mahsulot kiriting")
for k in range(5):
    savat.append(input(f"{k+1}-Mahsulotni qo'shing: ").lower())
if savat:
    for n in savat:
        if n in mahsulotlar:
            print(f"Do'konimizda {n} bor")
        else:
            print(f"Do'konimizda {n} yo'q")
else:
     print("savat bo'sh")