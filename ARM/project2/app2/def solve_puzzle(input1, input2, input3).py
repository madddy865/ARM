def find_correct_sequence(input1, input2, size):
    def construct_tree(arr1, arr2):
        if not arr1:
            return []
        root = arr1[0]
        left_size = arr2.index(root)
        left_tree = construct_tree(arr1[1:1+left_size], arr2[:left_size])
        right_tree = construct_tree(arr1[1+left_size:], arr2[left_size+1:])
        return [root] + left_tree + right_tree
    
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
    
    sequence1 = construct_tree(input1, input2)
    sequence2 = construct_tree(input2, input1)
    
    if is_sorted(sequence1):
        return sequence1
    else:
        return sequence2

# Example usage
input1 = [4, 2, 5, 1, 3]
input2 = [1, 2, 4, 5, 3]
input3 = 5

output = find_correct_sequence(input1, input2, input3)
print(output)
