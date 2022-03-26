__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: heap.py 2022-03-20'

"""
Heap homework
2022 - S2
@author: platon.neutron
"""

# given function

def Heap():
    """
        returns a fresh new empty heap

        :rtype: list (heap)
    """
    return [None]


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

def is_empty(H):
    """
        tests if the heap H is empty

        :param H: the heap
        :type H: list (hierarchical rep. of bintree)
        :rtype: bool
    """
    if (len(H) == 1 and H[0] == None):
        return True

    return False


def heap_push(H, elt, val):
    """
        adds the pair (val, elt) to heap H (in place: no need to return H)
    
        :param H: The heap
        :type H: list (hierarchical rep. of bintree)
        :param elt: The element to add
        :type elt: any
        :param val: The value associated to elt
        :type val: int or float
    """
    if (is_empty(H)):
        H.append((val, elt))

    else:
        H.append((val, elt))

        i = len(H) - 1
        j = i // 2
        (cVal, _) = H[i]
        (pVal, _) = H[j]

        while (pVal > cVal and j > 0):
            H[i], H[j] = H[j], H[i]

            i = j
            j = i // 2

            if (j > 0):
                (pVal, pElt) = H[j]


def __heap_pop_aux(H):
    """
        Function which return the min and the second min and theirs index

        :param H: The heap
        :return: the min and the second min and theirs index
        :rtype: ((minimum, index), (s_minimum, index))
    """
    minimum = (H[1], 1)
    s_minimum = (H[len(H) - 1], len(H) - 1)

    for i in range(2, len(H)):
        if (H[i][0] < minimum[0][0]):
            minimum = (H[i], i)

        elif (H[i][0] < s_minimum[0][0] and H[i] != s_minimum):
            s_minimum = (H[i], i)

    return (minimum, s_minimum)


def heap_pop(H):
    """
        removes and returns the pair of the smallest value in the heap H, raises Exception if H is empty
    
        :param H: The heap
        :type H: list (hierarchical rep. of bintree)
        :rtype: (num, any) (the removed pair)
    """
    if (is_empty(H)):
        raise Exception("H cannot be empty")

    else:
        minimum, s_minimum = __heap_pop_aux(H)
        result = minimum[0]
        i = minimum[1]
        j = s_minimum[1]

        while (j <= (len(H) - 1)):
            H[i] = H[j]
            i = j

            if ((j * 2 + 1) > (len(H) - 1)):
                j *= 2

            else:
                j = j * 2 + 1

        H.pop()

        return result


# ---------------------------------------------------------------
def is_heap(T):
    """
        tests whether the complete tree T is a heap
    
        :param T: a complete tree in hierarchical representation
        :type T: list (hierarchical rep. of bintree)
        :rtype: bool
    """
    # FIXME
    pass


def heap_sort(L):
    """
        sorts the associative list of (elements, values) L in increasing order according to values (not in place)
    
        :param L: a list containing pairs (element: any, value: int)
        :rtype: (any, num) list (the new list sorted)
    """
    # FIXME
    pass