#A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
#Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
#Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
#Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

#APPROACH

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
      
        #We will first sort the list in reverse order to get the maximum satisfaction first.
        satisfaction.sort(reverse=True)
        
        #we will check the sum of the values in the list which if less than 0 we will pop the last element.
        while sum(satisfaction)<0:
            satisfaction.pop()
            
        #Then finally we will calculate the total satisfaction.    
        total=0
        l=len(satisfaction)
        for i in range(l):
            total+=satisfaction[i]*(l-i)
        return total
