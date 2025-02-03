### Supermarket Pricing Calculator ###

### Description ###

This application models a supermarket pricing calculator using Python. The idea is to implement a programme that allows for various discount structures to be applied to a shopping basket.

screenshots?

### Features ###

* Calculate pricing for individual fixed price/weighed items
* Create multibuy discounts using `Offer` class
* Calculate savings using `OfferCalculator`
* Calculate subtotal (pre discount) and total (with discounts applied)

### Challenges and future improvements ###

With more time and resources, further improvements would include:
* Handle products in a more scalable way, such as in a database
* Handle mutually exclusive discounts
* Handle various customer tiers and loyalty cards
* Handle vouchers that exclude certain items (such as alcohol)


### Installation ###

* Clone this repository
* to run tests `python -m unittest discover ./tests`
* to run example main script `python main.py`