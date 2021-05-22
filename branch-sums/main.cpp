#include <vector>

using namespace std;

class BinaryTree
{
public:
    int value;
    BinaryTree *left;
    BinaryTree *right;

    BinaryTree(int value)
    {
        this->value = value;
        left = nullptr;
        right = nullptr;
    }
};

void branchSumsHelper(BinaryTree *tree, int sum, vector<int> &results)
{
    int runningSum = sum += tree->value;

    if (tree->left)
    {
        branchSumsHelper(tree->left, runningSum, results);
    }

    if (tree->right)
    {
        branchSumsHelper(tree->right, runningSum, results);
    }

    if (tree->right == nullptr && tree->left == nullptr)
    {
        results.push_back(runningSum);
    }
}

vector<int> branchSums(BinaryTree *root)
{
    vector<int> results;
    branchSumsHelper(root, 0, results);
    return results;
}
