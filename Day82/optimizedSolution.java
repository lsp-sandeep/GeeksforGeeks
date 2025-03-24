
class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {
    
    int[] getHeightDiameter(Node root) {
        /**
         * This function recursivesly finds the height and diameter
         * of a binary tree
         * 
         * Approach:
         * 1) The height is the max of left and right nodes
         * 2) The diameter is the max of left, right and sum of height
         * 
         * Time Complexity: O(n)
         * Space Complexity: O(h)
         **/

        if(root == null)
            return new int[] {0, 0};
        
        int leftH, leftD, rightH, rightD;
        leftH = leftD = rightH = rightD = 0;
        
        if(root.left != null) {
            int[] leftHD = getHeightDiameter(root.left);
            leftH = 1 + leftHD[0];
            leftD = leftHD[1];
        }
            
        if(root.right != null) {
            int[] rightHD = getHeightDiameter(root.right);
            rightH = 1 + rightHD[0];
            rightD = rightHD[1];
        }
        
        int D = leftH + rightH, d = leftD > rightD ? leftD : rightD;
        
        int[] res = {
                leftH > rightH ? leftH : rightH,
                D > d ? D : d
            };
            
        return res;

    }
    
    int diameter(Node root) {
        // This function calls the above and returns the diameter
        
        int[] res = getHeightDiameter(root);
        
        return res[1];
        
    }
}
