class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int validPointer = 1;
        int digitCounter = 0;
        int atMost = 2;
        int numsSize = nums.size();
        
        for (int i = 1; i < numsSize; i++) {
            if (nums[i] == nums[validPointer - 1] ) {
                digitCounter += 1;
            } else {
                digitCounter = 0;
            }
            
            if (digitCounter < atMost) {
                swap(nums[validPointer], nums[i]);
                validPointer ++;
            } 
        }
        return validPointer;
    }
};
