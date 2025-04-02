# Leetcode Solver
Solutions for LeetCode problems using different languages.

## Leetcode March Challenge / Study Room

### What's the purpose?
To learn and improve problem-solving skills.

<img src="./resources/images/dc_leetcode.PNG" width="700">

* https://leetcode.com/discuss/post/2347978/join-us-to-code-continuously-such-as-com-99h9/

<img src="./resources/images/completed.PNG" width="700">

| Year | Month | Day | Problem                                | My personal difficulty | Techniques and comments                              | Solution|
| ---- | ----- | --- | -------------------------------------- | ---------------------- | ---------------------------------------------------- | ---- |
| 2025 | March | 13  | 3356. Zero Array Transformation II     | Hard| difference array + binary search + lambda functions on Java | [Java](2025/March/013/3356_ZeroArrayTransformationII.java) |
| 2025 | March | 14  | 2226. Maximum Candies Allocated to K Children     | easy-medium| binary search | [Java](2025/March/014/2226_MaximumCandiesAllocatedtoKChildren.java) |
| 2025 | March | 15  | 2560. House Robber IV     |  medium - hard| binary search solutions, you can do dp but its better tc for bs | [Java](2025/March/015/2560_HouseRobberIV.java) |
| 2025 | March | 16  | 2594. Minimum Time to Repair Cars     |  medium - hard| tricky binary search problem | [Python3](2025/March/016/2594_MinimumTimetoRepairCars.py) |
| 2025 | March | 17  | 2206. Divide Array Into Equal Pairs     |  easy| hash or count, using Counter Built-in on python a special container data-type | [Python3](2025/March/017/2206_DivideArrayIntoEqualPairs.py) |
| 2025 | March | 18  | 2401. Longest Nice Subarray     |  easy-medium| sliding window approach + bitwise operations | [Python3](2025/March/018/2401LongestNiceSubarray.py) |
| 2025 | March | 19  | 3191. Minimum Operations to Make Binary Array Elements Equal to One I     |  easy| simulation | [Python3](2025/March/019/3191_MinimumOperationstoMakeBinaryArrayElementsEqualtoOneI.py) |
| 2025 | March | 20  | 3108. Minimum Cost Walk in Weighted Graph     |  hard| you need too much concepts for this problem, in this case is DSU | [Python3](2025/March/020/3108_MinimumCostWalkinWeightedGraph.py) |
| 2025 | March | 21  | 2115. Find All Possible Recipes from Given Supplies     |  medium-hard| topics: degree, topsort, BFS, dependencies | [Python3](2025/March/021/2115FindAllPossibleRecipesfromGivenSupplies.py) |
| 2025 | March | 22  | 2685. Count the Number of Complete Components     |  medium| dfs, mark nodes, components | [Python3](2025/March/022/2685_CountTheNumberOfCompleteComponents.py) |
| 2025 | March | 23  | 1976. Number of Ways to Arrive at Destination     |  Hard| dijkstra using heap + accumulator logic for get the ways | [Python3](2025/March/023/1976_NumberOfWaysToArriveAtDestination.py) |
| 2025 | March | 24  | 3169. Count Days Without Meetings     |  easy-medium| arrays + sorting + logic for intervals | [Python3](2025/March/024/3169_CountDaysWithoutMeetings.py) |
| 2025 | March | 25  | 3394. Check if Grid can be Cut into Sections     |  medium| intervals + sorting | [Python3](2025/March/025/3394_CheckIfGridCanBeCutIntoSections.py) |
| 2025 | March | 26  | 2033. Minimum Operations to Make a Uni-Value Grid     |  medium| sorting + median other approach sorting + prefix and sufix sum | [Python3](2025/March/026/033_MinimumOperationsToMakeAUni-ValueGrid-median.py) |
| 2025 | March | 27  | 2780. Minimum Index of a Valid Split|  medium| prefix and suffix | [Python3](2025/March/027/2780_MinimumIndexOfAValidSplit.py) |
| 2025 | March | 28  | 2503. Maximum Number of Points From Grid Queries|  Hard| sorting + bfs or min_heap + prefixSum | [Python3](2025/March/028/2503_MaximumNumberOfPointsFromGridQueries.py) |
| 2025 | March | 29  | 2818. Apply Operations to Maximize Score|  VERY Hard| Monotonic Stack + get primes factors (sieve) + modular exponentiation + min heap | [Python3](2025/March/029/2818_ApplyOperationsToMaximizeScore.py) |
| 2025 | March | 30  | 763. Partition Labels| easy-medium | sliding window | [Python3](2025/March/030/763_PartitionLabels.py) |
| 2025 | March | 31  | 2551. Put Marbles in Bags| Hard | need to think how build the solution using formulas + sorting or PQ (heap) | [Python3](2025/March/031/2551_PutMarblesinBags.py) |

# New Concepts learned + some interesting references
* `Counter` Objects for Python: https://www.geeksforgeeks.org/python-counter-objects-elements/


# Hard Problems table

| Problem                                | My personal difficulty | Techniques and comments                              | Solution|
| -------------------------------------- | ---------------------- | ---------------------------------------------------- | ---- |
| 732. My Calendar III | easy-medium | intervals + use some util structure for maintain the order, on my case i use `multiset<pair<int, int>>` | [cpp](Hard/0732_MyCalendarIII.cpp) |
| 980. Unique Paths III | medium-hard | recursion + dfs + cache | [Python3](Hard/0980_UniquePathsIII.py) |
| 2392. Build a Matrix With Conditions | Hard | detect cycles, queue, indegree, sort | [Python3](Hard/2392_BuildAMatrixWithConditions.py) |
| 1402. Reducing Dishes | medium | dp or prefix sum | [Python3](Hard/1402_ReducingDishes.py) |
| 1463. Cherry Pickup II | medium-hard | dp or bfs + relaxation approach | [Python3 DP](Hard/1463_CherryPickupII_dp.py), [Python3 BFS](Hard/1463_CherryPickupII_bfs.py)  |
| 2503. Maximum Number of Points From Grid Queries|  Hard| sorting + bfs or min_heap + prefixSum | [Python3](Hard/2503_MaximumNumberOfPointsFromGridQueries.py) |
| 2551. Put Marbles in Bags| Hard | need to think how build the solution using formulas + sorting or PQ (heap) | [Python3](2025/March/031/2551_PutMarblesinBags.py) |
| 2818. Apply Operations to Maximize Score|  VERY Hard| Monotonic Stack + get primes factors (sieve) + modular exponentiation + min heap | [Python3](2025/March/029/2818_ApplyOperationsToMaximizeScore.py) |
|3500. Minimum Cost to Divide Array Into Subarrays|  VERY Hard| DP + prefix sum + convex hull trick for optimization of queries | [Python3](Hard/3500_MinimumCostToDivideArrayIntoSubarrays.py) |
