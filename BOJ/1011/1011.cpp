#include<iostream>
#include<cmath>

using namespace std;

int solve(double dist){
    double tmp = round(sqrtl(dist));
    double interval = tmp * 2;
    double standard = (interval / 2) + tmp * (tmp - 1);
    if (standard >= dist){
        return tmp * 2 - 1;
    }
    else{
        return tmp * 2;
    }

    
}

int main(){
    int num;
    cin.tie(0);
    ios::sync_with_stdio(0);
    cin >> num ;
    double* input = new double[num];
    for(int i = 0; i < num; i ++){
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        input[i] = tmp2 - tmp1;
    }
    for(int i = 0; i < num; i ++){
        cout << solve(input[i]) << endl;
    }
}