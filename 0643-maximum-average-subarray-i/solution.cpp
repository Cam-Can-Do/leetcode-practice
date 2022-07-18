class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        if (nums.size() == 1) {
            return double(nums[0]) / k;
        }
        
        double sum = 0;
        
        
        // initialize old sum with 'leftmost' window
        for (auto i = 0; i < k; ++i) {
            sum += nums[i]; 
        }
        double max_sum = sum;
        
        for (auto i = k; i < nums.size(); ++i) {
            sum += nums[i] - nums[i-k];
            max_sum = max(max_sum, sum);
        }
        return max_sum / k;
        
    }
};
