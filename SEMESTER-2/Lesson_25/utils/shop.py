ITEMS = {
    "dog": 1,
    "cat": 3,
    "crocodile": 1
}
def buy(animal):
    for item, count in ITEMS.items():
        if item == animal and count:
            ITEMS[item] -= 1
            return animal
        
    return "We don't have that animal"

print(buy('cat'))


print(__name__)
