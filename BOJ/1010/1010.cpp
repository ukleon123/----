#include<iostream>

using namespace std;
int main(){
    int num = 0;
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> num;
    int** arr = new int*[num];

    for(int i = 0; i < num; i++){
        arr[i] = new int[2];
        cin >> arr[i][0] >> arr[i][1];
    }
    for(int i = 0; i < num; i++){
        double res = 1; // 비교적 정확한 답을 내는 것 같지만 double 로 인해 오류가 발생하는 것으로 보임
        double up = arr[i][1];
        double down = 1;
        if(arr[i][1] / 2 < arr[i][0]){
            arr[i][0] = arr[i][1] - arr[i][0];
        }
        for(int j = 0; j < arr[i][0]; j++){
            res *= up--/down++;
        }
        cout << (int)res << endl;
    }
}