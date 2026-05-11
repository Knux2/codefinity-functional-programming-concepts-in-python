def format_scores(names, scores):
    scores_list = []
    for idx, (name, score) in enumerate(zip(names, scores), start=1):
        formatted = f"{idx}. {name} scored {score}"
        scores_list.append(formatted)
    return scores_list    
    
result = format_scores(["Alice", "Bob", "Charlie"], [85, 92, 78])
print(result)