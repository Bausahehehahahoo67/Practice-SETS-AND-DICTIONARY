from pyscript import document, display

set_1 = {"Fries", "Burger", }
set_2 = {"Fries", "Burger", "Coke", "Applepie"}

#display(set_1 <= set_2, target = "result") #Subset gives out true because fries and burger are found on both
display(set_1 < set_2, target = "result") # Proper Subset gives out true because set_2 has ALL elements of set_1 (Fries and Burger). Unlike <=/Subset where it generally only looks for similar elements, not ALL.