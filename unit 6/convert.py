# package Q2;

# public class ArrayTest {
#     public static void main(String[] args) {
#         int[] nums = new int[100];
#         for (int lcv = 0; lcv < 100; lcv++)
#             nums[lcv] = lcv + 1;

#         for (int lcv = 0; lcv < 100; lcv++)
#             System.out.print(nums[lcv] + " ");
#         System.out.println();

#         char[] hello = "Hello, world!".toCharArray();
#         // For-each Loop:
#         // for (var x in array) {}
#         for (char x : hello)
#             System.out.print(x);
#         System.out.println();

#         String[] words = {"hello", "world", "wow", "cool", "wowsers", "cool beans"};
#         // for (String temp : words) { do stuff }
#         for (int lcv = 0; lcv < words.length; lcv++)
#             System.out.println(words[lcv]);

nums = [0]*100

for lcv in range(100):
    nums[lcv] = lcv+1

for lcv in range(100):
    print(nums[lcv],end = " ") # end = changes the ending of a print
print()

hello = "Hello World!"

for letter in hello:
    print(letter,end="")
print()

words = ["hello", "world", "wow", "cool", "wowsers", "cool beans"]

for lcv in range(len(words)):
    #for word in words:
    #   print(word)
    print(words[lcv])

"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 
Hello World!
hello
world
wow
cool
wowsers
cool beans
"""