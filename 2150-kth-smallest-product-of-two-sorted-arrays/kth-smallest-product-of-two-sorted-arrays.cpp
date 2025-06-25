class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        auto find_count = [&](long long midprod) {
            long long prod_count = 0;
            int n = nums2.size();
            for (int i = 0; i < nums1.size(); ++i) {
                if (nums1[i] >= 0) {
                    int l = 0, r = n - 1, m = -1;
                    while (l <= r) {
                        int mid = l + (r - l) / 2;
                        long long prod = 1LL * nums1[i] * nums2[mid];
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
                        long long prod = 1LL * nums1[i] * nums2[mid];
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
        };

        long long res = 0;
        long long l = -1e10, r = 1e10;

        while (l <= r) {
            long long mid = l + (r - l) / 2;
            long long count = find_count(mid);
            if (count >= k) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }
};
