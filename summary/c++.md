
## 1.basic library



STL:
```text
<string>
<cctype>
<algorithm>
```

Stanford Library


```c++
#include <iostream>
#include <algorithm> // Required header
#include <vector>

int main() {
    // 1. Comparing two values
    int a = 10, b = 20;
    int smallest_two = std::min(a, b); 

    // 2. Comparing a list of values (Initializer List)
    int smallest_list = std::min({5, 3, 9, 1}); 

    // 3. Finding the minimum in a container (Vector/Array)
    std::vector<int> vec = {7, 2, 8, 4};
    auto it = std::min_element(vec.begin(), vec.end());
    int smallest_container = *it; // Dereference iterator to get value
}

```