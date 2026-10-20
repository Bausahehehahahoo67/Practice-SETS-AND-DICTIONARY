from pyscript import document, display

set_1 = {"Fries", "Burger", }
set_2 = {"Fries", "Burger", "Coke", "Applepie"}

display(set_1 <= set_2, target = "result") # Subset gives out true because fries and burger are found on both
display(set_1 < set_2, target = "result") # Proper Subset gives out true because set_2 has ALL elements of set_1 (Fries and Burger) and MORE (Coke, Applepie). Unlike <=/Subset where it generally only looks for similar elements, not ALL + MORE.
display(set_2 >= set_1, target = "result") # Superset checks if all the elements of 2nd set (set_1) is found in 1st set (set_2), which is true. 
display(set_2 > set_1, target = "result") # Proper Superset true because the same as Proper subset, all and more are present hence true