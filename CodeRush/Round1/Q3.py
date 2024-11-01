def sort_scores_and_names(n_param, scores_param, names_param):
    # Step 1: Create two empty lists to store the combined scores and names
    combined_scores = []
    combined_names = []
    
    # Step 2: Manually combine scores and names into separate lists
    for i in range(n_param):
        combined_scores.append(scores_param[i])
        combined_names.append(names_param[i])
    
    # Step 3: Implement bubble sort manually to sort the combined lists by score first, then by name
    for i in range(n_param):
        for j in range(0, n_param - i - 1):
            # Sort by score first
            if combined_scores[j] > combined_scores[j + 1]:
                # Swap scores
                combined_scores[j], combined_scores[j + 1] = combined_scores[j + 1], combined_scores[j]
                # Swap corresponding names
                combined_names[j], combined_names[j + 1] = combined_names[j + 1], combined_names[j]
            # If scores are the same, sort by name alphabetically
            elif combined_scores[j] == combined_scores[j + 1]:
                if combined_names[j] > combined_names[j + 1]:
                    # Swap names
                    combined_names[j], combined_names[j + 1] = combined_names[j + 1], combined_names[j]
    
    # Step 4: Update the original scores_param and names_param lists with sorted values
    for i in range(n_param):
        scores_param[i] = combined_scores[i]
        names_param[i] = combined_names[i]
        
    print(combined_scores)
    print(combined_names)
