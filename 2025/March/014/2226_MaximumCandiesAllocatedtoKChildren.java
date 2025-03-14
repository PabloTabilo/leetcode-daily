class Solution {
    public int maximumCandies(int[] candies, long k) {
        long tot = 0;
        for(int x : candies){
            tot += (long) x;
        }
        if(tot < k){
            return 0;
        }
        Function<Integer, Boolean> isValid = (mx) -> {
            long cnt = 0;
            for(int c : candies){
                if(c >= mx){
                    long numChilds = c / mx;
                    cnt += numChilds;
                }
            }
            return cnt >= k;
        };
        int l = 1;
        int r = 10000000;
        int ans = 0;
        while(l <= r){
            int mid = l + (r - l) / 2;
            if(isValid.apply(mid)){
                ans = mid;
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        return ans;
    }
}