
class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        # Return -1 for error if no string or if it containts anything that isn't ABCD
        ALLOWED_SKUS: str = "ABCD"
        if not skus or set(skus) <= set(ALLOWED_SKUS):
            return -1

        # Count number of each letter
        num_a = skus.count("A")
        num_b = skus.count("B")
        num_c = skus.count("C")
        num_d = skus.count("D")

        # Check for discounts
        num_a_discount, num_a = num_a /

        # Add stuff up

        # Return charge

# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


