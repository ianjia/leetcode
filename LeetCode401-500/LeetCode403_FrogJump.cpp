class Solution {
public:
    bool canCross(vector<int>& stones) {
        unordered_map<int, unordered_set<int>> jumpMap;
        vector<int> diffVec = {-1, 0, 1};
        jumpMap[0] = {0};
        
        for (auto stone : stones) {
            if (jumpMap.find(stone) != jumpMap.end()) { // if the stones from where the current stone jumped from is accesible
                for (auto step : jumpMap[stone]) {
                    for (auto diff : diffVec) {
                        if (step + diff > 0) {
                            if (stone + step + diff == stones[stones.size() - 1]) { // if possible to reach end
                                return true;
                            }
                            jumpMap[stone + step + diff].insert(step + diff); // new stone adds where old stone starts from
                        }
                    }
                }
            }
        }
        
        return false;
    }
};