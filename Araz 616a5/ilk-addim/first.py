print("=== kərpic ===")
row={"cell_id":"BAK-0207","region":"Yasamal","rsrp_dom": -100.1}
row["band"]="LTE800"
print(row)
row["region"]="nizami"
print(row)


x=int(input("istediyiniz ededi daxil edin"))
print("=== kərpic 7===")
rsrp_list=[-91.5,-100.1,-85.1,-100.3,110.4]

for v in rsrp_list:
    print(v * x)