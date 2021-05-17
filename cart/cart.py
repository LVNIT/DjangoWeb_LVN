from decimal import  Decimal

from store.models import Shoe


class Cart():
    '''
    A Cart class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    '''


    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, shoes, qty ):
        '''
        Adding and updating the users basket session data

        '''
        shoe_id = str(shoes.id)

        if shoe_id in self.cart:
            self.cart[shoe_id]['qty'] += qty
        else:
            self.cart[shoe_id] = {'price': str(shoes.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        Collect the shoe_id in the session data to query the database
        :return: shoe
        """
        shoe_ids = self.cart.keys()
        shoes = Shoe.objects.filter(id__in=shoe_ids)
        cart = self.cart.copy()

        for shoe in shoes:
            cart[str(shoe.id)]['shoe'] = shoe

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        '''
        get the basket data and count the qty of items

        '''
        return sum(item['qty'] for item in self.cart.values())

    def update(self, shoe, qty):
        '''
        :param shoe:
        :param qty:
        :return:  Update values in session data
        '''

        shoe_id = str(shoe.id)
        if shoe_id in self.cart:
            self.cart[shoe_id]['qty'] = qty
        self.save()


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self,shoe):
        '''

        :param shoe:
        :return: Delete item from session data
        '''
        shoe_id = str(shoe.id)

        if shoe_id in self.cart:
            del self.cart[shoe_id]
            self.save()

    def clear(self):
        del self.session['skey']
        self.save()

    def save(self):
        self.session.modified = True

