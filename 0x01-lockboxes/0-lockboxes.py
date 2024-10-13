def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    
    # Set to track unlocked boxes, initially only box 0 is unlocked
    unlocked = set([0])
    
    # Set to track keys we have collected
    keys = set(boxes[0])  # Start with the keys from box 0
    
    # We continue processing while we have new keys to check
    while keys:
        new_key = keys.pop()  # Get one key from the set
        
        # If the new key corresponds to a box number and it's not already unlocked
        if new_key < n and new_key not in unlocked:
            # Unlock the box
            unlocked.add(new_key)
            # Add the new keys from this box into the keys set
            keys.update(boxes[new_key])
    
    # Check if all boxes are unlocked
    return len(unlocked) == n

