/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    bool check_leaf(TreeNode* node){
        if(node->left == NULL && node->right==NULL)
        return true;
        else
        return false;
    }
    int sum=0;
    int getans(TreeNode* root){
        if(root == NULL)
        return 0;
        else{
            if(root->left!=NULL){
                if(check_leaf(root->left))
                sum+=root->left->val;
                else getans(root->left);
            }
             if(root->right!=NULL){
                 getans(root->right);
            }
        }
        return sum;
    }
    int sumOfLeftLeaves(TreeNode* root) {
        getans(root);
        return sum;
    }
};