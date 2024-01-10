#include <iostream>
using namespace std;


void vymenaHodnot(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int a = 5;
    int b = 4;

    cout<<"Puvodni a: "<<a<<"\nPuvodni b: "<<b;
    vymenaHodnot(&a, &b);
    cout<<"\n\nProhozene a: "<<a<<"\nProhozene b: "<<b;


    return 0;

}