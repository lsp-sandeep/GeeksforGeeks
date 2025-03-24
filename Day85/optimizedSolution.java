
class Node {
    int data;
    Node left, right;
   Node(int item)    {
        data = item;
        left = right = null;
    }
}

class Solution {
    
    ArrayList<Integer> inOrderRec(Node root, ArrayList<Integer> out) {
        /**
         * This function returns the inorder traversal of a given binary tree
         * 
         * Approach: Recursively add the left, root and right in that order
         * 
         * Time Complexity: O(n)
         * Space Compelxity: O(h)
         **/
        
        if(root == null) return out;

        inOrderRec(root.left, out);

        out.add(root.data);

        inOrderRec(root.right, out);
        
        return out;
    }
    
    ArrayList<Integer> inOrder(Node root) {
         
        ArrayList<Integer> out = new ArrayList<>();
        
        return inOrderRec(root, out);
    }
}