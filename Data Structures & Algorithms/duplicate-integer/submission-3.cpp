class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        const int n =1e5 + 10 ;
        unordered_map<int , bool> mp;
        for (int i = 0; i < nums.size(); i++) {
            if (mp[nums[i]])
                return true;
            mp[nums[i]] = true;
        }
        return false ;
    }
};