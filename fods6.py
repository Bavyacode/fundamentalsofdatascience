Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: C:\Users\mbavy\.py =========================
Enter price of item 1:34
Enter price of item 2:45
Enter price of item 3:44
Enter price of item 4:56
Enter price of item 5:32
Enter item 1 quantity:3
Enter item 2 quantity:4
Enter item 3 quantity:2
Enter item 4 quantity:5
Enter item 5 quantity:6
Discount10
Tax8
Total Cost before discounts and taxes: $ 842
Total Discount Amount: $ 84.2
Total Cost after discounts: $ 757.8
Total Tax Amount: $ 60.623999999999995
Final Total Cost including taxes: $ 818.424
>>> 
========================== RESTART: C:\Users\mbavy\.py =========================
Enter price of item 1:300
Enter price of item 2:200
Enter price of item 3:400
Enter price of item 4:500
Enter price of item 5:100
Enter item 1 quantity:2
Enter item 2 quantity:3
Enter item 3 quantity:4
Enter item 4 quantity:
Traceback (most recent call last):
  File "C:\Users\mbavy\.py", line 5, in <module>
    item_quantities = np.array([int(input(f"Enter item {j+1} quantity:")) for j in range(items)])
  File "C:\Users\mbavy\.py", line 5, in <listcomp>
    item_quantities = np.array([int(input(f"Enter item {j+1} quantity:")) for j in range(items)])
ValueError: invalid literal for int() with base 10: ''
>>> 
========================== RESTART: C:\Users\mbavy\.py =========================
Enter price of item 1:200
Enter price of item 2:300
Enter price of item 3:100
Enter price of item 4:400
Enter price of item 5:500
Enter item 1 quantity:5
Enter item 2 quantity:4
Enter item 3 quantity:3
Enter item 4 quantity:2
Enter item 5 quantity:1
Discount15
Tax9
Total Cost before discounts and taxes: $ 3800
Total Discount Amount: $ 570.0
Total Cost after discounts: $ 3230.0
Total Tax Amount: $ 290.7
Final Total Cost including taxes: $ 3520.7
>>> 
=================================================================== RESTART: C:\Users\mbavy\.py ===================================================================
