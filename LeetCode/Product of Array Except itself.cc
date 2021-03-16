class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
         int numsLength = nums.size();
        vector<int> ans(numsLength, 0);

        ans[numsLength - 1] = nums[numsLength - 1];
      
        for(int i = numsLength - 2; i>=0; i--) {
            ans[i] = ans[i + 1] * nums[i];
        }

        int prefixProduct = nums[0];
        
        for (int i=0; i <= numsLength - 1; i++ ) {
            
            if (i > 0 && i != numsLength - 1) {
                ans[i] =  ans[i + 1] * prefixProduct;
                prefixProduct = prefixProduct * nums[i];
            } else if(i == numsLength - 1) {
                ans[i] = prefixProduct;
            }
            else {
                ans[i] = ans[i + 1];
            }
        }
        return ans;
    }
};
