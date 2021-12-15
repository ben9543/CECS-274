import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import DLList
import MaxStack

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = DLList.DLList()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedPrefix = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.similaGraph = AdjacencyList.AdjacencyList(0)
        self.bestSellers = BinaryHeap.BinaryHeap()
        
    # Lab 4
    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            count = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                sb = SortableBook.SortableBook(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.bookSortedCatalog.append(sb)
                self.indexKey.add(key, self.bookCatalog.size()-1)
                self.indexSortedPrefix.add(title, self.bookCatalog.size()-1)

            # The following line is used to calculate the total time 
            # of execution
            self.similaGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
            for i in range(self.bookCatalog.size()):
                l = self.bookCatalog[i].similar.split()
                for k in range(1, len(l)):
                    j = self.indexKey.find(l[k])
                    if j is not None:
                        self.similaGraph.add_edge(j, i)
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        return self.bookCatalog.size()

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, s : str) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with key s
        input: 
            s: key string    
        '''
        index = self.indexKey.find(s)
        if index != None: self.addBookByIndex(index)

    # Lab 5
    def addBookByPrefix(self, s : str) :
        '''
        addBookByPrefix: Inserts into the shopping cart the book with prefix s
        input: 
            s: Prefix
        '''
        # Validating the index. Otherwise it  crashes
        b = self.indexSortedPrefix.find(s)
        if b is not None:
            self.addBookByIndex(b)

    def pathLength(self, s1: str, s2: str) :
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similaGraph.distance(i, j)
        print(f"{s1} and {s2} are at distance {distance}")
        return distance

    # Lab 5
    def searchBookByInfix(self, infix : str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string 
        returns: 
            the number of books that contains infix in its title   
        '''
        exists = False
        for book in self.bookCatalog:
            if infix in book.title:
                print(book)
                r = self.similaGraph.out_edges(self.indexKey.find(book.key))
                for each_index in r:
                    print("Similar: ", self.bookCatalog[each_index])
                exists = True
        return exists

    def sortUsingMergeSort(self) :
        algorithms.merge_sort(self.bookSortedCatalog)

    
    def sortUsingQuickSort(self) :
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix : str) :
        s = SortableBook.SortableBook(0, prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, self.bookSortedCatalog.size()-1, s)
        if j != -1:
            print(self.bookSortedCatalog[j])
        else: print("No result")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            return u