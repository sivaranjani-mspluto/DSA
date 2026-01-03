class Solution {
    public int[] plusOne(int[] arr) {
        int n=arr.length;
        for(int i=arr.length-1;i>=0;i--) {
			if(arr[i]<9) {
				arr[i]++;
				return arr;
			}
            arr[i] = 0;
		}
			int[] narr= new int[n+1];
			narr[0]=1;
			return narr;
    }
}