
class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        # Return -1 for error if no string or if it contains anything that isn't ABCD
        ALLOWED_SKUS: str = "ABCD"
        if not set(skus) <= set(ALLOWED_SKUS):
            return -1

        # Count number of each letter
        num_a = skus.count("A")
        num_b = skus.count("B")
        num_c = skus.count("C")
        num_d = skus.count("D")

        # Check for discounts
        num_a_discount_5, num_a = divmod(num_a, 5)
        num_a_discount_3, num_a = divmod(num_a, 3)
        num_b_discount, num_b = divmod(num_b, 2)

        # Add stuff up
        charge_a = num_a * 50
        charge_b = num_b * 30
        charge_c = num_c * 20
        charge_d = num_d * 15
        charge_a_discount = num_a_discount * 130
        charge_b_discount = num_b_discount * 45

        # Return charge
        return charge_a + charge_b + charge_c + charge_d + charge_a_discount + charge_b_discount

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
