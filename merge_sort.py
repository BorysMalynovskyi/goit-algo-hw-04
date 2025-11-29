class MergeSort:

    @classmethod
    def sort(cls, arr):
        if len(arr) <= 1:
            return arr

        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        return cls.merge(cls.sort(left_half), cls.sort(right_half))

    @staticmethod
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged
