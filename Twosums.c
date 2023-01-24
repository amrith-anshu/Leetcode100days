/* Brute force
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
*/



class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> visited;
        int len = nums.size(); //
        for (int i = 0; i < len; ++i) {
            int n = nums[i];
            int complement = target - n;
            if (visited.count(complement)) {
                return {visited[complement], i};
            }
            visited[n] = i;  // assume that each input would have exactly one solution
        }
        return {};
    }
};
