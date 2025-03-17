import java.utils.*;

class Solution {
    public ArrayList<Double> getMedian(int[] arr) {
        /**
         * This function returns an array of medians of the elements encountered so far
         * 
         * Approach:
         * 1) Use a maxHeap and minHeap that hold almost equal elements
         * 2) All elements of minHeap must be less than maxHeap
         * 3) Return the extra element or average of minHeap and maxHeap top
         * 
         * Time Complexity: O(n*log(n))
         * Space Complexity: O(n)
         **/

        ArrayList<Double> medians = new ArrayList<>();

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for(int i = 0; i < arr.length; i++) {
            if(i%2 == 0) {
                boolean flag = false;
                if(!minHeap.isEmpty()) {
                    if(arr[i] > minHeap.peek())
                        flag = true;
                }
                
                if(flag) {
                    maxHeap.add(minHeap.remove());
                    minHeap.add(arr[i]);
                } else {
                    maxHeap.add(arr[i]);
                }
                medians.add((double)maxHeap.peek());
            } else {
                if(arr[i] < maxHeap.peek()) {
                    minHeap.add(maxHeap.remove());
                    maxHeap.add(arr[i]);
                } else {
                    minHeap.add(arr[i]);
                }
                medians.add((double)(minHeap.peek() + maxHeap.peek())/2);
            }

        }
        return medians;
    }
}