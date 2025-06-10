# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

import math

class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = int(pageSize)  
        self.totalItems = len(items) 
        self.totalPages = math.ceil(self.totalItems / self.pageSize)  
        self.currentPage = 1  
    def getVisibleItems(self):
        
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]
    
    def prevPage(self):
        
        if self.currentPage > 1:
            self.currentPage -= 1
        return self
    
    def nextPage(self):
       
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self
    
    def firstPage(self):
       
        self.currentPage = 1
        return self
    
    def lastPage(self):
        
        self.currentPage = self.totalPages
        return self
    
    def goToPage(self, pageNum):
        
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  

p.nextPage()
print(p.getVisibleItems())  

p.lastPage()
print(p.getVisibleItems())  

p.firstPage()
print(p.getVisibleItems())  

p.goToPage(3)
print(p.getVisibleItems())  

p.goToPage(10)  
print(p.getVisibleItems()) 