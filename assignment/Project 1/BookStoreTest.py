from BookStore import BookStore

b = BookStore()
b.loadCatalog("books.txt")

# Remove a book from an empty shoppingCart
b.removeFromShoppingCart()

# Add books with index 0, 542683, 271341, 135670, 407012
b.addBookByIndex(0)
b.addBookByIndex(542683)
b.addBookByIndex(271341)
b.addBookByIndex(135670)
b.addBookByIndex(407012)

# Remove all books in shoppingCart using the method removeFromShoppingCart
while(b.removeFromShoppingCart()):continue

# Searching for books by at least the following infix
b.searchBookByInfix("") # Empty infix
b.searchBookByInfix("World of Pa")      # Should display 4 books
b.searchBookByInfix("Tears of the Wo")   # Should display 1 book
