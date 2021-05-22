#include <vector>
#include <cmath>
using namespace std;

vector<int> sortedSquaredArray(vector<int> array)
{
    int smallIdx = 0;
    int largeIdx = array.size() - 1;
    vector<int> sorted(array.size(), 0);

    for (int i = array.size() - 1; i >= 0; i--)
    {
        int small = array[smallIdx];
        int large = array[largeIdx];

        if (abs(large) > abs(small))
        {
            sorted[i] = large * large;
            largeIdx--;
        }
        else
        {
            sorted[i] = small * small;
            smallIdx++;
        }
    }
    return sorted;
}
