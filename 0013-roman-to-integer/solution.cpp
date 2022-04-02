class Solution {
public:
    
    int rom_value(char letter) {
        if (letter == 'I') return 1;
        if (letter == 'V') return 5;
        if (letter == 'X') return 10;
        if (letter == 'L') return 50;
        if (letter == 'C') return 100;
        if (letter == 'D') return 500;
        if (letter == 'M') return 1000;
        else return 0; 
    }

    int romanToInt(string s) {
        int total = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (rom_value(s[i]) >= rom_value(s[i + 1])) {
                total += rom_value(s[i]);
            } else if (rom_value(s[i]) < rom_value(s[i + 1])) {
                total += rom_value(s[i + 1]) - rom_value(s[i]);
                ++i;
            }
        }
        return total;
        
    }
};
