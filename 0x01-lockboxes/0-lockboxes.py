#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = set([0])  # Start with box 0 unlocked
    keys = set(boxes[0])  # Collect keys from box 0

    # Continue processing as long as we have keys to check
    while keys:
        key = keys.pop()  # Get one key from the set
        
        # If the key corresponds to a valid box and it's not already unlocked
        if key < n and key not in unlocked:
            unlocked.add(key)  # Unlock the box
            keys.update(boxes[key])  # Add the keys from this newly unlocked box

    # If all boxes are unlocked, return True
    return len(unlocked) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
