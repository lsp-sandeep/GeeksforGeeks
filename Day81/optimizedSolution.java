
class Solution {
    int height(Node node) {
        /**
         * This function finds the number of edges
         * on the longest path from root to leaf node
         * 
         * Approach:
         * 1) if current node is null return height of 0
         * 2) Recursively find the number of edges for left and right
         * 
         * Time Complexity: O(n)
         * Space Complexity: O(h)
         **/
        
        if(node == null)
            return 0;
            
        int leftH = 0, rightH = 0;

        if(node.left != null)
            leftH = 1 + height(node.left);

        if(node.right != null)
            rightH = 1 + height(node.right);

        return (leftH > rightH ? leftH : rightH);
        
    }
}