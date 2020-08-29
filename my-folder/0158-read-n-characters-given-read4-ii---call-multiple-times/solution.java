/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf4); 
 */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    
    private int buf4Pointer = 0;
    private int buf4Count = 0;
    private char[] buf4 = new char[4];
    public int read(char[] buf, int n) {
        int pointer = 0;
        while (pointer < n) {
            if (buf4Pointer == 0) {
                buf4Count = read4(buf4);
            }
            if (buf4Count == 0) {
                break;
            }
            while (pointer < n && buf4Pointer < buf4Count) {
                buf[pointer++] = buf4[buf4Pointer++];
            }
            if (buf4Pointer >= buf4Count) {
                buf4Pointer = 0;
            }
        }
        return pointer;
    }
}
