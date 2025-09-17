
# Задание 1

def exam(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        elif char in "({[":
            stack.append(char)
    # Если стек пуст - все скобки закрыты правильно
    return len(stack) == 0

# Тестирование

if __name__ == "__main__":
    print("Задание №1")
    test_cases = ["()", "()[]{}", "(]", "([])", "([)]", '((()))']
    for test in test_cases:
        result = exam(test)
        print(f"'{test}': {result}")
    print("\n")



# Задание 2

def merge(nums1, m, nums2, n):
    # Указатели для nums1, nums2 и результирующей позиции
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Если в nums2 остались элементы (nums1 уже закончился)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Тестирование
if __name__ == "__main__":
    print("Задание №2")

    # Пример 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Пример 1: {nums1}")  # [1, 2, 2, 3, 5, 6]
    
    # Пример 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"Пример 2: {nums1}")  # [1]
    
    # Пример 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Пример 3: {nums1}\n")  # [1]



# Задание 3

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    
    left = 0  # указатель на день покупки
    right = 1  # указатель на день продажи
    max_profit = 0
    
    while right < len(prices):
        # Если текущая цена больше цены покупки
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            # Нашли новую минимальную цену для покупки
            left = right
        right += 1
    
    return max_profit

# Тестирование
if __name__ == "__main__":
    print("Задание №3")
    # Пример 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Пример 1: {maxProfit(prices1)}")  # 5
    
    # Пример 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Пример 2: {maxProfit(prices2)}\n")  # 0



# Задание 4

def isAnagram(s, t):
    # Длина срок должна быть равна
    if len(s) != len(t):
        return False
    
    s_new = [char for char in s]
    t_new = [char for char in t]
    s_new.sort()
    t_new.sort()

    if s_new == t_new:
        return True
    return False

# Тестирование
if __name__ == "__main__":
    print("Задание №4")
    # Пример 1
    s1, t1 = "anagram", "nagaram"
    print(f"Пример 1: s = '{s1}', t = '{t1}': вывод {isAnagram(s1, t1)}")  # True

    
    # Пример 2
    s2, t2 = "rat", "car"
    print(f"Пример 2: s = '{s2}', t = '{t2}': вывод {isAnagram(s2, t2)}\n") # False



# Задание 5

class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t):
        self.requests.append(t)
        lower_bound = t - 3000
        
        while self.requests and self.requests[0] < lower_bound:
            self.requests.pop(0)
        
        return len(self.requests)

# Тестирование
if __name__ == "__main__":
    print("Задание №5")

    recentCounter = RecentCounter()
    print(recentCounter.ping(1)) # 1
    print(recentCounter.ping(100)) # 2 
    print(recentCounter.ping(3001)) # 3
    print(recentCounter.ping(3002)) # 3


