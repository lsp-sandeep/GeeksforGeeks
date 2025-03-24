class Node
{
    int data;
    Node left, right;
   Node(int item)
   {
        data = item;
        left = right = null;
    }
}

class Solution {
    void mirror(Node node) {
        /**
         * This functions inverts the given binary tree to its mirror
         * 
         * Approach:
         * 1) mirror the left and right nodes recursively
         * 2) Swap the left and right node after mirroring
         * 
         * Time Complexity: O(n)
         * Space Complexity: O(h)
         **/
        
        if(node == null)
            return;
            
        mirror(node.left); mirror(node.right);
        
        Node temp;
        temp = node.right;
        node.right = node.left;
        node.left = temp;
        
    }
}
