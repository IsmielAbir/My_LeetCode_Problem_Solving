/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean check_leaf(TreeNode node){
        if(node.left == null && node.right==null)
        return true;
        else
        return false;
    }
    int sum=0;
    public int getans(TreeNode root){
        if(root==null)
        return 0;
        else{
            if(root.left!=null){
                if(check_leaf(root.left))
                sum+=root.left.val;
                else getans(root.left);
            }
             if(root.right!=null){
               
             getans(root.right);
            }

        }
        return sum;

    }
    public int sumOfLeftLeaves(TreeNode root) {
        getans(root);
        return sum;

        
    }
}