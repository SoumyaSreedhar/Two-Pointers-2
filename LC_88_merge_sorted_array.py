#TC -> o(m+n)
#SC->O(1)



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #   p1 i
        # [1,2,3,3,5,6] 
        # [2,5,6]
        #  p2
        
        p1 = m-1
        p2 = n-1
        idx = m+n-1

        while(p1>=0 and p2>=0):
            if nums2[p2]>= nums1[p1]:
                nums1[idx] = nums2[p2]
                p2 = p2-1
            
            else:
                nums1[idx] = nums1[p1]
                p1 = p1-1
            idx = idx - 1

        while(p2>=0):
            nums1[idx] = nums2[p2]
            p2 = p2-1
            idx = idx -1
        
        return nums1