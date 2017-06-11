import unittest
import time
from daftlistings import Daft, SaleType, RentType, SortOrder, SortType, CommercialType


class DaftTests(unittest.TestCase):

    def test_properties(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sale_agreed(True)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(200000)
        daft.set_max_price(250000)
        daft.set_sale_agreed(True)
        listings = daft.get_listings()

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)
        self.assertTrue('Dublin 15' in listing.get_formalised_address())

    def test_properties_sale_agreed_with_invalid_prices(self):
        daft = Daft()
        raised_exception = False
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sale_agreed(True)

        try:
            daft.set_min_price("Two")
            daft.set_max_price("")
            daft.get_listings()
        except:
            raised_exception = True

        self.assertTrue(raised_exception)

    def test_properties_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(200000)
        daft.set_max_price(250000)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)

    def test_apartments_to_let(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(RentType.APARTMENTS)
        listings = daft.get_listings()

        self.assertTrue(len(listings) > 0)

    def test_apartments_to_let_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_min_price(1000)
        daft.set_max_price(2000)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        if 'week' or 'month' in price:
            price = price.split()
            price = price[0]
        self.assertTrue(1000 <= int(price) <= 2000)

    def test_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(SaleType.COMMERCIAL)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)

    def test_area_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.COMMERCIAL)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)

    def test_commercial_property_types(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        listings = daft.get_listings()
        self.assertTrue(len(listings) > 0)

    def test_commercial_properties_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        daft.set_min_price(150000)
        listings = daft.get_listings()
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')

        self.assertTrue(int(price) >= 150000)

    def test_sort_by_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        daft.set_sort_by(SortType.PRICE)
        listings = daft.get_listings()
        listing = listings[0]
        price = listing.get_price()

        if "AMV" in price:
            price = price[6:]
        else:
            price = price[1:]
        print price
        price = price.replace(',', '')
        self.assertTrue(len(listings) > 0)
        self.assertTrue(int(price) <= 175000)

    def test_sort_by_date_descending(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sort_order(SortOrder.DESCENDING)
        daft.set_sort_by(SortType.DATE)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        listings = daft.get_listings()

        first = listings[0].get_posted_since().split()
        last = listings[-1].get_posted_since().split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date > last_date)

    def test_sort_by_date_ascending(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sort_order(SortOrder.ASCENDING)
        daft.set_sort_by(SortType.DATE)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        listings = daft.get_listings()

        first = listings[0].get_posted_since().split()
        last = listings[-1].get_posted_since().split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date < last_date)
