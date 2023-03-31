class Solution {
    public void reverseString(char[] a) {
     
      /*for(int i=0,j=a.length-1;i<j;i++,j--){
          char temp = a[i];
          a[i] = a[j];
          a[j] = temp;
      }*/

      int i=0, j=a.length-1;
      while(i<j){
          char temp = a[i];
          a[i] = a[j];
          a[j] = temp;
          i++;
          j--;

      }
    
    }
}