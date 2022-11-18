aisles={

"aisle_1":{"description":"Produce Aisle","section_1":{"description":"Section 1", "items":[]},"section_2":{"description":"Section 2", "items":[]},"section_3":{"description":"Section 3", "items":[]},"section_4":{"description":"Section 4", "items":[]},"section_1":{"description":"Section 5", "items":[]}},
"aisle_2":{"description":"Baking Aisle","section_1":{"description":"Section 1", "items":[]},"section_2":{"description":"Section 2", "items":[]},"section_3":{"description":"Section 3", "items":[]},"section_4":{"description":"Section 4", "items":[]},"section_1":{"description":"Section 5", "items":[]}},
"aisle_3":{"description":"Dairy Aisle","section_1":{"description":"Section 1", "items":[]},"section_2":{"description":"Section 2", "items":[]},"section_3":{"description":"Section 3", "items":[]},"section_4":{"description":"Section 4", "items":[]},"section_1":{"description":"Section 5", "items":[]}},
"aisle_4":{"description":"Frozen Food Aisle","section_1":{"description":"Section 1", "items":[]},"section_2":{"description":"Section 2", "items":[]},"section_3":{"description":"Section 3", "items":[]},"section_4":{"description":"Section 4", "items":[]},"section_1":{"description":"Section 5", "items":[]}},
"aisle_5":{"description":"Canned Food Aisle","section_1":{"description":"Section 1", "items":[]},"section_2":{"description":"Section 2", "items":[]},"section_3":{"description":"Section 3", "items":[]},"section_4":{"description":"Section 4", "items":[]},"section_1":{"description":"Section 5", "items":[]}},

}


map = [
{"aisle_0":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_1":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_2":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_3":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_4":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_5":["section_1","section_2","section_3","section_4","section_5",]},
{"aisle_6":["section_1","section_2","section_3","section_4","section_5",]}
]
##current aisle (num)
## current section (num)

### input = n
### if current aisle not equal to 0 or 6 current section -=1 .
## if current aisle <1 || >5 current aisle ++ 

##

# if input == "Search"
#  for item in grocery list 
#     if item in aisle section
#         print "you found" + item