class ChallengeTwo():

    # Define the product_except_self method
    def product_except_self(self, arr):
        # Assign an array the same length as arr
        right_mult = [0] * len(arr)
        # assigning the last index of arr to right_mult's last index
        right_mult[-1] = arr[-1]

        for i in range(1, len(arr)):
            right_mult[len(arr) - i - 1] = right_mult[len(arr) -
                                                      i] * arr[len(arr) - i - 1]
        result = [0] * len(arr)
        pref = 1
        index = 0
        while index < len(result) - 1:
            result[index] = pref * right_mult[index+1]
            pref *= arr[index]
            index += 1
        result[-1] = pref
        return result
