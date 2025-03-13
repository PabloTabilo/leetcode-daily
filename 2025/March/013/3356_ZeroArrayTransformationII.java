class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = queries.length;
        int m = nums.length;
        Function<Integer, Boolean> isValid = (k) -> {
            int [] diff = new int[m];
            diff[0] = nums[0];
            for(int i=1;i<m;i++){
                diff[i] = nums[i] - nums[i-1];
            }
            for(int i=0;i<k;i++){
                int l = queries[i][0];
                int r = queries[i][1];
                int v = queries[i][2];
                diff[l] -= v;
                if(r+1 < m){
                    diff[r+1] += v;
                }
            }
            int accSum = diff[0];
            if(accSum > 0) return false;
            for(int i=1;i<m;i++){
                accSum += diff[i];
                if(accSum > 0){
                    return false;
                }
            }
            return true;
        };
        int l = 0;
        int r = n;
        int ans = -1;
        while(l <= r){
            int mid = l + (r - l) / 2;
            if(isValid.apply(mid)){
                ans = mid;
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return ans;
    }
}