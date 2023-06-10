staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}
def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    
    try: 
        ratio = sales_people / managers
    except ZeroDivisionError: 
        print('Ratio is undefined.')
        return
        
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()
try:
    for location, staff in staff.items():
        # Write your code below:
        print_staff_report(location, staff)
except KeyError:
    print('Invalid key used.')

class OutOfStockError(Exception):
    def __init__(self, supply):
        self.supply = supply

    def __str__(self):
        return "We don't " + str(self.supply) + ' in stock'


inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}


def submit_order(instr, quant):
    try:
        sup = inventory[instr]
        if sup < quant:
            raise OutOfStockError(quant)
        inventory[instr] -= quant
        print('Successfully placed order! Remaining supply: ' + str(inventory[instr]))
    except OutOfStockError as err:
        print(err)


instr = 'Guitar'
quant = 5
submit_order(instr, quant)