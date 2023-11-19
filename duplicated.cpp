#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Create an unordered set to store unique elements
        unordered_set<int> uniqueSet;
        
        // Iterate through the vector
        for (int num : nums) {
            // If the element is already in the set, it's a duplicate
            if (uniqueSet.count(num) > 0) {
                return true;
            }
            // Otherwise, insert the element into the set
            uniqueSet.insert(num);
        }
        
        // No duplicates found
        return false;
    }
};

int main() {
    Solution solution;
    
    vector<int> nums1 = {1, 2, 3, 1};
    cout << solution.containsDuplicate(nums1) << endl;  // Output: 1 (true)
    
    vector<int> nums2 = {1, 2, 3, 4};
    cout << solution.containsDuplicate(nums2) << endl;  // Output: 0 (false)
    
    return 0;
}
