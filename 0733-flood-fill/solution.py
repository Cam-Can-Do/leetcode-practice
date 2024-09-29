class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.visit(image, sr, sc, image[sr][sc], color, len(image) - 1, len(image[0]) - 1)

        return image

    def visit(self, image, sr, sc, startColor, targetColor, rowLen, colLen):
        if sr < 0 or sr > rowLen or sc < 0 or sc > colLen or image[sr][sc] != startColor or image[sr][sc] == targetColor:
            return
        
        image[sr][sc] = targetColor

        self.visit(image, sr + 1, sc, startColor, targetColor, rowLen, colLen)
        self.visit(image, sr - 1, sc, startColor, targetColor, rowLen, colLen)
        self.visit(image, sr, sc + 1, startColor, targetColor, rowLen, colLen)
        self.visit(image, sr, sc - 1, startColor, targetColor, rowLen, colLen)


