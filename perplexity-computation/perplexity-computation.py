def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    N = len(actual_tokens)
    
    log_sum = 0.0
    
    for i in range(N):
        p_i = prob_distributions[i][actual_tokens[i]]
        log_sum += math.log(p_i)
    
    cross_entropy = -log_sum / N
    perplexity = math.exp(cross_entropy)
    
    return perplexity
    