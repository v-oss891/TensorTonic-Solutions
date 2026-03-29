def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    arr=[]
    for word in tokens:
        if word not in stopwords:
            arr.append(word)
    return arr
            
            