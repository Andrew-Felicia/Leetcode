
## 1.basic library:
```text
   
java.util
├── List
│   ├── ArrayList
│   └── LinkedList
│
├── Map
│   ├── HashMap
│   │   ├── computeIfAbsent()
│   │
│   └── TreeMap
│
└── Set
│   ├── HashSet
│   └── TreeSet
│   
├── stream()
│ 	├── filter()      // keep some elements
│	├── map()         // transform elements
│	├── flatMap()     // flatten nested collections
│	├── sorted()      // sort
│	├── distinct()    // remove duplicates
│	├── limit()       // take first n
│	├── skip()        // skip first n
│	├── count()       // count elements
│	├── findFirst()   // first matching element
│	├── anyMatch()    // exists?
│	├── allMatch()    // all satisfy?
│	├── reduce()      // combine into one value
│	└── toList()      // collect results
│
│
│
│
│
│
│

  
```


```text
java.lang
├── Object
│   ├── toString()
│   ├── equals(Object)
│   ├── hashCode()
│   ├── getClass()
│   └── clone()
│
├── String
│   ├── length()
│   ├── charAt(int) -> char
│   ├── substring()
│   ├── indexOf()
│   ├── contains()
│   ├── startsWith()
│   ├── endsWith()
│   ├── equals()
│   ├── equalsIgnoreCase()
│   ├── compareTo()
│   ├── split()
│   ├── replace()
│   ├── trim()
│   ├── toLowerCase()
│   ├── toUpperCase()
│   ├── isEmpty()
│   └── valueOf()
│
├── StringBuilder
│   ├── append()
│   ├── insert()
│   ├── delete()
│   ├── reverse()
│   ├── length()
│   ├── setCharAt()
│   └── toString()
│
├── Math
│   ├── abs()
│   ├── max()
│   ├── min()
│   ├── sqrt()
│   ├── pow()
│   ├── random()
│   ├── ceil()
│   ├── floor()
│   └── round()
│
├── System
│   ├── out.println()
│   ├── currentTimeMillis()
│   ├── nanoTime()
│   ├── arraycopy()
│   ├── getenv()
│   └── exit()
│
├── Integer
│   ├── parseInt()
│   ├── valueOf()
│   ├── toString()
│   ├── compare()
│   ├── MAX_VALUE
│   └── MIN_VALUE
│
├── Double
│   ├── parseDouble()
│   ├── valueOf()
│   ├── compare()
│   ├── isNaN()
│   ├── isInfinite()
│   └── toString()
│
├── Boolean
│   ├── parseBoolean()
│   ├── valueOf()
│   └── toString()
│
├── Character
│   ├── isDigit()
│   ├── isLetter()
│   ├── isUpperCase()
│   ├── isLowerCase()
│   ├── toUpperCase()
│   └── toLowerCase()
│
├── Enum
│   ├── name()
│   ├── ordinal()
│   └── valueOf()
│
├── Throwable
│   ├── getMessage()
│   ├── printStackTrace()
│   └── getCause()
│
├── Exception
│   └── (inherits Throwable methods)
│
├── RuntimeException
│   ├── NullPointerException
│   ├── IllegalArgumentException
│   ├── IndexOutOfBoundsException
│   └── ArithmeticException
│
├── Thread
│   ├── start()
│   ├── run()
│   ├── sleep()
│   ├── join()
│   ├── interrupt()
│   └── currentThread()
│
└── Class
    ├── getName()
    ├── getMethods()
    ├── getFields()
    └── getSuperclass()
```


## 2."list"
`int[]`
`char []`
`string[]`


## 3.String 
`.tocharArray()`


## 4.sort
Arrays.sort()


## 5.JVM, JVM 内存溢出

## 6.how to make java projects portable?


## 7.lambda, regex.


## 8.length vs length()
`.length` is a field (stored value), while `.length()` is a method (a function call).
```text
Array      → length
String     → length()
Collection → size()
```

## 9.能够通过某种策略迅速排出大量数据（在每一个循环排掉50%的无效数据）的算法通常都很快，O(log(n)).


## 10.java stream chain
Java Streams are all about **chaining operations together**.

General pattern:

```
collection.stream().intermediateOperation1()          
                   .intermediateOperation2()          
                   .terminalOperation();
```

---

### Example 1: Filter + Map + Collect

Suppose:

```
List<String> names = List.of("alice", "bob", "charlie");
```

Get names longer than 3 characters and uppercase them:

```
List<String> result = names.stream().filter(name -> name.length() > 3)                                               .map(String::toUpperCase)                                                        .toList();
System.out.println(result);
```

Output:

```
[ALICE, CHARLIE]
```

---

### Example 2: Sum numbers

```
List<Integer> nums = List.of(1, 2, 3, 4, 5);
```

Sum the even numbers:

```
int sum = nums.stream().filter(n -> n % 2 == 0)                                                         .mapToInt(Integer::intValue)             
                       .sum();
System.out.println(sum);
```

Output:

```
6
```

---

### Example 3: Sort + Limit

```
List<Integer> nums = List.of(9, 1, 5, 3, 7);
```

Get the smallest 3 numbers:

```
List<Integer> result = nums.stream()                           
                           .sorted()                           
                           .limit(3)                                                                        .toList();
System.out.println(result);
```

Output:

```
[1, 3, 5]
```

---

### Example 4: Count

Count how many strings start with `'a'`:

```
List<String> words = List.of("apple", "banana", "avocado", "pear");
long count = words.stream()                  
                  .filter(w -> w.startsWith("a"))                                                  .count();
System.out.println(count);
```

Output:

```
2
```

---

### Example 5: Find First

```
Optional<String> result = words.stream()         
                               .filter(w -> w.length() > 5)                                                     .findFirst();
System.out.println(result.orElse("Not Found"));
```

Output:

```
banana
```

---

### Example 6: Remove duplicates

```
List<Integer> nums = List.of(1, 2, 2, 3, 3, 3, 4);
```

```
List<Integer> result = nums.stream()                          
                           .distinct()                           
                           .toList();
System.out.println(result);
```

Output:

```
[1, 2, 3, 4]
```

---

### Example 7: LeetCode-style chain

Given:

```
List<Integer> nums =  List.of(1,2,3,4,5,6,7,8,9,10);
```

Get squares of even numbers greater than 4:

```
List<Integer> result = nums.stream()                           
						   .filter(n -> n > 4)                           
						   .filter(n -> n % 2 == 0)                           
						   .map(n -> n * n)                           
						   .toList();
 System.out.println(result);
```

Output:

```
[36, 64, 100]
```



## 11. Q&A

why set.contains() is faster than ArrayList.contains()?

Because **`Set` (usually `HashSet`) uses hashing**, while **`ArrayList` uses linear search**.



to solve the same quesion and use same algorithms, why java runs faster than python?

Java usually runs faster than Python because Java code is JIT-compiled into optimized machine code with static types, while Python executes dynamically typed objects through an interpreter, creating much more runtime overhead even when the algorithm is the same.


## 12.java "slice":

```java
Arrays.copyOfRange(nums, 1, 3);
```


## 13. divide and conquer(分治)


