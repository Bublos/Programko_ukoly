#include <iostream>

using namespace std;

template <typename T, int N>
class Array
{
    public:
        void fillArray(T val);
        void print();
        T* at(int idx);

    private:
        T items[N];
};

int main()
{
    Array<int,10>ar1;
    ar1.fillArray(1);
    *ar1.at(1)=2;
    ar1.print();

    Array<char,10>ar2;
    ar2.fillArray('a');
    *ar2.at(2)='b';
    ar2.print();
}

template<typename T, int N>
void Array<T,N>::fillArray(T val)
{
    for (int i=0;i<N;i++)
    {
        items[i]=val;
    }
}

template<typename T, int N>
void Array<T,N>::print()
{
    for (int i=0;i<N;i++)
    {
        cout<<items[i]<<" ";
    }
    cout<<endl;
}

template<typename T, int N>
T* Array<T,N>::at(int idx)
{
    return &items[idx];
}