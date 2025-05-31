import numpy as np

# solving two sum problem
def two_sum(array, target):
    """
    Finds two numbers in an array that sum to a target value.

    Args:
        nums: An array of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the two numbers, or None if no such pair exists.
    """
    num_maps = {}

    for index, number in enumerate(array):
        complement = target - number

        if complement == number:
            return (index, index)
        elif complement in num_maps:
            return (num_maps[complement], index)
        else:
            num_maps[number] = index
    
    return None

array = np.random.randint(10, 100, 10)
index0, index1 = np.random.randint(0, 9, 2)
target = array[index0] + array[index1]
output = two_sum(array, target)
print(index0, index1, output)


# Partition Labels
def partition_labels(labels):
    partitions = []
    labels_start = {}
    labels_end = {}
    for index, label in enumerate(labels):
        if label in labels_start:
            labels_end[label] = index+1
        else:
            labels_start[label] = index
            labels_end[label] = index+1
    print(labels_start)
    start = 0
    end = 0
    for index, label in enumerate(labels):
        if index < end:
            continue
        start = index
        end = labels_end[label]
        for j in range(start, end):
            end = labels_end[labels[j]] if labels_end[labels[j]] > end else end
        partitions.append(labels[start: end])
    print(partitions)

s = "ababcbacadefegdezhijhklij"
partition_labels(s)
