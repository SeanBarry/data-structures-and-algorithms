#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void countingSort(vector<int> &array, int digit);
int myPow(int base, int exponent);

vector<int> radixSort(vector<int> array)
{
    if (array.size() == 0)
    {
        return array;
    }

    int maxNumber = *max_element(array.begin(), array.end());
    int maxNumberLen = to_string(maxNumber).length();

    for (int i = 0; i < maxNumberLen; i++)
    {
        countingSort(array, i);
    }

    return array;
}

void countingSort(vector<int> &array, int digit)
{
    vector<int> sortedArray(array.size(), 0);
    vector<int> countArray(10, 0);

    int digitColumn = myPow(10, digit);

    for (int i = 0; i < array.size(); i++)
    {
        int countIndex = array[i] / digitColumn % 10;
        countArray[countIndex]++;
    }

    for (int i = 1; i < 10; i++)
    {
        countArray[i] += countArray[i - 1];
    }

    for (int i = array.size() - 1; i > -1; i--)
    {
        int countIndex = array[i] / digitColumn % 10;
        countArray[countIndex]--;
        int sortedIndex = countArray[countIndex];
        sortedArray[sortedIndex] = array[i];
    }

    for (int i = 0; i < array.size(); i++)
    {
        array[i] = sortedArray[i];
    }
}

int myPow(int base, int exponent)
{
    int result = 1;
    for (int i = 1; i <= exponent; i++)
    {
        result *= base;
    }
    return result;
}
