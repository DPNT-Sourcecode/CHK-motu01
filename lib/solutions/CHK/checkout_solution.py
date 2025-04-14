class CheckoutSolution:
    ALLOWED_SKUS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50 }
    def checkout(self, skus: str) -> int:
        # Return -1 for error if no string or if it contains anything that isn't in ALLOWED_SKUS
        
        if not set(skus) <= set(self.ALLOWED_SKUS):
            return -1

        # Count number of each letter
        sku_counts = {sku: skus.count(sku) for sku in set(self.ALLOWED_SKUS)}

        # Apply freebie count reductions
        #2E get one B free
        sku_counts['B'] = max(sku_counts['B'] - sku_counts['E'] // 2, 0)
        #3N get one M free
        sku_counts['M'] = max(sku_counts['M'] - sku_counts['N'] // 3, 0)
        #3R get one Q free
        sku_counts['Q'] = max(sku_counts['Q'] - sku_counts['R'] // 2, 0)

        # Calculate price for each SKU



        # Total it all

        # Return it



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


# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 | multibuy discount
# | B    | 30    | 2B for 45              | multibuy discount
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      | freebie
# | F    | 10    | 2F get one F free      | multibuy discount
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  | multibuy discount
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             | multibuy discount
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      | freebie
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             | multibuy discount
# | Q    | 30    | 3Q for 80              | multibuy discount
# | R    | 50    | 3R get one Q free      | freebie
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      | multibuy discount
# | V    | 50    | 2V for 90, 3V for 130  | multibuy discount
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+



prices = {
'A': lambda x: x * 50,
'B': lambda x: x * 30,
'C': lambda x: x * 20,
'D': lambda x: x * 15,
'E': lambda x: x * 40,
'F': lambda x: x * 10,
'G': lambda x: x * 20,
'H': lambda x: x * 10,
'I': lambda x: x * 35,
'J': lambda x: x * 60,
'K': lambda x: x * 80,
'L': lambda x: x * 90,
'M': lambda x: x * 15,
'N': lambda x: x * 40,
'O': lambda x: x * 10,
'P': lambda x: x * 50,
'Q': lambda x: x * 30,
'R': lambda x: x * 50,
'S': lambda x: x * 30,
'T': lambda x: x * 20,
'U': lambda x: x * 40,
'V': lambda x: x * 50,
'W': lambda x: x * 20,
'X': lambda x: x * 90,
'Y': lambda x: x * 10,
'Z': lambda x: x * 50,
}
