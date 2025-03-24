class Node {
    int data;
    Node left, right;

    public Node(int d)
    {
        data = d;
        left = right = null;
    }
}

class Solution {
    
    boolean isLeaf(Node node) {
        if(node != null && node.left == null && node.right == null)
            return true;
        return false;
    }
    
    void addLeftBoundary(Node node, ArrayList<Integer> res) {
        if(node == null) return;
        
        if(!isLeaf(node)) res.add(node.data);
        
        if(node.left == null)
            addLeftBoundary(node.right, res);
        else
            addLeftBoundary(node.left, res);
    }
    
    void addLeaves(Node node, ArrayList<Integer> res) {
        if(node == null) return;

        if(isLeaf(node)) res.add(node.data);
        
        addLeaves(node.left, res);
        addLeaves(node.right, res);
    }

    void addRightBoundary(Node node, ArrayList<Integer> res) {
        if(node == null) return;
        
        if(node.right == null)
            addRightBoundary(node.left, res);
        else
            addRightBoundary(node.right, res);

        if(!isLeaf(node)) res.add(node.data);
    }

    ArrayList<Integer> boundaryTraversal(Node node) {
        ArrayList<Integer> res = new ArrayList<>();
        
        if(node == null) return res;
        
        if(!isLeaf(node)) res.add(node.data);
        
        addLeftBoundary(node.left, res);
        addLeaves(node, res);
        addRightBoundary(node.right, res);
        
        return res;
    }
}
