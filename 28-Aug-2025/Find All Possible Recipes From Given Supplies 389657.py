# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        ingre = {r : 0 for r in recipes }

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                ingre[recipe] += 1

        q = deque(supplies)
        res = []

        while q:
            item = q.popleft()
            for recipe in graph[item]:
                ingre[recipe] -= 1
                if ingre[recipe] == 0:
                    res.append(recipe)
                    q.append(recipe)
        return res 