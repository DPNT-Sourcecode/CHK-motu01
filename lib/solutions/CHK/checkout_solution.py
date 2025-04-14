class CheckoutSolution:
    ALLOWED_SKUS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50 }
    def checkout(self, skus: str) -> int:
        # Return -1 for error if no string or if it contains anything that isn't ABCD
        
        if not set(skus) <= set(self.ALLOWED_SKUS):
            return -1

        {sku: skus.count(sku) for sku in set(self.ALLOWED_SKUS)}

        # Count number of each letter
        num_a = skus.count("A")
        num_b = skus.count("B")
        num_c = skus.count("C")
        num_d = skus.count("D")
        num_e = skus.count("E")
        num_f = skus.count("F")

        # Apply the E discount on number of B to a minimum B of 0
        num_b = max(num_b - num_e // 2, 0)

        # Check for discounts
        num_a_discount_5, num_a = divmod(num_a, 5)
        num_a_discount_3, num_a = divmod(num_a, 3)
        num_b_discount, num_b = divmod(num_b, 2)
        num_f_discount, num_f = divmod(num_f, 3)

        # Add stuff up
        charge_a = num_a * 50
        charge_b = num_b * 30
        charge_c = num_c * 20
        charge_d = num_d * 15
        charge_e = num_e * 40
        charge_f = num_f * 10
        charge_a_discount_5 = num_a_discount_5 * 200
        charge_a_discount_3 = num_a_discount_3 * 130
        charge_b_discount = num_b_discount * 45
        charge_f_discount = num_f_discount * 20

        # Return charge
        return charge_a + charge_b + charge_c + charge_d + charge_e + charge_f + charge_a_discount_3 + charge_a_discount_5 + charge_b_discount + charge_f_discount


{'A': 50
 'B': 30
 'C': 20
 'D': 15
 'E': 40
 'F': 10
 'G': 20
 'H': 10
 'I': 35
 'J': 60
 'K': 80
 'L': 90
 'M': 15
 'N': 40
 'O': 10
 'P': 50
 'Q': 30
 'R': 50
 'S': 30
 'T': 20
 'U': 40
 'V': 50
 'W': 20
 'X': 90
 'Y': 10
 'Z': 50


# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+