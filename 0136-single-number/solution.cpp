class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int temp = nums[0];
        for (auto i = 1; i < nums.size(); ++i) {
            temp = temp ^ nums[i]; 
        }
        return temp;
    }
};
