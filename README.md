### Supermarket Pricing Calculator ###

### Description ###

This application models a supermarket pricing calculator using Python. The idea is to implement a programme that allows for various discount structures to be applied to a shopping basket.



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

```shell
$ python main.py

Beans           0.50      
Beans           0.50      
Beans           0.50      
Beans           0.50      
Coke            0.70      
Coke            0.70      
Coke            0.70      
Onions          0.12      
----------
Sub-total: 4.22
----------
Savings
Coke two for £1 -0.40     
Beans 3 for 2   -0.50     
Total savings -0.90
----------
Total to pay: 3.32
```