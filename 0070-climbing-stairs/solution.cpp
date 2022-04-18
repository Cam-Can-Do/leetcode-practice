class Solution {
public:
    int climbStairs(int n) { 
        /* not effeicient enough
        if (n == 1 || n == 0) {
            return 1;
        }
        return climbStairs(n-1) + climbStairs(n-2);          
        */
        
        if (n == 1 || n == 0) return 1;
        int* numbers = new int[n + 1];
        numbers[0] = 1;
        numbers[1] = 1;
        for (int i = 2; i < n + 1; ++i) {
            numbers[i] = numbers[i - 1] + numbers[i - 2];
        }
//        delete[] numbers;
        return numbers[n];
    }
};
