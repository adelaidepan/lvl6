# 1、以Student类为例，在Python中，定义类如下：



class Student(object):
    pass

# （Object）表示该类从哪个类继承下来的，Object类是所有类都会继承的类。

# 2、实例：定义好了类，就可以通过Student类创建出Student的实例，创建实例是通过类名+()实现：



student = Student()

# 3、由于类起到模板的作用，因此，可以在创建实例的时候，把我们认为必须绑定的属性强制填写进去。这里就用到Python当中的一个内置方法__init__方法，例如在Student类时，把name、score等属性绑上去:



class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score1234

# 这里注意：（1）、__init__方法的第一参数永远是self，表示创建的类实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。（2）、有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去：



student = Student("Hugh", 99)
>>>student.name
"Hugh"
>>>student.score
9912345

# 另外，这里self就是指类本身，self.name就是Student类的属性变量，是Student类所有。而name是外部传来的参数，不是Student类所自带的。故，self.name = name的意思就是把外部传来的参数name的值赋值给Student类自己的属性变量self.name。

# 4、和普通数相比，在类中定义函数只有一点不同，就是第一参数永远是类的本身实例变量self，并且调用时，不用传递该参数。除此之外，类的方法(函数）和普通函数没啥区别，你既可以用默认参数、可变参数或者关键字参数（*args是可变参数，args接收的是一个tuple，**kw是关键字参数，kw接收的是一个dict）。

# 5、既然Student类实例本身就拥有这些数据，那么要访问这些数据，就没必要从外面的函数去访问，而可以直接在Student类的内部定义访问数据的函数（方法），这样，就可以把”数据”封装起来。这些封装数据的函数是和Student类本身是关联起来的，称之为类的方法：



class Student(obiect):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s: %s" % (self.name, self.score)123456



>>>student = Student("Hugh", 99)
>>>student.print_score
Hugh: 99123

# 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score。而如何打印，都是在Student类的内部定义的，这些数据和逻辑被封装起来了，调用很容易，但却不知道内部实现的细节。

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线，在Python中，实例的变量名如果以开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：



class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print "%s: %s" %(self.__name,self.__score)1234567

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：



>>> student = Student('Hugh', 99)
>>> student.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'12345

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：



class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score12345678

# 如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：



class Student(object):
    ...

    def set_score(self, score):
        self.__score = score12345



# ---------------------

# 本文来自 CLHugh 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/CLHugh/article/details/75000104?utm_source=copy 
