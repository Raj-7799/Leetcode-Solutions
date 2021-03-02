class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        
        int defaultSum = 0;
        int linearSum = 0;
        int it = 1;
        int negativeIt = -1;
        int likeTime = 0;
        
        for (auto x : satisfaction) {
            if (x > 0) {
                defaultSum += x * it;
                linearSum += x;
                it += 1;
            } else {
                negativeIt += 1; 
            }
        }
        
        likeTime = defaultSum;
        
        while(negativeIt > -1) {
            linearSum += satisfaction[negativeIt];
            defaultSum += linearSum;
            likeTime = max(likeTime, defaultSum);
            negativeIt -= 1;
        }
        
        return likeTime;
    }
};
