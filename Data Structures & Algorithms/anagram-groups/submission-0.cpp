class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, int> mp; 
        int cnt = 0;

        for (int i = 0; i < strs.size(); i++) {
            string s = strs[i];
            sort(s.begin(), s.end()); 

            if (mp.find(s) == mp.end()) {
                mp[s] = cnt++;       
                res.push_back({});   
            }

            res[mp[s]].push_back(strs[i]);
        }

        return res;
    }
};
