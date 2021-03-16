class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> remainderCount(60, 0);
       int ans = 0;
        
        for (auto &it : time) {
            if (it % 60 == 0) {
                ans += remainderCount[0];
            } else {
                ans += remainderCount[60 - it % 60];
            }
    
            remainderCount[it % 60]++;
        }
        return ans;
    }
};
