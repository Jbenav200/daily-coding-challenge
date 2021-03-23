class CheckSums:
    potential_solutions = {}
    array = [10, 14, 2, 3]

    def checksums(self, k):
        for num in self.array:
            if num in self.potential_solutions:
                return f'The array contains two numbers which add up to {k}'
            if k - num in self.array:
                self.potential_solutions[k - num] = num
                print(f'{k-num} => {self.potential_solutions[k-num]} \n')
        return f'The array does not contain two numbers which add up to {k}'
