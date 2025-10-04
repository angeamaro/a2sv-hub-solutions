# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.price_map = {p: pr for p, pr in zip(products, prices)}

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        total = sum(self.price_map[p] * a for p, a in zip(product, amount))

        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100.0

        return total
