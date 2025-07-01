def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # For each number from 1 to m, collect the indices where it appears in arrays a and b
    positions_a = [[] for _ in range(m + 1)]
    positions_b = [[] for _ in range(m + 1)]
    
    for i in range(n):
        positions_a[a[i]].append(i)
        positions_b[b[i]].append(i)
    
    # Key insight: For each number, we need to check if its positions in array a
    # can be made to match its positions in array b after some cyclic shift
    for num in range(1, m + 1):
        pos_a = positions_a[num]
        pos_b = positions_b[num]
        
        # If the number appears a different number of times in both arrays, it's impossible
        if len(pos_a) != len(pos_b):
            return "NO"
        
        if len(pos_a) <= 1:
            # If there's only one instance of this number, we don't need to check
            continue
        
        # Convert positions to "gaps" between consecutive occurrences
        gaps_a = []
        gaps_b = []
        
        for i in range(len(pos_a)):
            next_i = (i + 1) % len(pos_a)
            gap_a = (pos_a[next_i] - pos_a[i]) % n
            gap_b = (pos_b[next_i] - pos_b[i]) % n
            
            # Classify gaps: 1 means consecutive (can't swap), >1 means non-consecutive (can swap)
            # This is because we can only swap elements if their difference is at least 2
            gaps_a.append(1 if gap_a == 1 else 0)
            gaps_b.append(1 if gap_b == 1 else 0)
        
        # Check if there's any rotation of gaps_a that matches gaps_b
        if not can_match_with_rotation(gaps_a, gaps_b):
            return "NO"
    
    return "YES"

def can_match_with_rotation(pattern_a, pattern_b):
    """
    Check if pattern_a can be rotated to match pattern_b.
    We're looking for a one-to-one match for elements that are 1 (consecutive positions).
    Elements that are 0 (non-consecutive positions) can be matched with other 0s.
    """
    if len(pattern_a) != len(pattern_b):
        return False
    
    n = len(pattern_a)
    if n == 0:
        return True
    
    # If the patterns have different numbers of consecutive positions (1s),
    # they can never match after any rotation
    if pattern_a.count(1) != pattern_b.count(1):
        return False
    
    # If there are no consecutive positions, any rotation works
    if pattern_a.count(1) == 0:
        return True
    
    # Create a double pattern to handle rotations
    double_a = pattern_a + pattern_a
    
    # Try all possible rotations
    for i in range(n):
        rotation = double_a[i:i+n]
        if rotation == pattern_b:
            return True
    
    return False

def can_match_cyclic(pattern_a, pattern_b):
    """Check if pattern_a can be cyclically shifted to match pattern_b."""
    if len(pattern_a) != len(pattern_b):
        return False
        
    # Double the pattern to handle cyclic shifts easily
    doubled = pattern_a + pattern_a
    
    # Check if pattern_b is a sublist of doubled
    n = len(pattern_a)
    for i in range(n):
        if doubled[i:i+n] == pattern_b:
            return True
    
    return False

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()