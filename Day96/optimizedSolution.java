import java.utils.*;

class Solution {

    public int getDistance(int[] point) {
        int x = point[0] * point[0];
        int y = point[1] * point[1];
        return x + y;
    }

    public int[][] kClosest(int[][] points, int k) {
        /**
         * This function returns the k closes points from origin
         * 
         * Approach:
         * 1) Initialize a max heap of points using euclidian distance comparator
         * 2) Add first k element directly to heap
         * 3) Add each of the remaining elements only if their distance is less than the head
         * 4) Remove each of the k elements back into a resultant array
         * 
         **/

        PriorityQueue<int[]> maxQ = new PriorityQueue<>(
            (a, b) -> getDistance(b) - getDistance(a)
            );
        
        for(int i = 0; i < k; i++)
            maxQ.add(points[i]);

        for(int i = k; i < points.length; i++) {
            if(getDistance(points[i]) < getDistance(maxQ.peek())) {
                maxQ.remove();
                maxQ.add(points[i]);
            }
        }
        
        int[][] res = new int[k][2];
        
        for(int i = 0; i < k; i++)
            res[i] = maxQ.remove();

        return res;
    }
}