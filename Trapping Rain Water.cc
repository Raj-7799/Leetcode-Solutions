class Solution {
public:
    int trap(vector<int>& height) {
        int leftPtr = 0;
        int rightPtr = height.size() - 1;
        int leftMax = 0;
        int rightMax = 0;
        int ans = 0;
        
        while (leftPtr < rightPtr) {
            if (height[leftPtr] < height[rightPtr]) {
                if (height[leftPtr] >= leftMax) {
                    leftMax = height[leftPtr];
                } else {
                    ans += (leftMax - height[leftPtr]);
                }
                leftPtr++;
            } else {
                if (height[rightPtr] >= rightMax) {
                    rightMax = height[rightPtr];
                } else {
                    ans += (rightMax - height[rightPtr]);
                }
                rightPtr--;
            }
        }
        return ans;
    }
};
