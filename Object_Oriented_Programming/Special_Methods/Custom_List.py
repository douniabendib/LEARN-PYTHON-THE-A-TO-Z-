class CustomList:
    """Create a CustomList class that mimics the behavior of Python's built-in list class"""

    def __init__(self, my_list=None):
        """Initialize the list with optional initial items"""
        self.my_list = my_list if my_list is not None else []

    def __getitem__(self, index):
        """Support indexing for getting values"""
        return self.my_list[index]
    
    def __setitem__(self, index, value):
        """Support indexing for setting values"""
        self.my_list[index] = value
    
    def __len__(self):
        """Support length checking (len(my_list))"""
        return len(self.my_list)
    
    def __add__(self, other):
        """Support addition with another CustomList or a regular list"""
        return CustomList(self.my_list + other.my_list)
    
    def __str__(self):
        """Support string representation (str(my_list)"""
        return str(self.my_list)
    
    def __repr__(self):
        """Support string representation (repr(my_list)"""
        return repr(self.my_list)

    def __iter__(self):
        """Support iteration (for item in my_list)"""
        return iter(self.my_list)
    
    def __contains__(self, item):
        """Support contains check (item in my_list"""
        return item in self.my_list

    def append(self, item):
        """Include an append method that adds an item to the end of the list"""
        return self.my_list.append(item)

    def pop(self, index=-1):
        """Include a pop method that removes and returns the last item"""
        return self.my_list.pop(index)

    def clear(self):
        """Include a clear method that removes all items"""
        return self.my_list.clear()


# Test code -
def test_custom_list():
    try:
        # Test initialization
        empty_list = CustomList()
        assert len(empty_list) == 0, f"Empty list should have length 0, but has {len(empty_list)}"
        
        init_list = CustomList([1, 2, 3])
        assert len(init_list) == 3, f"Initialized list should have length 3, but has {len(init_list)}"
        
        # Test indexing
        assert init_list[0] == 1, f"First element should be 1, but got {init_list[0]}"
        init_list[1] = 10
        assert init_list[1] == 10, f"Element after assignment should be 10, but got {init_list[1]}"
        
        # Test string representation
        assert str(init_list) == "[1, 10, 3]", f"String representation incorrect, got {str(init_list)}"
        
        # Test addition
        combined = init_list + CustomList([4, 5])
        assert len(combined) == 5, f"Combined list should have length 5, but has {len(combined)}"
        assert combined[3] == 4, f"Fourth element of combined list should be 4, but got {combined[3]}"
        
        # Test iteration and contains
        items = []
        for item in combined:
            items.append(item)
        assert items == [1, 10, 3, 4, 5], f"Iteration produced incorrect items: {items}"
        
        assert 10 in combined, "10 should be in the list"
        assert 7 not in combined, "7 should not be in the list"
        
        # Test append and pop
        combined.append(6)
        assert len(combined) == 6, f"After append, length should be 6, but got {len(combined)}"
        assert combined[5] == 6, f"Last element after append should be 6, but got {combined[5]}"
        
        popped = combined.pop()
        assert popped == 6, f"Popped value should be 6, but got {popped}"
        assert len(combined) == 5, f"After pop, length should be 5, but got {len(combined)}"
        
        # Test clear
        combined.clear()
        assert len(combined) == 0, f"After clear, length should be 0, but got {len(combined)}"
        
        print("All tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")

test_custom_list()
print("Tests completed")
