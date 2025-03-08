import java.utils.*;

class Solution {
    public ArrayList<Integer> kLargest(int[] arr, int k) {
        /**
         * This function returns the k largest elements of an array
         * in descending order using priority queue (min heap)
         * 
         * Time Complexity: O(k + (n-k)*log(k) + k*log(k) + k/2) = O(n*log(k))
         * Space Complexity: O(k)
         **/
        
        // Initialize a priority queue of first k elements
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        for(int i = 0; i < k; i++) minQ.add(arr[i]);
        
        // Add each element if it is greater than the head
        for(int i = k; i < arr.length; i++) {
            if(minQ.peek() < arr[i]) {
                minQ.remove();
                minQ.add(arr[i]);
            }
        }
        
        // Initialize the result and add the each element
        ArrayList<Integer> res = new ArrayList<>();
        for(int i = 0; i < k; i++)
            res.add(minQ.remove());
        
        // Reverese the order of the result to descending
        int left = 0, right = k - 1;
        while(left < right) {
            int temp = res.get(right);
            res.set(right, res.get(left));
            res.set(left, temp);
            
            left++; right--;
        }
        
        return res;
    }
}