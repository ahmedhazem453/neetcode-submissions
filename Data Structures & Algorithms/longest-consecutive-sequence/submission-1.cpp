class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        unordered_set<int> s{nums.begin(), nums.end()};
        int res = 0;

        for (int num : s) {
            if (!s.count(num - 1)) {
                int current = num;
                int cnt = 1;

                while (s.count(current + 1)) {
                    current++;
                    cnt++;
                }
                res = max(res, cnt);
            }
        }

        return res;
    }
};