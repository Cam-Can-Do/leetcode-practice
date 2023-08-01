class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            aLeft = A[i] if i >= 0 else float("-infinity")
            aRight = A[i + 1] if i + 1 < len(A) else float("infinity")
            bLeft = B[j] if j >= 0 else float("-infinity")
            bRight = B[j + 1] if j + 1 < len(B) else float("infinity")

            # partitions are correct
            if aLeft <= bRight and bLeft <= aRight:
                # total size is odd, so just need the middle element
                if total % 2 != 0:
                    return min(aRight, bRight)
                else:   # total size is even, so take average of two middle elements
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1






        
