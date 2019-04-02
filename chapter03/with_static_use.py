class BookPriceCalculator:
    PER_PAGE_PRICE = 8

    def __init__(self, pages, author):
        self.pages = pages
        self.author = author

    @property
    def standard_price(self):
        return self.pages * PER_PAGE_PRICE


    @staticmethod
    def price_to_book_ratio(market_price_per_share, book_value_per_share):
        return market_price_per_share/book_value_per_share
