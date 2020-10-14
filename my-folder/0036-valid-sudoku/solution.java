class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] row = new HashSet[9];
    Set<Character>[] col = new HashSet[9];
    Set<Character>[] subbox = new HashSet[9];
    for (int i = 0; i < 9; i++) {
      row[i] = new HashSet<>();
      col[i] = new HashSet<>();
      subbox[i] = new HashSet<>();
    }

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        char c = board[i][j];
        if (c == '.') {
          continue;
        }
        // check row
        if (row[i].contains(c)) {
          return false;
        }
        row[i].add(c);
        // check col
        if (col[j].contains(c)) {
          return false;
        }
        col[j].add(c);
        // check subbox
        int boxRow = i / 3;
        int boxCol = j / 3;
        if (subbox[boxRow*3+boxCol].contains(c)){
          return false;
        }
        subbox[boxRow*3+boxCol].add(c);
      }
    }

    return true;
    }
}
