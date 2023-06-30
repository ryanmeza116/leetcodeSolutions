# Given a list of scores, determine the second highest score. 

# 1) Reduce list to set 
# 2) Loop through, create value to be highest and second highest. 
# 3) return second highest 

def runner_up(list):
    scores = set(list)
    print(scores)
    highest = 0
    runner_up = 0
    for i in scores: 
        if i > highest:
            highest = i
    for j in scores:
        if j > runner_up and j < highest:
            runner_up = j
    return runner_up


print(runner_up([1,2,3,4,5,3,2,3,4,5,6,7]))

# Another solution: 
if __name__ == '__main__':

    n=input()
    a=map(int,input().split())
    a=list(set(a))
    a.remove(max(a))
    print (max(a))