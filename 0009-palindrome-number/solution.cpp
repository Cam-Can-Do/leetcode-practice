class Solution {
public:
    bool isPalindrome(int x) {
        std::string str_x = std::to_string(x);
        
        int i = 0;
        int j = str_x.length() - 1;
        while (i != j && i < j){
            if(str_x[i] != str_x[j]) {
                return false;
            }
            ++i;
            --j;
        }
    return true;
    }
};
