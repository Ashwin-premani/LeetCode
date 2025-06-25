class Solution {
    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        long l = -10000000000L, r = 10000000000L, res = 0;

        while (l <= r) {
            long mid = l + (r - l) / 2;
            long count = findCount(nums1, nums2, mid);
            if (count >= k) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }

    private long findCount(int[] nums1, int[] nums2, long midprod) {
        long prod_count = 0;
        int n = nums2.length;

        for (int i = 0; i < nums1.length; i++) {
            if (nums1[i] >= 0) {
                int l = 0, r = n - 1, m = -1;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    long prod = 1L * nums1[i] * nums2[mid];
                    if (prod <= midprod) {
                        m = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                prod_count += (m + 1);
            } else {
                int l = 0, r = n - 1, m = n;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    long prod = 1L * nums1[i] * nums2[mid];
                    if (prod <= midprod) {
                        m = mid;
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }
                prod_count += (n - m);
            }
        }

        return prod_count;
    }
}
