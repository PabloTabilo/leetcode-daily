#include <set>
#include <utility>
class MyCalendarThree {
public:
    multiset<pair<int, int>> s;    
    MyCalendarThree() {
        
    }
    
    int book(int startTime, int endTime) {
        s.insert({startTime, 1});
        s.insert({endTime, -1});
        int ans = 0;
        int curr = 0;
        for(auto it : s){
            curr += it.second;
            ans = max(ans, curr);
        }
        return ans;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */