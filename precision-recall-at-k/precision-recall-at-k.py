def precision_recall_at_k(recommended, relevant, k) :
    relevant_items = set(relevant)
    if k <= 0 :
        return [0.0, 0.0]

    top_k = recommended[:k]
    hits = sum(item in relevant_items for item in top_k)
    precision = hits / k
    recall = hits / len(relevant_items) if relevant_items else 0.0

    return [precision, recall]