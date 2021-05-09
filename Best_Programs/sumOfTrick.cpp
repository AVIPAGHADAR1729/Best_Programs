#include <iostream>

using namespace std;
/*
long sumOfArray(int i,int arr[]){
	if(i<0) return 0;
	return sumOfArray(i-1,arr) + arr[i];

}

long sumOfDigits(long long n){
	if(n == 0) return 0;
	return sumOfDigits(n/10) + n % 10;
}*/

long sumOfArray(int i,int arr[]){
	return i<0 ? 0 : sumOfArray(i-1,arr) + arr[i];
}

long sumOfDigits(long n){
	return n == 0 ? 0 : sumOfDigits(n/10) + n%10;
}

int main(){
  int arr[] = {10,20,1,5,3,4};
  cout<<"sumOfArray:) "<<sumOfArray(5,arr)<<endl;
  cout<<"sumOfArray:) "<<sumOfArray(3,arr)<<endl;
  cout<<"sumOfDigits:) "<<sumOfDigits(112371243)<<endl;


}