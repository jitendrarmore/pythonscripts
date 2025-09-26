


def merge(nums1,  nums2,  m, n):

    lastIndex = m + n -1

    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[lastIndex] = nums1[m-1]
            m -= 1
        else:
            nums1[lastIndex] = nums2[n-1]
            n -= 1
        lastIndex -= 1

    while n > 0:
        nums1[lastIndex] = nums2[n-1]
        n -= 1
        lastIndex -= 1


    print(nums1)


merge([1,2,3,0,0,0],[2,5,6], 3, 3 )