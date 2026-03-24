def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    
    """
    n=len(relevant)
    recommended=recommended[:k]
    count=0
    for i in recommended:
        if i in relevant:
            count+=1
    p=count/k
    r=count/n
    return [p,r]
    
    
    