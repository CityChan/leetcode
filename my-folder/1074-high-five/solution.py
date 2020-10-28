class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        result = []
        for x in items:
            # for every student, create a list of their scores using dictionary
            # 类似Java的HashMap, student as the key, list of scores as the value
            if x[0] in mapping:
                mapping[x[0]].append(x[1])
            else:
                mapping[x[0]] = [x[1]]

        # traverse through the dictionary elements and take average of the sorted scores
        for x, y in mapping.items():
            y.sort(reverse=True)
            total = 0
            i = 0
            # there might be less than 5 scores for each student
            while i < 5 and i < len(y):
                total += y[i]
                i += 1
            # store the average for every student id into result
            result.append([x, total//i])
        return result
