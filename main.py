#
#   By: Keith Averre, 7/11/2022
#
#   This program is made to calculate income after tax according to the IRS 2022 marginal tax brackets for individuals
#   Input: Untaxed total expected income for the year 2022 in integer or decimal form
#   Output:
#
#

import sys


def tax_taken(v1, v2, v3, v4, v5, v6, v7):
    print("\n\nTotal tax removed:")
    if v1 != 0.0:
        print("${} taken out at bracket {}".format(v1, 1))
    if v2 != 0.0:
        print("${} taken out at bracket {}".format(v2, 2))
    if v3 != 0.0:
        print("${} taken out at bracket {}".format(v3, 3))
    if v4 != 0.0:
        print("${} taken out at bracket {}".format(v4, 4))
    if v5 != 0.0:
        print("${} taken out at bracket {}".format(v5, 5))
    if v6 != 0.0:
        print("${} taken out at bracket {}".format(v6, 6))
    if v7 != 0.0:
        print("${} taken out at bracket {}".format(v7, 7))
    print("Total: ${}".format(v1 + v2 + v3 + v4 + v5 + v6 + v7))
    return 1


def main(argv):
    if len(argv) < 2:
        raise Exception("Missing arguments, exiting...")
    if len(argv) > 2:
        raise Exception("Too many arguments, exiting...")

    print("User Input: {}".format(argv[1:]))
    pre_tax_income: float = float(argv[1])

    if pre_tax_income <= 0.0:
        raise ValueError("\nOnly positive values are allowed... exiting")

    running_total: float = pre_tax_income
    after_tax_income: float = 0.0
    # Stupid numpy and pycharm things...
    # Recording tax reductions
    tax_taken_out_1 = 0.0
    tax_taken_out_2 = 0.0
    tax_taken_out_3 = 0.0
    tax_taken_out_4 = 0.0
    tax_taken_out_5 = 0.0
    tax_taken_out_6 = 0.0
    tax_taken_out_7 = 0.0

    # 1st tax bracket
    if running_total < 10275.0:
        tax_taken_out_1 = running_total / 100 * 10
        after_tax_income = after_tax_income + running_total - tax_taken_out_1
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_1 = 10275.0 / 100.0 * 10
    after_tax_income = after_tax_income + 10275.0 - tax_taken_out_1
    running_total -= 10275.0

    # 2nd tax bracket
    if running_total < (41775.0 - 10275.0):
        tax_taken_out_2 = running_total / 100 * 12
        after_tax_income = after_tax_income + running_total - tax_taken_out_2
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_2 = (41775.0 - 10275.0) / 100.0 * 12
    after_tax_income = after_tax_income + (41775.0 - 10275.0) - tax_taken_out_2
    running_total -= (41775.0 - 10275.0)

    # 3rd tax bracket
    if running_total < (89075 - 41775):
        tax_taken_out_3 = running_total / 100 * 22
        after_tax_income = after_tax_income + running_total - tax_taken_out_3
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_3 = (89075 - 41775) / 100.0 * 22
    after_tax_income = after_tax_income + (89075 - 41775) - tax_taken_out_3
    running_total -= (89075 - 41775)

    # 4th tax bracket
    if running_total < (170050 - 89075):
        tax_taken_out_4 = running_total / 100 * 24
        after_tax_income = after_tax_income + running_total - tax_taken_out_4
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_4 = (170050 - 89075) / 100.0 * 24
    after_tax_income = after_tax_income + (170050 - 89075) - tax_taken_out_4
    running_total -= (170050 - 89075)

    # 5th tax bracket
    if running_total < (215950 - 170050):
        tax_taken_out_5 = running_total / 100 * 32
        after_tax_income = after_tax_income + running_total - tax_taken_out_5
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_5 = (215950 - 170050) / 100.0 * 32
    after_tax_income = after_tax_income + (215950 - 170050) - tax_taken_out_5
    running_total -= (215950 - 170050)

    # 6th tax bracket
    if running_total < (539900 - 215950):
        tax_taken_out_6 = running_total / 100 * 35
        after_tax_income = after_tax_income + running_total - tax_taken_out_6
        tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
                  tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
        print("After tax income: ${}".format(after_tax_income))
        return 1
    tax_taken_out_6 = (539900 - 215950) / 100.0 * 35
    after_tax_income = after_tax_income + (539900 - 215950) - tax_taken_out_6
    running_total -= (539900 - 215950)

    # 7th tax bracket
    tax_taken_out_7 = running_total / 100 * 37
    after_tax_income = after_tax_income + running_total - tax_taken_out_7

    tax_taken(tax_taken_out_1, tax_taken_out_2, tax_taken_out_3,
              tax_taken_out_4, tax_taken_out_5, tax_taken_out_6, tax_taken_out_7)
    print("After tax income: ${}".format(after_tax_income))
    return 1

# Marginal Rates: For tax year 2022, the top tax rate remains 37% for individual single taxpayers with incomes greater
#       than $539,900 ($647,850 for married couples filing jointly).
# The other rates are:
# 35%, for incomes over $215,950 ($431,900 for married couples filing jointly);
# 32% for incomes over $170,050 ($340,100 for married couples filing jointly);
# 24% for incomes over $89,075 ($178,150 for married couples filing jointly);
# 22% for incomes over $41,775 ($83,550 for married couples filing jointly);
# 12% for incomes over $10,275 ($20,550 for married couples filing jointly).
# The lowest rate is 10% for incomes of single individuals with incomes of $10,275 or less ($20,550 for married couples
#       filing jointly).

if __name__ == '__main__':
    main(sys.argv[0:])
#   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
