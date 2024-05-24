#include <iostream>
using namespace std;

int main(){
    int x = 5;
    float y = 3.14;
    char c = 'A';
    double d = 3.14159;
    long l = 1234567890;

    if(x>0){
        cout<<"x is positive"<<endl;
    }
    else if(x<0){
        cout<<"x is negative"<<endl;
    }
    else{
        cout<<"x is zero"<<endl;
    }

    for(int i=0; i<5; i++){
        cout<<i<<endl;
    }

    do{
        cout<<x<<endl;
        x--;
        if(x==2){
            break;
        }
    }while(x>0);

    while(x > 0){
        x--;
        if(x == 2){
            continue;
        }
        cout << x << endl;
    }

    void myFunction() {
        const int MAX_VALUE = 100;
        static int count = 0;

        class MyClass {
            private:
                int privateVar;

            public:
                void setPrivateVar(int value) {
                    privateVar = value;
                }
        };

        struct MyStruct {
            int x;
            int y;
        };

        union MyUnion {
            int a;
            float b;
        };

        enum MyEnum {
            VALUE1,
            VALUE2,
            VALUE3
        };

        typename MyType;

        namespace MyNamespace {
            int x;
            int y;
        }

        using namespace std;

        virtual void myVirtualFunction() {
            cout << "Virtual function" << endl;
        }

        class Base {
            public:
                virtual void myVirtualFunction() {
                    cout << "Base class virtual function" << endl;
                }
        };

        class Derived : public Base {
            public:
                void myVirtualFunction() override {
                    cout << "Derived class virtual function" << endl;
                }
        };

        MyClass obj;
        obj.setPrivateVar(10);

        int* ptr = nullptr;

        bool flag = true;
        bool flag2 = false;

        int* dynamicArray = new int[10];
        delete[] dynamicArray;

        try {
            throw runtime_error("An error occurred");
        } catch(const exception& e) {
            cout<<"Caught exception: "<<e.what()<<endl;
        }

        template<typename T>
        T add(T a, T b) {
            return a + b;
        }

        friend class FriendClass;

        inline int multiply(int a, int b) {
            return a * b;
        }

        class MyClass {
            public:
                MyClass operator+(const MyClass& other) {
                    //Comment
                }
                explicit MyClass(int value) {
                    //Comment
                }
        };

        constexpr int MAX_SIZE = 100;

        mutable int counter = 0;

        register int regVar = 10;

        volatile int volVar = 20;

        asm("movl %eax, %ebx");

        export int exportedVar;

        import int importedVar;

        size_t size = sizeof(int);

        Base* basePtr = dynamic_cast<Base*>(derivedPtr);

        Derived* derivedPtr = static_cast<Derived*>(basePtr);

        int* intPtr = reinterpret_cast<int*>(floatPtr);

        const int* constPtr = const_cast<const int*>(intPtr);

        typeid(int);

        decltype(x) result;

        void myFunction() noexcept {
            //This is a comment :D
        }
    }

    int a = 5;
    int b = 3;

    int sum = a + b;
    int difference = a - b;
    int product = a * b;
    int quotient = a / b;
    int remainder = a % b;

    a++;
    b--;
    a = 10;
    b += 5;
    a -= 3;
    b *= 2;
    a /= 4;
    b %= 3;

    bool isEqual = (a == b);
    bool isNotEqual = (a != b);
    bool isGreater = (a > b);
    bool isLess = (a < b);
    bool isGreaterOrEqual = (a >= b);
    bool isLessOrEqual = (a <= b);

    bool logicalAnd = (a > 0) && (b < 10);
    bool logicalOr = (a > 0) || (b < 10);
    bool logicalNot = !(a > 0);

    int bitwiseAnd = a & b;
    int bitwiseOr = a | b;
    int bitwiseXor = a ^ b;
    int bitwiseNot = ~a;
    int leftShift = a << 2;
    int rightShift = a >> 2;

    int max = (a > b) ? a : b;

    string s = "Hello";
    cout << s.length() << endl;

    return 0;

    string s = "Hello";

    return 0;
}
