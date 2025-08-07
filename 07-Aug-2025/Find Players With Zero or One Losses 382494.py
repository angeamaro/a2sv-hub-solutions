# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        players = set()

        zero = []
        one = []
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1
        
        for player in players:
            if player not in losses:
                zero.append(player)
            elif losses[player] == 1:
                one.append(player)

        return[sorted(zero),sorted(one)] 

            

        