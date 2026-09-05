class Solution {
public:
    bool isValid(string s) {
        stack <char>st;
        int cnt = 0 ;
        for (int i =0 ;i < s.size();i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                st.push(s[i]);
            }else {
                cnt++;
                if (!st.empty()) {
                    if (s[i] == ')' && st.top() == '(')st.pop(),cnt--;
                    else if (s[i] == '}' && st.top() == '{')st.pop(),cnt--;
                    else if (s[i] == ']' && st.top() == '[')st.pop(),cnt--;
                }
            }
        }
        return !cnt && st.empty();
    }
};