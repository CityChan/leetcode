class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      if (image[sr][sc] == color) return image;
      fill(image, sr, sc, color, image[sr][sc]);
      return image;
    }
  
    private void fill(int[][] image, int sr, int sc, int color, int currColor) {
      if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length) return;
      
      if (currColor != image[sr][sc]) return;
      
      image[sr][sc] = color;
      
      //recrusive calls to 4 directions 
      fill(image, sr-1, sc, color, currColor);
      fill(image, sr+1, sc, color, currColor);
      fill(image, sr, sc-1, color, currColor);
      fill(image, sr, sc+1, color, currColor);
    }
}
