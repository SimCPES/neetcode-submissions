class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        for a, b in prerequisites:
            if a in order and b in order:
                index_a = order.index(a)
                index_b = order.index(b)
                if index_a < index_b:
                    return []
            elif a in order:
                index_a = order.index(a)
                order.insert(max(index_a-1, 0), b)
            elif b in order:
                index_b = order.index(b)
                order.insert(min(index_b+1, len(order)), a)
            else:
                order.extend([b, a])
        for c in range(numCourses):
            if c not in order:
                order.append(c)
        return order
