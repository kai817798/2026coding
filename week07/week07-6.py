#LeetCode 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        print(senate,type(senate))
        print(list(senate),type(list(senate)))
        queue = deque(list(senate))
        print(queue,type(queue))

        banR,banD = 0,0
        R,D = senate.count('R'),senate.count('D')
        while queue:
            now = queue.popleft()
            if now=='R':
                if banR>0:
                    banR -= 1
                    R -= 1
                else:
                    banD += 1
                    queue.append(now)
            else:
                if banD > 0:
                    banD -= 1
                    D -=  1
                else:
                    banR += 1
                    queue.append(now)
            if R==0: return 'Dire'
            if D==0: return 'Radiant'
