# Get the current properties for rent in Dublin that are between 1000 and 1500 per month.

from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(listing.get_contact_number())
    print(listing.get_views())
    facilities = listing.get_facilities()
    if facilities is not None:
        print('Facilities: ')

        for facility in facilities:
            print(facility)

    features = listing.get_features()
    if features is not None:
        print('Features: ')
        for feature in features:
            print(feature)

    print("")