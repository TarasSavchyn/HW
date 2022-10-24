class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitor_num = 50

    def __setattr__(self, key, value):
        if key == 'visitors_count' and value < self.max_visitor_num:
            return object.__setattr__(self, key, value)
        return object.__setattr__(self, key, self.max_visitor_num)



Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.__dict__)
print(concert.visitors_count)
