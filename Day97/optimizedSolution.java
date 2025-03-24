import java.utils.*;

class Solution {
    // Function to merge K sorted linked list.
    Node mergeTwoLists(Node left, Node right) {
        if(left == null) return right;
        if(right == null) return left;
        
        Node head;
        if(left.data < right.data) {
            head = left; left = left.next;
        } else {
            head = right; right = right.next;
        }
        Node curr = head;
        while(left != null && right != null) {
            if(left.data < right.data) {
                curr.next = left;
                left = left.next;
                curr = curr.next;
            } else {
                curr.next = right;
                right = right.next;
                curr = curr.next;
            }
        }
        
        while(left != null) {
            curr.next = left;
            left = left.next;
            curr = curr.next;
        }
        
        while(right != null) {
            curr.next = right;
            right = right.next;
            curr = curr.next;
        }
        
        return head;
    }

    Node mergeKLists(List<Node> arr) {
        /**
         * This function merges an array of sorted linked lists
         * 
         * Approach:
         * Use inplace merge algorithm for two linked lists
         * and extend it to an array
         * 
         * Time Complexity: O(n)
         * Space Complexity: O(1)
         **/

        Node head = arr.get(0);
        
        for(int i = 1; i < arr.size(); i++)
            head = mergeTwoLists(head, arr.get(i));
        
        return head;
    }
}