#include <vector>
#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> ans;
        unordered_map<int, vector<int>> g;
        int n = nums.size();
        for(int i = n-1; i >= 0; i--){
            for(int j = i-1; j >=0;j--){
                if( (nums[i] % nums[j]) == 0){
                    g[nums[i]].push_back(j);
                }
            }
        }
        //vector<bool> vis(n, false);
        int startIdx = 0;
        int sz = -1;
        unordered_map<int, int> best;
        vector<int> dp(n, 0);
        for(int i = 0; i < n; i++){
            if(g.count(nums[i]) > 0){
                for(int j : g[nums[i]]){
                    if(dp[i] < (1 + dp[j]) ){
                        dp[i] = 1 + dp[j];
                        best[i] = j;
                    }
                }
            }else{
                best[i] = -1;
            }

        }
        int mx = -1;
        int currIdx = -1;
        for(int i=0;i<n;i++){
            if(dp[i] > mx){
                mx = dp[i];
                currIdx = i;
            }
        }
        while(best.count(currIdx) > 0){
            ans.push_back(nums[currIdx]);
            currIdx = best[currIdx];
        }

        return ans;
    }
};