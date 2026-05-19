from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index == 0:
        return heap
    l = list(heap.data)
    parent_index = (index -1) // 2
    if l[index] < l[parent_index]:
        l[index], l[parent_index] = l[parent_index], l[index]
        return heapify_up(MinHeap(l), parent_index)
    return MinHeap(l)

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    lowest_val = index
    l = list(heap.data)
    l_len = len(l)
    left_ind = 2 *index +1
    right_ind = 2 * index+ 2
    if right_ind < l_len and l[right_ind] < l[lowest_val]:
        lowest_val = right_ind
    if left_ind < l_len and l[left_ind] < l[lowest_val]:
        lowest_val = left_ind
    
    if lowest_val != index:
        l[index], l[lowest_val] = l[lowest_val], l[index]
        return heapify_down(MinHeap(l), lowest_val)
    
    return MinHeap(l)


def insert(heap: MinHeap, element: Node) -> MinHeap:
    l = list(heap.data) + [element]
    return heapify_up(MinHeap(l), len(l)-1)


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    l = list(heap.data)
    l[-1], l[0] = l[0], l[-1]
    popped_head = l.pop()
    return (heapify_down(MinHeap(l), 0), popped_head)


def count_frequency(s: str)-> dict[str,int]:

    return_dict = {}
    for string in s:
        if string in return_dict:
            return_dict[string] = return_dict[string] +1
        else:
            return_dict[string] = 1
    return return_dict


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:

    return_heap = MinHeap()
    for key, val in frequency.items():
        return_heap = insert(return_heap, Node(val, key))
    return return_heap


def build_tree(priority_queue: MinHeap) -> Node:
    while len(priority_queue.data) >1:
        priority_queue, left = extract_min(priority_queue)
        priority_queue, right = extract_min(priority_queue)
        
        priority_queue = insert(priority_queue, Node(left.freq + right.freq, left.char + right.char, left, right))
    return priority_queue.data[0]


def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    
    if code is None:
        code = {}  
    if node is None:
        return code
    if node.right is None and node.left is None:
        code[node.char] = prefix
        return code
    generate_codes(node.left, prefix + "0", code)
    generate_codes(node.right, prefix + "1", code)
    return code


def encode(s: str, codes: dict)-> str:
    res = []
    for string in s:
        res.append(codes[string])
    return "".join(res)


def decode(encoded_string: str, root: Node):
    res = []
    cur = root
    for s in encoded_string:
        if s == "0":
            cur = cur.left
        else:
            cur = cur.right
        if cur.right is None and cur.left is None:
            res.append(cur.char)
            cur = root
    return "".join(res)

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes
