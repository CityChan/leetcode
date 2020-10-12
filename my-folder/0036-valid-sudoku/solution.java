class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] row = new HashSet[9];
        Set<Character>[] col = new HashSet[9];
        Set<Character>[] subbox = new HashSet[9];
        for(int i=0;i<9;i++){
            row[i] = new HashSet<>();
            col[i] = new HashSet<>();
            subbox[i] = new HashSet<>();
        }
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.'){
                    continue;
                }
                int index = i/3*3+j/3;
                if(!row[i].add(board[i][j]) || !col[j].add(board[i][j]) || !subbox[index].add(board[i][j])){
                    return false;
                }
            }
        }
        
        return true;
    }
}
