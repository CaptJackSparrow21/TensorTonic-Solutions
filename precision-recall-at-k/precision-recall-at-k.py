def precision_recall_at_k(recommended, relevant, k):
    top_k = recommended[:k]
    relevant_items = set(relevant)
    hits = sum(item in relevant_items for item in top_k)
    precision = hits / k
    recall = hits / len(relevant_items)
    return [precision, recall]
