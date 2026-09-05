#include <bits/stdc++.h>
using namespace std;

class MinStack {
    stack<pair<int, int>> st; // {value, current_min}
    
public:
    MinStack() {}

    void push(int val) {
        if (st.empty())
            st.push({val, val});
        else
            st.push({val, min(val, st.top().second)});
    }

    void pop() {
        if (!st.empty())
            st.pop();
    }

    int top() {
        if (st.empty()) throw runtime_error("Stack is empty");
        return st.top().first;
    }

    int getMin() {
        if (st.empty()) throw runtime_error("Stack is empty");
        return st.top().second;
    }
};