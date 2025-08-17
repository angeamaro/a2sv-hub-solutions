# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index: int, path: str, value: int, prev: int):
            # Base case: if we've reached the end of the string
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i != index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr = int(curr_str)

                if index == 0:
                    # First number, no operator needed
                    backtrack(i + 1, curr_str, curr, curr)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + curr_str, value + curr, curr)
                    # Subtraction
                    backtrack(i + 1, path + "-" + curr_str, value - curr, -curr)
                    # Multiplication: undo prev, multiply, and re-add
                    backtrack(i + 1, path + "*" + curr_str,
                              value - prev + prev * curr,
                              prev * curr)

        backtrack(0, "", 0, 0)
        return res