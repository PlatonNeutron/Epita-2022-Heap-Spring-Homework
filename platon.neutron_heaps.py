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
        result = H[1]
        i = 1
        j = len(H) - 1
        finished = False

        while not (finished):
            H[i], H[j] = H[j], H[i]

            if (j != (len(H) - 1)):
                i = j

            if ((i * 2) <= (len(H) - 1) and ((i * 2) + 1) <= (len(H) - 1)):

                if (H[i][0] > H[i * 2][0] and H[i][0] > H[(i * 2) + 1][0]):
                    mini = min((H[i * 2][0], i * 2), (H[(i * 2) + 1][0], (i * 2) + 1))
                    j = mini[1]

                elif (H[i][0] > H[i * 2][0]):
                    j = H[i * 2][0]

                elif (H[i][0] > H[(i * 2) + 1][0]):
                    j = H[(i * 2) + 1][0]

                else:
                    finished = True

            else:
                finished = True

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
    heap = True

    if (is_empty(T)):
        return heap

    else:
        i = len(T) - 1

        while (heap != False and i > 1):
            if (T[i // 2][0] <= T[i][0]):
                i -= 1

            else:
                heap = False

    return heap


def heap_sort(L):
    """
        sorts the associative list of (elements, values) L in increasing order according to values (not in place)
    
        :param L: a list containing pairs (element: any, value: int)
        :rtype: (any, num) list (the new list sorted)
    """
    result = []
    result2 = Heap()

    for i in range(0, len(L)):
        if (isinstance(L[i][0], int)):
            nb, elt = L[i]

        else:
            elt, nb = L[i]

        heap_push(result2, elt, nb)

    for j in range(1, len(result2)):
        nb, elt = result2[j]

        result.append((elt, nb))

    return result