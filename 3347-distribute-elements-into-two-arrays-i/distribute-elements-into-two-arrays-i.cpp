class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        vector<int> list1;
        vector<int> list2;
        
        list1.push_back(nums[0]);
        list2.push_back(nums[1]);
        
        for(int k = 2; k < nums.size(); k++){
            if(list1.back() > list2.back()){
                list1.push_back(nums[k]);
            }
            else{
                list2.push_back(nums[k]);
            }
        }
        
        int k = 0;
        
        for(int num : list1){
            nums[k++] = num;
        }
        
        for(int num : list2){
            nums[k++] = num;
        }

        return nums;
    }
};