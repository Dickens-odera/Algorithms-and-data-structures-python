class Algorithms:
    def __init__(self):
        self.A = [8,6,3,1,9,2,5,7,4,10,0] #The list of the numbers to be sorted in ascending order
    #insertion sort using a for loop
    def insertionSort1(self):
        for i in range(1, len(self.A)):
            for j in range(i - 1, 0, -1):
                if self.A[j] > self.A[j + 1]:
                    self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]
                    print(self.A)
                else:
                    break
    #insertion sort using a while loop
    def insertionSort2(self):
        for i in range(1, len(self.A)):
            j = i -1
            while self.A[j] > self.A[j + 1] and j >= 0:
                self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]
                j -= 1
                print(self.A)

    #Bubble sort algorithm
    def bubbleSort(self):
       n = len(self.A)
       for i in range(n):
           for j in range(0, n - i - 1):
                if self.A[j] > self.A[j + 1]:
                   self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]

       print(self.A)
#run the application by creating an instance of the Algorithms class and calling it's method
if __name__ == "__main__":
    algorithms = Algorithms()
    print("Insertion sort")
    algorithms.insertionSort2()
    print("Bubble sort")
    algorithms.bubbleSort()
        