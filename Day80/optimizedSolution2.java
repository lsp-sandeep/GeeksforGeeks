class Solution {

    public ArrayList<ArrayList<Integer>> levelOrder(Node root) {
        /**
         * This function implements the level order or bredth first search
         * using queue and interating for each level
         **/

        ArrayList<ArrayList<Integer>> out = new ArrayList<ArrayList<Integer>>();
        
        Queue<Node> nodeQ = new LinkedList<>();
        
        nodeQ.add(root);
        
        int currLevel = 0;
        
        while(!nodeQ.isEmpty()) {
            
            int lenQ = nodeQ.size();
            
            out.add(new ArrayList<Integer>());
            
            for(int i = 0; i < lenQ; i++) {
                
                Node nQ = nodeQ.poll();
                
                out.get(currLevel).add(nQ.data);
                
                if(nQ.left != null)
                    nodeQ.add(nQ.left);
                
                if(nQ.right != null)
                    nodeQ.add(nQ.right);
            }
            
        }

        return out;

    }
}