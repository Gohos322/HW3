class BubbleSort:

    def __init__(self, quick=False):
        self.content=[]
        self.quick=quick    
    
    def append (self, value):
        self.content.append(value)
        self._sort()

    def _sort(self):
        lst=self.content
        _moved=False
        for passnum in range(len(lst)-1,0,-1):
            for i in range(passnum):
                _moved=False
                if lst[i]>lst[i+1]:
                    temp = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = temp
                    _moved=True
            if _moved==False and self.quick==True:
                break

    def getMin(self):
        return self.content[0]
    
    def getMax(self):
        return self.content[-1]

    def getClassName(self):
        return ("BubbleSort" if self.quick==False else "QuickBubbleSort")
    
    def clean(self):
        self.content=[]

