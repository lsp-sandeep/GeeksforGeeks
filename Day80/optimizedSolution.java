

class Solution {
    public void levelOrderRec(Node root, int level, ArrayList<ArrayList<Integer>> out) {
        /**
         * This is the recursion helper function that call for both left and right nodes
         **/

        if(root == null)
            return;
        
        if(out.size() <= level)
            out.add(new ArrayList<Integer>());
        
        out.get(level).add(root.data);
        
        levelOrderRec(root.left, level + 1, out);
        levelOrderRec(root.right, level + 1, out);

        return;

    }

    public ArrayList<ArrayList<Integer>> levelOrder(Node root) {
        /**
         * This function implements the level order or bredth first search
         * using recursion to add elements at each level
         **/

        ArrayList<ArrayList<Integer>> out = new ArrayList<ArrayList<Integer>>();
        
        levelOrderRec(root, 0, out);

        return out;

    }
}