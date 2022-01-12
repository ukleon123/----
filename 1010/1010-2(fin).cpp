#include<iostream>
#include<vector>

using namespace std; 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int num;
    int primary, secondary;
    cin >> num;
    for(int i = 0; i < num; i ++){
        long long result = 1;
        cin >> secondary >> primary;
        if(secondary > primary/2) secondary = primary - secondary;
        for(int j = 1; j <= secondary; j++){
            result *= primary--;
            result /= j;
        }
        cout << result << endl;
    }
}