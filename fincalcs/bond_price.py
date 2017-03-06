def bond_price(coupon_rate,
               yield_to_maturity,
               years, par_value,
               coupon=(lambda rate, par_value: par_value * rate / 100),
               discount=(lambda value, rate, period: value / (1 + rate) ** period)):
    return sum([discount(coupon(coupon_rate, par_value), yield_to_maturity, p) for p in range(1, years + 1)],
               discount(par_value, yield_to_maturity, years))


bond_prices = lambda coupon_rate, yield_to_maturity, years, par_value: sum(
    map(lambda t: t[0] / (1 + yield_to_maturity) ** t[1],
        (map(lambda p: (par_value * coupon_rate / 100, p),
             [p for p in range(1, years + 1)]))),
    (lambda: par_value / (1 + yield_to_maturity) ** years)())

if __name__ == "__main__":
    print(bond_price(0.05, 0.1, 2, 100))
    print(bond_prices(0.05, 0.1, 2, 100))
