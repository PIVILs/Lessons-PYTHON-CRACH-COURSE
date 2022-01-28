import restaurant

rest = restaurant.Restaurant('жигули', 'пивоварня')
rest.describe_restaurant()

rest.set_number_served(100)
rest.describe_restaurant()

rest.increment_number_served(100)
rest.describe_restaurant()

my_cream = restaurant.IceCreamStand('жигули', 'пивоварня')
my_cream.describe_restaurant()
my_cream.icecream()

