with open("siir.txt", "r", encoding="utf-8") as file:
    bas_harfler=""
    for satır in file:
        bas_harfler += satır[0]
    print(bas_harfler)


