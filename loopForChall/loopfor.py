farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

yuck =["carrots","celery"]

num =input("""
        choose farm by number:
        0. NE Farm
        1. W Farm
        2. SE Farm
        >"""
num=int(num)

         for critters in farms[num].get("agriculture"):
            if critters not in yuck:
                print(critters)
