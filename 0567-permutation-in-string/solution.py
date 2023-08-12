class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = {}
        for letter in s1:
            s1_letters[letter] = s1_letters.get(letter, 0) + 1

        l = 0
        window = {}
        for r in range(len(s2)):
            cur_char = s2[r]
            window[cur_char] = window.get(cur_char, 0) + 1

            if window == s1_letters:
                return True

            while r - l + 1 >= len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
        return False

