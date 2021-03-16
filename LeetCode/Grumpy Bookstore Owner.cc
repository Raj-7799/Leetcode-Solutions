class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int totalMin = customers.size();
        
        int totalSatisfied = 0;
        
        for (int i = 0; i < totalMin; i++) {
            if (grumpy[i] == 0)
                totalSatisfied += customers[i];
        }
        
        int secretlySatisfied = 0;
        int finalSecretlySatisfied = 0;
        int ans = 0;
        unsigned int i;
        
        for (i = 0; i < totalMin && i < X; i++) {
            if (grumpy[i])
                secretlySatisfied += customers[i];
        }
        
        finalSecretlySatisfied = max(finalSecretlySatisfied, secretlySatisfied);
        
        for (; i < totalMin; i++) {
            if (grumpy[i - X]) {
                secretlySatisfied -= customers[i - X];
            } 
            
            if (grumpy[i]) {
                secretlySatisfied += customers[i];
            }
            
            finalSecretlySatisfied = max(finalSecretlySatisfied, secretlySatisfied);
        }
        
        
        return totalSatisfied + finalSecretlySatisfied;
    }
};
