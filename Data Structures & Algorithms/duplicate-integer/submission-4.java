
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbers = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (numbers.contains(num)) {
                return true;   
            } else {
                numbers.add(num);
            }
        }
        return false;

        
    }
}