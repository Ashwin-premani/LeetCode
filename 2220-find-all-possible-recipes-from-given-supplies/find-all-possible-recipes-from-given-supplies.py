class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Graph (not making)
        can_cook = {s:True for s in supplies}
        recipe_index = {r:i for i, r in enumerate(recipes)}
        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False
            can_cook[r] = False
            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
            can_cook[r] = True
            return can_cook[r]

        return [r for r in recipes if dfs(r)]


        # wrong anser after 50 cases
        # supplies_set = set(supplies)  
        # res = []
        
        # for i in range(len(recipes)):
        #     can_make = True
        #     for j in ingredients[i]:  
        #         if j not in supplies_set:
        #             can_make = False
        #             break
            
        #     if can_make: 
        #         supplies_set.add(recipes[i])
        #         res.append(recipes[i])
                
        # return res