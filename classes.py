from random import randint

class Item(object):
    def __init__(self, id, name, race, description, rarity, item_type, price, weight):
        self.id = id
        self.name = name
        self.race = race
        self.description = description
        self.rarity = rarity
        self.type = item_type
        self.price = price
        self.weight = weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
class Shop(object):
    def __init__(self, name, level, item_list, race):
        self.name = name
        self.level = level
        self.race = race
        self.item_list = []
        self.build_item_list(item_list)
        print(f"Shop {self.name} has been created with items: \n{self.item_list}")

    def build_item_list(self, item_list):
        # shop_item_list = []
        local_items = self.level + 3
        exotic_items = self.level - randint(int(self.level * .5), self.level)


        item_list.sort(key=lambda x: x.rarity)
        item_list.sort(key=lambda x: x.race)

        item_pointer = 0
        item_rariy_pointer = 1
        while item_pointer < len(item_list):
            if item_list[item_pointer].race == self.race and item_list[item_pointer].rarity == item_rariy_pointer and local_items > 0:
                self.item_list.append(item_list[item_pointer])
                local_items -= 1
                item_list.remove(item_list[item_pointer])
              
            else:
                item_pointer += 1
                if item_pointer == len(item_list) and local_items > 0:
                    item_pointer = 0
                    item_rariy_pointer += 1

        if local_items > 0:
            item_rariy_pointer += 1
            item_pointer = 0
        # print (f"items left: {item_list}")
        if exotic_items > 0:
            for item in item_list:
                if item.rarity <= self.level + 1 and exotic_items > 0:
                    self.item_list.append(item)
                    exotic_items -= 1


        # for item in item_list:
        #     if item.race == self.race and item.rarity == 1 and local_items > 0:
        #         self.item_list.append(item)
        #         item_list.remove(item)
        #         local_items -= 1
        #         print(f"Local Item: {item.name}, and {local_items} left")

        # print(f"\nItems from {self.name}: {self.item_list}")
        # print(f"Items from Shop init:{shops_item_list}")
        # self.item_list = shops_item_list
        
