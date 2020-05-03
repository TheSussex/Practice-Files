foodstuffs = ["Rice", "Beans", "Garri", "Yam", "Spaghetti"]
beverages = ["Milk", "Sugar", "Milo"]
# modified garri
foodstuffs[2] = "Noodles"
# add beverages to foodstuffs
foodstuffs.extend(beverages)
# added semovita to the end of the list
foodstuffs.append("Semovita")
# added coffee as 6th item
foodstuffs.insert(6, "Coffee")
# use .remove to delete a specific item
foodstuffs.remove("Beans")
# use pop to remove the last item in the list
foodstuffs.pop()
# use index to know if an item is in a list
foodstuffs.index("Noodles")
# use sort to put in alphabetical order
foodstuffs.sort()
foodstuffs2 = foodstuffs.copy()
print(foodstuffs2)