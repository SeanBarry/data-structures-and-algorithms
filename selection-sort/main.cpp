#include <vector>

using namespace std;

vector<int> selectionSort(vector<int> array)
{
    int currentIdx = 0;

    while (currentIdx < array.size() - 1)
    {
        int smallestIdx = currentIdx;

        for (int i = 0; i < array.size(); i++)
        {
            if (array[i] < array[smallestIdx])
            {
                smallestIdx = i;
            }

            swap(array[currentIdx], array[smallestIdx]);
            currentIdx++;
        }
    }

    return array;
}