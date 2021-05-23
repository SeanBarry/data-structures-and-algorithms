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

struct Item
{
    BinaryTree *root;
    int depth;
};

int nodeDepths(BinaryTree *root)
{
    vector<Item> stack = {{root, 0}};
    int sumOfDepths = 0;
    while (stack.size() > 0)
    {
        BinaryTree *node = stack.back().root;
        int depth = stack.back().depth;
        stack.pop_back();

        if (node == nullptr)
        {
            continue;
        }

        sumOfDepths += depth;
        stack.push_back(Item{node->left, depth + 1});
        stack.push_back(Item{node->right, depth + 1});
    }
    return sumOfDepths;
}
