import BookStore

b = BookStore.BookStore()

b.loadCatalog("books.txt")
b.sortUsingMergeSort()
b.searchBookUsingBinarySearch("Tears of the M")
b.searchBookUsingBinarySearch("World of Po")
