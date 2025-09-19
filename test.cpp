#include <iostream>
#include <vector>
#include <cstdlib>

#ifdef _WIN32
#include <windows.h>
#define sleep_ms(x) Sleep(x)
#else
#include <unistd.h>
#define sleep_ms(x) usleep((x)*1000)
#endif

using namespace std;

void drawArray(const vector<int>& arr){
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
    for(int x:arr) cout << x << " ";
    cout << "\n";
    for(int i=0;i<arr.size();i++){
        for(int j=0;j<arr[i];j++) cout << "#";
        cout << "\n";
    }
    sleep_ms(300);
}

void bubbleSort(vector<int>& arr){
    int n = arr.size();
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            drawArray(arr);
            if(arr[j]>arr[j+1])
                swap(arr[j],arr[j+1]);
        }
    }
    drawArray(arr);
}

int main(){
    srand(time(0));
    int n = 10;
    vector<int> arr(n);
    for(int i=0;i<n;i++) arr[i] = rand()%10+1;

    bubbleSort(arr);
    cout << "Sorted Array: ";
    for(int x:arr) cout << x << " ";
    cout << endl;
}
