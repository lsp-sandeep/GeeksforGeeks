class Solution {

    public static Node buildTreeRec(
            int inorder[], int preorder[], int rootIdx, int inBegin, int inEnd
        ) {
        /**
         * This function uses recursion to construct a binary tree from
         * inorder and preorder traversals of a binary tree
         * 
         * Approach:
         * 1) Initialize the root index and the range of inorder search for each call
         * 2) Search for the root value in the inorder array
         * 3) Construct the left node by incrementing root index by 1
         * 4) Search in the left side of the inorder index for left node
         * 5) Construct the right node by moving the root index after inorder index
         * 6) Search in the right side of the inorder index for right node
         * 
         * Time Complexity: O(n)
         * Space Complexity: O(h)
         **/
        
        if(rootIdx > preorder.length - 1 || inEnd < inBegin)
            return null;
            
        Node root = new Node(preorder[rootIdx]);
        
        int inIdx = 0;
        
        for(int i = inBegin; i <= inEnd; i++) {
            if(inorder[i] == preorder[rootIdx]) {
                inIdx = i;
            }
        }
        
        root.left = buildTreeRec(
                inorder, preorder, rootIdx + 1, inBegin, inIdx - 1
            );
        
        root.right = buildTreeRec(
                inorder, preorder, rootIdx + inIdx - inBegin + 1, inIdx + 1, inEnd
            );

        return root;
    }
    
    public static Node buildTree(int inorder[], int preorder[]) {

        return buildTreeRec(
            inorder, preorder, 0, 0, inorder.length - 1
        );
    }
}