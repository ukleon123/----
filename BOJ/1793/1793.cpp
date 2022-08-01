#include<iostream>

#include<vector>
#include<algorithm>


using namespace std;

void main(){
    int n;
    vector<int> dp;
    dp.push_back(1);
    while(cin >> n)
    {
        if(dp.size() >= n)
        {
            cout << dp[n - 1];
            continue;
        }
        else
        {
            int current = dp.size();
            while(current < n)
            {
                if(current % 2)
                {
                    dp.push_back(2 * dp[current - 1] + 1);
                }
                else
                {
                    dp.push_back(2 * dp[current - 1] - 1);
                }
                current++;
            }
        }
        cout << dp[n - 1];
    }
}