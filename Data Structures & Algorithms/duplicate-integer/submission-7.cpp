class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> st ; 
        st.insert(nums.begin() , nums.end());
        return st.size() != nums.size() ;
    }
};