#include<iostream>

using namespace std;
int combination(int primary, int secondary){
    if(secondary == 1){
        return primary;
    }
    else if (primary == secondary || secondary == 0){
        return 1;
    }
    else {
        return combination(primary - 1, secondary) + combination(primary - 1, secondary - 1);
    }
}
int main (){
    int num = 0;
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> num;
    int** arr = new int*[num];

    for(int i = 0; i < num; i++){
        arr[i] = new int[2];
        cin >> arr[i][0] >> arr[i][1];
        if(!(arr[i][0] == arr[i][1]) &&arr[i][1] / 2 < arr[i][0]){
            arr[i][0] = arr[i][1] - arr[i][0];
        }
        cout << combination(arr[i][1], arr[i][0]) << endl;
    }
    
    
}
//시간 초과가 자꾸발생한다. 시간 초과를 해결할 수 있는 효과적인 코드가 필요할 것 같다.