class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long res = 1;
        int cnt =0;
        vector<int> ress;
        for (int i =0 ; i<nums.size(); i++) {
            if (nums[i] != 0) res *= nums[i];
            else cnt++;
        }
        for (int i =0 ; i<nums.size(); i++) {
            if (nums[i] != 0) ress.push_back(cnt?0: res / nums[i]);
            else ress.push_back(cnt>1 ?0 : res);
        }
        return ress;
    }
};