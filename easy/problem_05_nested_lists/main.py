if __name__=='__main__':
    # collecting all the data
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # sorting the data
    scores = []
    for s in students:
        score_only = s[1]
        scores.append(score_only)
    # removing the duplicates
    scores = sorted(list(set(scores)))
    # finding the second lowest score
    second_lowest_score = scores[1]
    # finding the students with the second lowest score
    winners = []
    for s in students:
        if s[1] == second_lowest_score:
            winners.append(s[0])
    # sorting the winners alphabetically
    winners.sort()
    for name in winners:
        print(name)
        
