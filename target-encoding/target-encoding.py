def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    t = {}
    for cat, tar in zip(categories, targets):
        if cat in t:
            t[cat][0] += 1
            t[cat][1] += tar
        else:
            t[cat] = [1, tar]

    for index, category in enumerate(categories):
        cat_index = t[category]
        categories[index] = float(cat_index[1] / cat_index[0])

    return categories