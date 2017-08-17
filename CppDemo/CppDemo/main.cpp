#include <QCoreApplication>

#include <iostream>
#include <vector>

//using声明别名
template< class T >
class ClassA {
    T data;
public:
    ClassA(T dataR): data(dataR) {
    }
    void show() const {
        std::cout << data << std::endl;
    }
};
template< typename T >
using Table = std::vector< ClassA<T> >; //有模版的别名不能声明在函数内

//constexpr 常量表达式，编译器直接推断值。
constexpr int new_size()
{
    return 42;
}
constexpr size_t scale(size_t arg)
{
    return new_size() * arg;
}

//c++11测试体
void TestSTLObject() {
   std::string str = "Hello";
   std::vector<std::string> v;

   // uses the push_back(const T&) overload, which means
   // we'll incur the cost of copying str
   v.push_back(str);
   std::cout << "After copy, str is \"" << str << "\"\n";

   // uses the rvalue reference push_back(T&&) overload,
   // which means no strings will be copied; instead, the contents
   // of str will be moved into the vector.  This is less
   // expensive, but also means str might now be empty.
   v.push_back(std::move(str));
   std::cout << "After move, str is \"" << str << "\"\n";

   std::cout << "The contents of the vector are \"" << v[0]
                                        << "\", \"" << v[1] << "\"\n";

   const char strt[] = "How many characters does this string contain?";
   std::cout << "without null character: " << std::strlen(strt) << '\n'
               << "with null character: " << sizeof strt << '\n';

   constexpr    int mf = 20;
   constexpr    int limit = mf+10;
   constexpr    int siz = new_size();


    std::cout<<scale(2)<<std::endl;
    std::cout<<scale(mf)<<std::endl;
    int xa = 23;
    std::cout<<scale(xa)<<std::endl;

    static constexpr std::string kAdminDb = "admin"_sd;
    std::cout<<"kAdminDb"<<kAdminDb<<std::endl;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    TestSTLObject();

    return a.exec();
}
