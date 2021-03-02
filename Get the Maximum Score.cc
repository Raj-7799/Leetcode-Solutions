class Solution {
  public:
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        long long ans=0;
        long long mod= 1000000007;
        int n1=nums1.size(),n2=nums2.size();
        
        long long up=0,dn=0;
        int i=0,j=0;
        while(i<n1 && j<n2){
            if(nums1[i]==nums2[j]){
                ans+= max(up,dn)+ nums1[i];
                up=0,dn=0;
                i++,j++;
            }
            else if(nums1[i]>nums2[j]){
                dn+= nums2[j];
                j++;
            }
            else{
                up+= nums1[i];
                i++;
            }
        }
        while(i<n1) up+=nums1[i++];
        while(j<n2) dn+=nums2[j++];
        return (max(up,dn)+ans)%mod;
    }
};
