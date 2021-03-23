class CheckSums:
    potential_solutions = {}
    array = [10, 14, 2, 3]

    def checksums(self, k):
        for num in self.array:
            if num in self.potential_solutions:
                return True
            if k - num in self.array:
                self.potential_solutions[k - num] = num
                print(self.potential_solutions)
        return False
