class Solution:
    def romanToInt(self, s: str) -> int:
        arr1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arr2 = []

        for n in s:
            arr2.append(arr1[n])

        arr = []

        i = 0
        while i < len(arr2):

            if i == len(arr2) - 1:
                arr.append(arr2[i])
                i =+1
                break

            for j in range(i+1, len(arr2)):

                if i == len(arr2) - 1:
                    arr.append(arr2[i])
                elif arr2[j] == (arr2[i] * 5) or arr2[j] == (arr2[i] * 10):
                    x = arr2[j]-arr2[i]
                    i = i + 1
                    arr.append(x)
                    break
                else:
                    arr.append(arr2[i])
                    break

            i = i + 1
        answer = 0
        for i in arr:
            answer = answer + i

        return answer
 

