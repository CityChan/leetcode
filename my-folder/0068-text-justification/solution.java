class Solution {
    public  List<String> fullJustify(String[] words, int maxWidth) {
    List<String> result = new ArrayList<>();

    int i = 0;
    while (i < words.length) {
      int j = i + 1;
      int curLen = words[i].length();
      while (j < words.length && (curLen + words[j].length() + (j - i - 1) < maxWidth)) {
        curLen += words[j].length();
        j++;
      }
      int totalSpace = maxWidth - curLen;
      // one word or last line, left justify
      if (j - i == 1 || j == words.length) {
        result.add(leftJustify(words, i, j, totalSpace));
      } else { // otherwise, middle justify
        result.add(middleJustify(words, i, j, totalSpace));
      }
      i = j;
    }

    return result;
  }

  private  String middleJustify(String[] words, int i, int j, int totalSpace) {
    int sections = j - i - 1;
    // space in between
    int spaces = totalSpace / sections;
    // left over
    int extraSpaces = totalSpace % sections;

    StringBuilder sb = new StringBuilder(words[i]);
    for (int k = i + 1; k < j; k++) {
      int spacesToApply = spaces + (extraSpaces > 0 ? 1 : 0);
      extraSpaces--;
      sb.append(fillSpaces(spacesToApply)).append(words[k]);
    }

    return sb.toString();
  }
    
  private  String leftJustify(String[] words, int i, int j, int totalSpace) {
    StringBuilder sb = new StringBuilder(words[i]);
    for (int k = i + 1; k < j; k++) {
      sb.append(" ").append(words[k]);
    }
    int rightSpace = totalSpace - (j - i - 1);
    sb.append(fillSpaces(rightSpace));
    return sb.toString();
  }

  private  String fillSpaces(int n) {
    if (n <= 0) {
      return "";
    }
    char[] chars = new char[n];
    Arrays.fill(chars, ' ');
    return String.valueOf(chars);
  }
}
