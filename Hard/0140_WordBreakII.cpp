#include <string>
#include <vector>
#include <queue>
const int N = 26;
struct TrieNode{
    struct TrieNode *childs[N];
    bool isEnd = false;
    int pos = -1;
};

struct TrieNode *getNode(void){
    struct TrieNode * p = new TrieNode;
    for(int i=0;i<N;i++){
        p->childs[i] = NULL;
    }
    return p;
};

void insert(struct TrieNode *root, string k, int idx){
    struct TrieNode * curr = root;
    for(char c : k){
        int pos = c - 'a';
        if(!curr->childs[pos]){
            curr->childs[pos] = getNode();
        }
        curr = curr->childs[pos];
    }
    curr->isEnd = true;
    curr->pos = idx;
}

vector<int> search(struct TrieNode * root, string k, int start){
    struct TrieNode * curr = root;
    vector<int> ans;
    int n = k.length();
    for(int i = start; i < n; i++){
        int idx = k[i] - 'a';
        if(!curr->childs[idx]){
            break;
        }
        curr = curr->childs[idx];
        if(curr->pos != -1){
            ans.push_back(curr->pos);
        }
    }
    return ans;
}

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        TrieNode * root = getNode();
        int m = wordDict.size();
        for(int i=0;i<m;i++){
            insert(root, wordDict[i], i);
        }
        vector<string> ans;
        int start = 0;
        queue<pair<int, string> > q;
        q.push({0,""});
        int n = s.length();
        while(!q.empty()){
            auto [sz, str] = q.front();
            q.pop();
            if(sz == n){
                ans.push_back(str);
                continue;
            }
            vector<int> pos = search(root, s, sz);
            if(pos.size() == 0){
                continue;
            }
            for(auto i : pos){
                string t = wordDict[i];
                int addSZ = t.length();
                if(str.empty()){
                    q.push(make_pair(sz+addSZ, t));
                }else{
                    q.push(make_pair(sz+addSZ, str + " " + t));
                }
            }
        }
        return ans;
    }
};