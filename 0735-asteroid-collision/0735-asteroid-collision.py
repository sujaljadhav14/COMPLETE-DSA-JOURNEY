class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while stack and stack[-1]>0 and i <0:
                if abs(stack[-1])<abs(i):
                    stack.pop()
                elif abs(stack[-1])==abs(i):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive=False
                    break
            if alive:
                stack.append(i)
        return stack
