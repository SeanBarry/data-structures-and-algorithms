#include <vector>

using namespace std;

bool isMonotonic(vector<int> array) {
    if (array.size() < 2) {
        return true;
    }

    int start = array[0];
    int end = array[array.size() - 1];
    bool trendingUp = end > start;

    for (int i = 1; i < array.size() -1; i++) {
        if (trendingUp && array[i] < array[i - 1]) {
            return false;
        } else if (!trendingUp && array[i] > array[i - 1]) {
            return false;
        }
    }

    return true;
}