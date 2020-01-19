class Algorithms:
    def __init__(self):
        self.A = [8,6,3,1,9,2,5,7,4,10,0]
        
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

if __name__ == "__main__":
    algorithms = Algorithms()
    algorithms.insertionSort2()
