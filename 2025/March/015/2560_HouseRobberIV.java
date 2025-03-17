class Solution {
    public int n;
    public int f(int i, int k, int [] nums){
        if(k <= 0){
            return 0;
        }
        if(i >= n){
            return 100000;
        }
        int nxt = f(i+1, k, nums);
        int take = Math.max(nums[i], f(i+2, k-1, nums));
        return Math.min(nxt, take);
    }
    public int minCapability(int[] nums, int k) {
        n = nums.length;
        //return f(0, k, nums);

        /*
        int [][] dp = new int [n+2][k+1];
        for(int ki=k;ki>=0;ki--){
            dp[n][ki] = 1000000;
            dp[n+1][ki] = 1000000;
        }

        for(int i=0;i<=(n+1);i++){
            dp[i][0] = 0;
        }

        for(int i=n-1;i>=0;i--){
            for(int ki=1;ki <= k; ki++){
                int nxt = dp[i+1][ki];
                int take = Math.max(nums[i], dp[i+2][ki-1]);
                dp[i][ki] = Math.min(nxt, take);
            }
        }
        System.out.println("DP: ");
        for(int i=0;i<=(n+1);i++){
            for(int ki=0;ki<=k;ki++){
                System.out.print(dp[i][ki] + " ");
            }
            System.out.println("");
        }
        return dp[0][k];
        */

        int l = 1;
        int r = Arrays.stream(nums).max().getAsInt();
        while(l < r){
            int mid = l + (r - l) / 2;
            int i = 0;
            int possible = 0;
            while(i < n){
                if(nums[i] <= mid){
                    possible++;
                    i += 2;
                }else{
                    i++;
                }
            }
            if(possible >= k){
                r = mid;
            }else{
                l = mid + 1;
            }
        }
        return l;
    }
}