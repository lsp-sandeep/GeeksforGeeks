class Solution {
    
    int findMaxSumRec(Node node, int[] res) {
        
        if(node == null) return 0;
        
        int leftMax = findMaxSumRec(node.left, res);
        int rightMax = findMaxSumRec(node.right, res);
        
        leftMax = (leftMax > 0 ? leftMax : 0);
        rightMax = (rightMax > 0 ? rightMax : 0);
        
        int splitMax = node.data + leftMax + rightMax;
        
        res[0] = splitMax > res[0] ? splitMax : res[0];
        
        int nonSplitMax = node.data + (
                    leftMax > rightMax ? leftMax : rightMax
                );

        return nonSplitMax;
    }
    
    // Function to return maximum path sum from any node in a tree.
    int findMaxSum(Node node) {

        int[] res = {node.data};
        
        findMaxSumRec(node, res);
        
        return res[0];
    }
}
